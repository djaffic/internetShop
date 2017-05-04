from django.shortcuts import render
from .forms import SubscriberForm


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
