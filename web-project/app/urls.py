from django.contrib import admin
from django.conf import settings
from django.urls import path, include, re_path
from django.conf.urls.i18n import i18n_patterns
from django.views.generic.base import TemplateView

urlpatterns = [
    path('', include('calculator.urls')), # Keep that to still allow url without /{{lang.code}}/
    path('luhcaran/', admin.site.urls),
    path('robots.txt', TemplateView.as_view(template_name="robots.txt", content_type='text/plain')),
]

# Add language prefix to all urls
urlpatterns += i18n_patterns (
    path('', include('calculator.urls')),
)

# Add rosetta urls
if 'rosetta' in settings.INSTALLED_APPS:
    urlpatterns += [
        re_path(r'^deth/', include('rosetta.urls'))
    ]

# Add custom error handlers
handler404 = 'calculator.views_wiki.handler404'
handler500 = 'calculator.views_wiki.handler500'