from django.db import models


class About(models.Model):
    """
    Setting up model for about sections with
    each fields that will be seen by the user
    as well as what is to be completed by the admin
    and what is auto-completed
    """
    name = models.CharField(max_length=200)
    favourite_quote = models.TextField(default='empty')
    my_story = models.TextField(default='empty')
    why_i_started = models.TextField(default='empty')
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class ClassBookingRequest(models.Model):
    """
    The class booking request sets up the model to be
    completed a user who would like to attend a
    mindfulness class as well as those fields
    that are auto completed
    """
    name = models.CharField(max_length=200)
    email = models.EmailField()
    availability = models.TextField()
    read = models.BooleanField(default=False)

    def __str__(self):
        return f"Class booking request from {self.name}"
