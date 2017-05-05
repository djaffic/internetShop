from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from mainApp.views import landing, home, about, contact
from product.views import product
from order.views import basket_adding

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^landing/$', landing),
    url(r'^$', home, name='home'),
    url(r'^about/$', about, name='about'),
    url(r'^contact/$', contact, name='contact'),
    url(r'^basket_adding/$', basket_adding, name='basket_adding'),
    url(r'^product/(?P<product_id>\w+)/$', product, name='product')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)\
