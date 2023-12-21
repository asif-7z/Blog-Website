from django import forms
from .models import LogIn,BlogPost2

# class CreateForm(forms.Form):
#     title2 = forms.CharField()
#     slug = forms.SlugField()
#     content2 = forms.CharField()
class CreateForm(forms.ModelForm):
    class Meta:
        model = BlogPost2
        fields = ['title2','image','slug','content2','publish_date']

    def clean_title2(self,*args,**kwargs):
        instance = self.instance
        print(instance)
        title2 = self.cleaned_data.get('title2')
        qs = BlogPost2.objects.filter(title2=title2)
       # print(qs)
        if instance is not None:
            qs = qs.exclude(pk=instance.pk)
        if qs.exists():
            raise forms.ValidationError("this title alredy exists")
        return title2

class LoginForm(forms.ModelForm):
    class Meta:
        model = LogIn
        fields = ['user_name','email','content']
    
    def clean_email(self,*args,**kwargs):
        email = self.cleaned_data.get('email')
        print(email)
        if email.endswith(".edu"):
            raise forms.ValidationError("this is not valid email which ends with .edu")
        return email