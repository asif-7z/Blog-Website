from django.db import models
from django.conf import settings
from blog2.models import BlogPost2
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


User = settings.AUTH_USER_MODEL

# Create your models here.
class CommentSection(models.Model):
    user = models.ForeignKey(User,default=1,null=True,on_delete=models.SET_NULL)
    title = models.ForeignKey(BlogPost2,null=True,on_delete=models.SET_NULL)
    
    # content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    # object_id = models.PositiveIntegerField()
    # content_object = GenericForeignKey("content_type", "object_id")

    text = models.TextField(null=False,max_length=200)
    # time_stamp = models.DateTimeField(auto_now=True,editable=True)
                              
    def __unicode__(self):
        return str(self.user.username)
    def __str__(self):
        return self.user.username


