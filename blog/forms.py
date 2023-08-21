# 3rd Party Imports
from django import forms

# Internal
from . models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
