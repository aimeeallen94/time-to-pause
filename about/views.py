from django.shortcuts import render
from .models import About

# Create your views here.


def about_me(request):
    about = About.objects.all().order_by('-date_created').first()

    return render(request, "about.html", {"about":about},)