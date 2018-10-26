# coding: utf-8
from django.conf.urls import url, include
from django.contrib import admin


urlpatterns = [
     url(r'^helloWorld/', include('helloWorld.urls')),
     url(r'^admin/', admin.site.urls),
]
