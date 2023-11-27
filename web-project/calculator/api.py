import json
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from .function import send_webhook, send_embed, checkContributor, getCredentialForNonLoginRequired, loadContent
from .models import UserQueue, Token
from django.contrib import messages
from .forms import UserQueueForm
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.urls import reverse
from django.utils.translation import activate, gettext_lazy as _
from .local_data import LocalDataContentWiki
from django.conf import settings

from django.utils.functional import Promise
from django.utils.encoding import force_str
from django.core.serializers.json import DjangoJSONEncoder


## This API will work like that : 
# class UserQueue(models.Model):
#     username = models.CharField(max_length=255)
#     email = models.EmailField()
#     password = models.CharField(max_length=255)
#     is_validated = models.BooleanField(default=False)
#     created_at = models.DateTimeField(auto_now_add=True)
# - In order to create a UserQueue, the user need to send a get request (need to secure this views because it send data to a database)
# - Then the owner of the app receive a notification on discord with the url created in the previous step
# - The notification will be send with an existing function send_webhook(msg:Any)
# - When i click on the url, it will check wheter or not i'm logged in as a django superuser
# - if yes then it will add the user to the django User model if not i will be redirected to the admin panel login (which i changed to /luhcaran/ instead of /admin/)
# - after this, the user will need to send a GET request to another views that will redirect the user to the menu of the website at / and in the backend will send a notification with the request, username, password (hashed), token
# - Then once i've got the token, i will search in the admin pannel the user and add it the token in order to get POST access on the API

@loadContent(db_maintenance=True, editor_login=True)
def data(request):
    user_credential = getCredentialForNonLoginRequired(request).get('user_credential')
    if checkContributor(user_credential,request):
        status = request.session['status']
        url_query = "?q="
        filter_query = str(request.build_absolute_uri()).split(url_query)
        try:
            with open("calculator/local_data.json", 'r', encoding="utf-8") as f:
                data = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError) as e:
            messages.error(request, _(f"Error: {e}"))
        query_list = filter_query[1].split('.') if len(filter_query) > 1 and filter_query[1] != "" else []
        if request.method == "GET":
            SidebarContent = LocalDataContentWiki['SidebarContent']
            for query in query_list:
                try:
                    data = data[query]
                    url_query += f"{query}."
                except (KeyError, TypeError) as e:
                    messages.error(request, _(f"Query Error :{e}"))
            if not isinstance(data, (int, str, list)):
                keys = list(data.keys()) if len(data) != 1 else data
                result = False
            else:
                keys = data
                result = True
            previous = "/data/?q=" + ".".join(query_list[:-1]) if query_list else "/data/"
            return render(request, "api/api.html", {"keys":keys,"sidebarContent":SidebarContent,"header_msg":_("Website Data"),"url_query":url_query,"result":result,"previous":previous,"status":status})
        elif request.method == "POST":
            if status == "authorized":
                response_data = request.session['response_data']
                old_value = data
                for query in query_list:
                    old_value = old_value[query]
                if isinstance(old_value, (int, str, list)):
                    avatar_url = f"https://cdn.discordapp.com/avatars/{response_data.get('id','0')}/{response_data.get('avatar','a')}"
                    new_value = request.POST.get('new_value',None)
                    str_query_list = " -> ".join([i for i in query_list])
                    type_old_value = type(old_value)
                    try:
                        type_old_value(new_value)
                    except TypeError as e:
                        messages.error(request, _(f"The type of the old value must be the same for the new value {e}"))
                        return HttpResponseRedirect(request.build_absolute_uri())
                    send_embed(f"{response_data.get('username','a')}","__API Update__",
                        f"Change Author : <@{response_data.get('id','a')}> ({response_data.get('locale','a')})",
                        f"{str_query_list}",f"```diff\n- {old_value}\n+ {new_value}```","A200FF",request,True,avatar_url=avatar_url)
                    data_temp = data
                    for key in query_list[:-1]:
                        data_temp = data_temp[key]
                    data_temp[query_list[-1]] = new_value
                    with open('calculator/local_data.json', 'w', encoding="utf-8") as file:
                        json.dump(data, file, indent=4)
            return HttpResponseRedirect(request.build_absolute_uri())
    else:
        request.session['error_message'] = f"You're not allowed to access this page" # raise TypeError(f'Object of type {o.__class__.__name__} ' TypeError: Object of type __proxy__ is not JSON serializable
        return HttpResponseRedirect('/')


