from rest_framework.serializers import ModelSerializer,HyperlinkedIdentityField,SerializerMethodField

from blog2.models import BlogPost2
from comments.models import CommentSection
from comments.api.serializers import CommentsDetailSerializer






class BlogPost2CreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = BlogPost2
        fields = ['id','slug','title2','content2']

class BlogPost2Serializer(ModelSerializer):
    # image = SerializerMethodField()
    user = SerializerMethodField()
    
    # image = SerializerMethodField()
    # html = SerializerMethodField()
    url = HyperlinkedIdentityField(view_name='blogs-api:detail',
                               lookup_field = 'slug')
    delete_url = HyperlinkedIdentityField(view_name='blogs-api:delete',lookup_field='slug')

    class Meta:
        model = BlogPost2       
        fields = [
                'url',
                'user',
                'id',
                'title2',
                'delete_url',
                # 'image',
                # 'html'


                 ]
    
   


        
    def get_user(self,obj):
        return obj.user.username
    # def get_image(self,obj):
    #     return obj.image.url
    # def get_html(self,obj):
    #     return obj.get_markdown
        
        


        
class BlogPost2DetailSerializer(ModelSerializer):
    comment = SerializerMethodField()
    
    class Meta:
        
        model = BlogPost2
        fields = [
            'user','id','title2','slug','content2','comment',
        ]
    def get_comment(self,obj):
        obj1 = CommentSection.objects.filter_blog_obj(obj)
        comments = CommentsDetailSerializer(obj1,many=True).data
        return comments