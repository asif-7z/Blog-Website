from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

# Create your models here.
class CommentSection(models.Model):
    user = models.ForeignKey(User,default=1,null=True,on_delete=models.SET_NULL)
    text = models.TextField(null=False,max_length=200)
    username = models.CharField(max_length=20,null=False)
    email = models.EmailField(null=False)
    time_stamp = models.DateTimeField(auto_now=True,editable=True)
    title = models.CharField(null=True,max_length=20)



