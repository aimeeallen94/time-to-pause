from django.shortcuts import render
from django.contrib import messages
from .models import About
from .forms import ClassBookingRequestForm


def about_me(request):
    """
    This is the view for the form that is completed
    by users who are intereted in attending a mindfulness
    class and also the response users will get when they
    complete the form and how it will be saved laid out in the
    admin panel also. This also returns users to the
    about page once they have completed the form.
    """

    if request.method == 'POST':
        class_booking_request_form = ClassBookingRequestForm(data=request.POST)
        if class_booking_request_form.is_valid():
            class_booking_request_form.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Your interest has been registered! We will be in contact soon with available dates.'
            )

    about = About.objects.all().order_by('-date_created').first()
    class_booking_request_form = ClassBookingRequestForm()

    return render(
        request,
        "about.html",
        {
            "about": about,
            "class_booking_request_form": class_booking_request_form
            },)
