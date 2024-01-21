from rest_framework.serializers import ModelSerializer,SerializerMethodField,HyperlinkedIdentityField
from comments.models import CommentSection

class CommentSerializer(ModelSerializer):
    user = SerializerMethodField()
    title = SerializerMethodField()
    url = HyperlinkedIdentityField(view_name='comment-apis:detail',lookup_field='id')
    class Meta:
        
        model = CommentSection
        fields = [
            'url',
            'id',
            'user',
            'title',
            'text',


        ]
    def get_user(self,obj):
        return obj.user.username  
    def get_title(self,obj):
        if obj.title:
            return obj.title.slug
        return None
class CommentsDetailSerializer(ModelSerializer):
    slug = SerializerMethodField()
    user = SerializerMethodField()
    class Meta:
        model = CommentSection
        fields = [
            'id',
            'user',
            'slug',
            'text',
            'time_stamp',

        ]
    def get_slug(self,obj):
        if obj.title:
            return obj.title.slug
        return None
    def get_user(self,obj):
        return obj.user.username  