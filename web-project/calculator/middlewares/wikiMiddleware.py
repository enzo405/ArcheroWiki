from calculator.models import ServerManagement
from app.settings import STATIC_VERSION

class CustomHeaderMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        try:
            server_instance = ServerManagement.objects.get(pk=1)
            archeroVersion = server_instance.archeroVersion
            archeroIconLink = server_instance.archeroIconLink
        except Exception:
            archeroVersion = "Archero"
            archeroIconLink = "https://play-lh.googleusercontent.com/cMYvvKCxCnhIg0Gc4pbI0CgCqNw9l5lAFUAmAv4aXkK1nynqwiye8P8NxArULW9eMQ"

        # Add data to the request context
        request.archero_version = archeroVersion
        request.archero_icon_link = archeroIconLink
        request.static_version = STATIC_VERSION

        response = self.get_response(request)
        return response
