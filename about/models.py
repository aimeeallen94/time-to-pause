from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.

class About(models.Model):
    name = models.CharField(unique=True)
    favourite_quote = models.TextField()
    about_me = models.TextField()
    why_i_started = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)