from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import About
# Create your views here.


def about(request):
    about = get_object_or_404(queryset)
    return render(request, "about/about.html", {"about":about},)