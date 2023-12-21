from django import forms
from .models import CommentSection

class CommentModel(forms.ModelForm):
    class Meta:
        model = CommentSection
        fields = ['text','username','email','title']




