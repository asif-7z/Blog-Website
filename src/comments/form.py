from django import forms
from .models import CommentSection

class CommentModel(forms.ModelForm):
    class Meta:
        model = CommentSection
        fields = ['text','content_type','object_id']

        widgets = {
            'text': forms.Textarea(attrs={'id': 'exampleFormControlTextarea1','rows':"3",'class':'form-control','placeholder':'Comment',}),
            'content_type': forms.HiddenInput(),
            'object_id': forms.HiddenInput()
        }
# class CommentModel(forms.Form):
#     content_type = forms.CharField(widget=forms.HiddenInput)
#     object_id = forms.IntegerField(widget=forms.HiddenInput)
#     text = forms.CharField(widget=forms.Textarea)



