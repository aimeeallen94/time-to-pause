from .models import Comment
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)
        def __init__(self):
            self.helper.add_input(Submit('submit', 'Post Comment'))