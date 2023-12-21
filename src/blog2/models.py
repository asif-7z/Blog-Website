from django.db import models
from django.conf import settings
from django.db.models import Q
from django.utils import timezone

User = settings.AUTH_USER_MODEL

class BlogPost2QuerySet(models.QuerySet):
    def published(self):
        now = timezone.now()
        return self.filter(publish_date__lte=now)
    
    def search(self,query):
        lookup=Q(Q(title2__icontains=query)|
                 Q(content2__icontains=query)|
                 Q(slug__icontains=query)|
                 Q(user__username__icontains=query)
                 )
        return self.filter(lookup)

class BlogPostManager(models.Manager):
    def get_queryset(self):
        return BlogPost2QuerySet(self.model, using=self._db)
    
    def published(self):
        return self.get_queryset().published()
    
    def search(self, query=None):
        if query is None:
            return self.get_queryset().none()
        return self.get_queryset().published().search(query)





# Create your models here.
class BlogPost2(models.Model):
    user = models.ForeignKey(User,default=1,null=True,on_delete=models.SET_NULL)
    title2 = models.CharField(max_length=120)
    image = models.ImageField(upload_to='image/',blank=True,null=True)
    slug = models.SlugField(unique=True)
    content2 = models.TextField()
    publish_date = models.DateTimeField(auto_now=False,auto_now_add=False,null=True,blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    objects = BlogPostManager()

    class Meta:
         ordering = ['-publish_date','-updated','-timestamp']

    def get_absolute_url(self):
        return f"/blog2/{self.slug}"
    
    def get_title(self):
        return f"{self.title2}"
        
    
    def get_edit_url(self):
        # print(self.slug)
        return f"{self.get_absolute_url()}/update"
    
    def get_delete_url(self):
        return f"/blog2/{self.slug}/delete"

class LogIn(models.Model):
    user_name = models.CharField(max_length=120)
    email = models.EmailField(unique=True)
    content = models.TextField()
