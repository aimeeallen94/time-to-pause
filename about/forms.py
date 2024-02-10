from .models import ClassBookingRequest
from django import forms


class ClassBookingRequestForm(forms.ModelForm):
    """
    Setting up the form to be filled in by users
    who wish to attend a mindfulness class
    """
    class Meta:
        model = ClassBookingRequest
        fields = ('name', 'email', 'availability')
