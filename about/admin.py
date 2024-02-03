from django.contrib import admin
from .models import About, ClassBookingRequest
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.


@admin.register(About)
class AboutAdmin(SummernoteModelAdmin):

    summernote_fields = ('my_story', 'favourite_quote', 'why_i_started',)

@admin.register(ClassBookingRequest)
class ClassBookingRequestAdmin(admin.ModelAdmin):

    list_display = ('availability', 'read',)
