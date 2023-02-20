from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('calculator.urls')),
]

handler404 = 'calculator.views_wiki.handler404'
handler500 = 'calculator.views_wiki.handler500'