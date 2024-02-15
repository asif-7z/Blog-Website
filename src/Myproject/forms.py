from django import forms

class ContactForm(forms.Form):
    user_name = forms.CharField()
    email = forms.EmailField()
    content = forms.CharField()
