from django.db import models
# Create your models here.

class About(models.Model):
    name = models.CharField(max_length=200)
    favourite_quote = models.TextField(default='empty')
    my_story = models.TextField(default='empty')
    why_i_started = models.TextField(default='empty')
    date_created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

class ClassBookingRequest(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    availability = models.TextField()
    read = models.BooleanField(default=False)

    def __str__(self):
        return f"Class booking request from {self.name}"