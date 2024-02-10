from .models import Comment
from django import forms


class CommentForm(forms.ModelForm):
    """
    This is the form for users to be able
    to leave comments including what fields will
    be there.
    """
    class Meta:
        model = Comment
        fields = ('content',)

        def __init__(self):
            self.helper.add_input(Submit('submit', 'Post Comment'))
