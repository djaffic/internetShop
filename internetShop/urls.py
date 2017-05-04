from django.conf.urls import url
from django.contrib import admin
from mainApp.views import landing

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^landing/$', landing),
]
