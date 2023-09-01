from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns
from django.views.generic.base import TemplateView

urlpatterns = [
    path('luhcaran/', admin.site.urls),
    path('robots.txt', TemplateView.as_view(template_name="robots.txt", content_type='text/plain')),
    path('', include('calculator.urls')), # keep that to still allow url without /{{lang.code}}/
]

urlpatterns += i18n_patterns (
    path('', include('calculator.urls')),
)

handler404 = 'calculator.views_wiki.handler404'
handler500 = 'calculator.views_wiki.handler500'