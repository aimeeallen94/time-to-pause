from django.shortcuts import render
from django.contrib import messages
from .models import About
from .forms import ClassBookingRequestForm

# Create your views here.


def about_me(request):

    if request.method == 'POST':
        class_booking_request_form =ClassBookingRequestForm(data=request.POST)
        if class_booking_request_form.is_valid():
            class_booking_request_form.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Your interest has been regiestered! We will be in contact soon with available dates.'
            )
            
    about = About.objects.all().order_by('-date_created').first()
    class_booking_request_form = ClassBookingRequestForm()


    return render(
        request, 
        "about.html", 
        {
            "about":about,
            "class_booking_request_form":class_booking_request_form
            },)
            