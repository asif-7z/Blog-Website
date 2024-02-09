from django.db import models
from django.conf import settings
from blog2.models import BlogPost2
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.urls import reverse



User = settings.AUTH_USER_MODEL

# Create your models here.

class CommentSectionManager(models.Manager):

    def all(self):
        qs = super(CommentSectionManager,self).filter(parent=None)
        return qs
    
    def filter_blog_obj(self,blog_obj):
        content_type  = ContentType.objects.get_for_model(blog_obj.__class__)
        obj_id = blog_obj.id
        qs = super(CommentSectionManager,self).filter(content_type=content_type,object_id=obj_id).filter(parent=None)
        return qs
    
    def create_by_model(self,model_type,slug,text,user,parent_obj=None):
        model_qs = ContentType.objects.filter(model=model_type)
        if model_qs.exists() or model_qs.count() == 1:
            SomeModel  = model_qs.first().model_class()
            obj_qs = SomeModel.objects.filter(slug=slug)
            if obj_qs.exists() or obj_qs.count()==1:
                instance = self.model()
                instance.text = text
                instance.user = user
                instance.content_type = model_qs.first()
                instance.object_id = obj_qs.first().id
                if parent_obj:
                    instance.parent = parent_obj
                instance.save()
                return instance
        return None





class CommentSection(models.Model):
    user = models.ForeignKey(User,default=1,null=True,on_delete=models.SET_NULL)
    # title = models.ForeignKey(BlogPost2,null=True,on_delete=models.SET_NULL)
    
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE,null=True)
    object_id = models.PositiveIntegerField(null=True)
    content_object = GenericForeignKey("content_type", "object_id")

    parent = models.ForeignKey("self",null=True,blank=True,on_delete=models.CASCADE)
    text = models.TextField(null=False,max_length=200)
    time_stamp = models.DateTimeField(auto_now_add=True)

    objects = CommentSectionManager()

    class Meta:
        ordering = ['-time_stamp']
                              
    def __unicode__(self):
        return str(self.user.username)
    def __str__(self):
        i = self.user.username + " "+str(self.parent_id)
        return i
    
    def get_api_url(self):
        return reverse('blogs-api:detail',kwargs={"slug":self.slug})
    
    def children(self):
        return CommentSection.objects.filter(parent=self)
       
    def is_parent(self):
        if self.parent is not None:
            return False
        return True
        
        
        


