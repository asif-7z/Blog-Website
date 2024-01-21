from rest_framework.serializers import ModelSerializer,HyperlinkedIdentityField,SerializerMethodField

from blog2.models import BlogPost2



post_detail_url = HyperlinkedIdentityField(view_name='blogs-api:detail',
                               lookup_field = 'slug')

post_delete_url = HyperlinkedIdentityField(view_name='blogs-api:delete',lookup_field='slug')

class BlogPost2CreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = BlogPost2
        fields = ['id','slug','title2','content2']

class BlogPost2Serializer(ModelSerializer):
    url = post_detail_url
    delete_url = post_delete_url
    # image = SerializerMethodField()
    user = SerializerMethodField()
    image = SerializerMethodField()
    # html = SerializerMethodField()
    class Meta:
        model = BlogPost2
        fields = [
                'url',
                'user',
                'id',
                'title2',
                'delete_url',
                'image',
                # 'html'

                ]
        
    def get_user(self,obj):
        return obj.user.username
    def get_image(self,obj):
        return obj.image.url
    # def get_html(self,obj):
    #     return obj.get_markdown
        
        


        
class BlogPost2DetailSerializer(ModelSerializer):
    
    class Meta:
        
        model = BlogPost2
        fields = [
            'user','id','title2','slug','content2',
        ]
