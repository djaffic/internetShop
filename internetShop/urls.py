from django.conf.urls import url
from django.contrib import admin
from mainApp.views import landing, home

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^landing/$', landing),
    url(r'^$', home),
]
