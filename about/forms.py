from .models import ClassBookingRequest
from django import forms

class ClassBookingRequestForm(forms.ModelForm):
    class Meta:
        model = ClassBookingRequest
        fields = ('name', 'email', 'availability')
#        def __init__(self):
#            self.helper.add_input(Submit('submit', 'Register Interest'))
