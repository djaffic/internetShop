from django.shortcuts import render
from .forms import SubscriberForm
from product.models import ProductImage


# Create your views here.
def landing(request):
    name = "djaffic"
    current_day = "04.05.2017"
    form = SubscriberForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        print(request.POST)
        print(form.cleaned_data)

        data = form.cleaned_data
        print(data["name"])

        form = form.save()

    return render(request, 'mainApp/landing.html', locals())

def home(request):
    products_images = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True)
    products_images_phones = products_images.filter(product__category__id=1)
    products_images_laptops = products_images.filter(product__category__id=2)
    return render(request, 'mainApp/home.html', locals())

def about(request):
    return render(request, 'mainApp/about.html', locals())

def contact(request):
    return render(request, 'mainApp/contact.html', locals())