class CalculatorAPI(APIView):

    def get(self, request):
        filter_query = request.query_params.get("q")
        try:
            with open("calculator/local_data.json", 'r', encoding="utf-8") as f:
                data = json.load(f)
        except FileNotFoundError:
            return Response({"error": "File not found."}, status=status.HTTP_404_NOT_FOUND)
        except json.JSONDecodeError:
            return Response({"error": "Invalid JSON."}, status=status.HTTP_400_BAD_REQUEST)
        query_list = filter_query.split('.') if filter_query else []
        for query in query_list:
            try:
                data = data[query]
            except (KeyError, TypeError):
                return Response({"error": "Invalid query parameter."}, status=status.HTTP_400_BAD_REQUEST)
        return Response(data)


@loadContent(db_maintenance=True, login_required=True)
def create_user_queue(request):
    SidebarContent = LocalDataContentWiki['SidebarContent']
    if request.method == "POST":
        form = UserQueueForm(request.POST)
        if form.is_valid():
            user_credential = request.session['user_credential']
            user_queue = form.save(commit=False)
            user_queue.save()
            url = request.build_absolute_uri(reverse('validate_user_queue', kwargs={'pk': user_queue.pk}))
            messages.success(request,_("An Admin have been warned and will take care of you demand"))
            send_webhook(f'A new user queue was created. Click here to validate: {url}\n{user_credential}')
        else:
            messages.error(request,str(form.errors.as_text))
        return HttpResponseRedirect('/')
    else:
        form = UserQueueForm()
    return render(request, 'base/create_user_queue.html', {'form': form,"sidebarContent":SidebarContent})

@loadContent(db_maintenance=True, login_required=True)
def validate_user_queue(request, pk):
    if request.user.is_superuser:
        try:
            user_queue = UserQueue.objects.get(pk=pk)
        except UserQueue.DoesNotExist:
            messages.error(request,_(f'The user with {pk} as Primary Key doesn\'t exist'))
            return HttpResponseRedirect('/')
        user = User.objects.create_user(user_queue.username, user_queue.email, user_queue.password)
        send_webhook(f"{user_queue} Deleted Log :\nUsername : {user_queue.username} | Email : {user_queue.email}")
        user_queue.delete()
        token = Token.objects.create(user=user)
        send_webhook(f'The user "{user.username}" was validated and added to the Django User model. Token: {token.key}')
        messages.info(request,_(f'The user "{user.username}" was validated and added to the Django User model. Token: {token.key}'))
        return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/luhcaran/login/?next=' + request.build_absolute_uri())

class WikiAPI(APIView):

    def get(self, request):
        filter_query = request.query_params.get("q")
        lang = request.query_params.get("lang")
        if lang in dict(settings.LANGUAGES).keys():
            activate(lang)
        else:
            activate("en")
        try:
            parseDictToJson = json.dumps(LocalDataContentWiki, cls=LazyEncoder)
            data = json.loads(parseDictToJson)
        except FileNotFoundError:
            return Response({"error": "File not found."}, status=status.HTTP_404_NOT_FOUND)
        except json.JSONDecodeError:
            return Response({"error": "Invalid JSON."}, status=status.HTTP_400_BAD_REQUEST)
        query_list = filter_query.split('.') if filter_query else []
        for query in query_list:
            try:
                data = data[query]
            except (KeyError, TypeError):
                return Response({"error": "Invalid query parameter."}, status=status.HTTP_400_BAD_REQUEST)
        return Response(data)


# https://stackoverflow.com/questions/19734724/django-is-not-json-serializable-when-using-ugettext-lazy
class LazyEncoder(DjangoJSONEncoder):
    def default(self, obj):
        if isinstance(obj, Promise):
            return force_str(obj)
        return super(LazyEncoder, self).default(obj)
