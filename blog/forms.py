# 3rd Party Imports
from django import forms

# Internal
from . models import Comment


class CommentForm(forms.ModelForm):
    """
    A class for the comment field which
    will display on the view for the user.
    """
    class Meta:
        model = Comment
        fields = ('body',)
