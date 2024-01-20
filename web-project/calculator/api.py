import json
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import messages
from django.urls import reverse
from django.utils.translation import activate, gettext_lazy as _
from django.conf import settings
from django.utils.functional import Promise
from django.utils.encoding import force_str
from django.core.serializers.json import DjangoJSONEncoder

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token

from .function import send_webhook, send_embed, checkContributor, loadContent
from .data.wiki_data import LocalDataContentWiki

from rest_framework.decorators import authentication_classes, permission_classes, api_view


@api_view(['GET'])
def get(request):
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
