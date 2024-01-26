from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.

class About(models.Model):
    name = models.CharField(max_length=200)
    favourite_quote = models.TextField()
    my_story = models.TextField()
    why_i_started = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return {self.name}