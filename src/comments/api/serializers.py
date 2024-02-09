from rest_framework.serializers import ModelSerializer,SerializerMethodField,HyperlinkedIdentityField,ValidationError
from comments.models import CommentSection
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model

User = get_user_model()



def create_comment_serializer(model_type='blog2',slug=None,parent_id=None,user=None):
    class CommentCreateSerializer(ModelSerializer):
        class Meta:
            model = CommentSection
            fields = ['id','parent','text','time_stamp']
        
        def __init__(self,*args,**kwargs):
            self.model_type = model_type
            self.slug = slug
            self.parent_obj = None
            if parent_id:
                qs = CommentSection.objects.filter(id = parent_id)
                if qs.exists() or qs.count() == 1:
                    
                    self.parent_obj = qs.first()
            return super(CommentCreateSerializer,self).__init__(*args,**kwargs)

        def validate(self,data):
            model_type = self.model_type
            model_qs = ContentType.objects.filter(model=model_type)
            if not model_qs.exists() or model_qs.count() != 1:
                raise ValidationError("model does not exist")
            model_obj = model_qs.first().model_class()
            obj_qs = model_obj.objects.filter(slug = self.slug)
            if not obj_qs.exists() or obj_qs.count() !=1:
                raise ValidationError("slug  does not exist for this content type")
            return data
        
        def create(self,validated_data):
            text = validated_data.get('text')
            if user:
                main_user = user
            else:
                main_user = User.objects.all().first()
            model_type = self.model_type
            slug = self.slug
            parent_obj = self.parent_obj
            comment = CommentSection.objects.create_by_model(model_type,slug,text,main_user,parent_obj=parent_obj)

            return comment
    return CommentCreateSerializer



class CommentSerializer(ModelSerializer):
    user = SerializerMethodField()
    url = HyperlinkedIdentityField(view_name='comment-apis:detail',lookup_field='id')
    replies_count = SerializerMethodField()
    class Meta:
        
        model = CommentSection
        fields = [
            'url',
            'id',
            'user',
            'text',
            'replies_count',
                 ]
    def get_replies_count(self,obj):
        if obj.is_parent:
            return obj.children().count()
        return 0

    def get_user(self,obj):
        return obj.user.username  
    
class CommentListSerializer(ModelSerializer):
    user = SerializerMethodField()
    content_obj_url  = SerializerMethodField()
    url = HyperlinkedIdentityField(view_name='comment-apis:detail',lookup_field='id')
    replies_count = SerializerMethodField()
    class Meta:
        
        model = CommentSection
        fields = [
            'url',
            'id',
            'user',
            'text',
            'replies_count',
            'content_obj_url',
                 ]
    def get_replies_count(self,obj):
        if obj.is_parent:
            return obj.children().count()
        return 0

    def get_user(self,obj):
        return obj.user.username  
    def get_content_obj_url(self,obj):
        return obj.content_object.get_api_url()
   
    
class ChildCommentSerializer(ModelSerializer):
    class Meta:
        model = CommentSection
        fields = ['id','text','time_stamp']



class CommentsDetailSerializer(ModelSerializer):
    user = SerializerMethodField()
    replies_count = SerializerMethodField()
    replies = SerializerMethodField()
    class Meta:
        model = CommentSection
        fields = [
            'id',
            'user',
            'content_type',
            'object_id',
            'text',
            'time_stamp',
            'replies_count',
            'replies',


        ]
        read_only_fields = [
            'id',
            'content_type',
            'object_id',
            'replies_count',
            'replies',
        ]

    def get_replies(self,obj):
        if obj.is_parent:
            return ChildCommentSerializer(obj.children(),many=True).data
        return None
    
    def get_replies_count(self,obj):
        if obj.is_parent:
            return obj.children().count()
        return 0
   
    def get_user(self,obj):
        return obj.user.username  
    

