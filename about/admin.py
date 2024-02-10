from django.contrib import admin
from .models import About, ClassBookingRequest
from django_summernote.admin import SummernoteModelAdmin


@admin.register(About)
class AboutAdmin(SummernoteModelAdmin):
    """
    This class registers the about sections and lays
    out the fields for the about sections to be
    completed by the admin which are three
    summernote fields to be completed.
    """

    summernote_fields = ('my_story', 'favourite_quote', 'why_i_started',)


@admin.register(ClassBookingRequest)
class ClassBookingRequestAdmin(admin.ModelAdmin):
    """
    This class registers the form to be completed by
    visitors to the page who want to register
    their interest in attending a class and
    the fields that will be seen by the admin in
    the admin panel.
    """

    list_display = ('availability', 'read',)
