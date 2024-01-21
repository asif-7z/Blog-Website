from django import forms
from .models import CommentSection

class CommentModel(forms.ModelForm):
    class Meta:
        model = CommentSection
        fields = ['text']

        widgets = {
            'text': forms.Textarea(attrs={'id': 'exampleFormControlTextarea1','rows':"3",'class':'form-control','placeholder':'Comment'}),
        }




