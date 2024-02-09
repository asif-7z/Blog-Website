from django.shortcuts import render,redirect
from .models import CommentSection
from .form import CommentModel
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from blog2.models import BlogPost2
from django.contrib.contenttypes.models import ContentType

# Create your views here.

@login_required
@staff_member_required
def comment_thread(request,id):
    template_name = "comment/comments.html"
    obj = CommentSection.objects.get(id=id)
    initial_data = {"content_type":obj.content_type,"object_id":obj.object_id}
    form = CommentModel(request.POST or None,initial=initial_data)
    if form.is_valid():
        c_type = form.cleaned_data.get('content_type')
        content_type_model = ContentType.objects.get_for_model(obj.__class__)
        o_id = form.cleaned_data.get('object_id')
        text = form.cleaned_data.get('text')
        parent_id = request.POST.get('parent_id')
        parent_obj = None
        try:
            parent_id = int(request.POST.get('parent_id'))
        except:
            parent_id = None
        if parent_id:
            parent_qs= CommentSection.objects.filter(id =parent_id)
            if parent_qs:
                parent_obj = parent_qs.first()
        if request.user.is_authenticated:
            print("hrllo")
            new_obj,obj1 = CommentSection.objects.get_or_create(user=request.user,
                                                                content_type=content_type_model,
                                                                object_id = o_id,
                                                                parent=parent_obj,
                                                                text= text)
            form = CommentModel()
            return redirect('.')
        else:
            print("not found")



    context = {"list": obj ,"comment":form}
    return render(request,template_name,context)


def delete_comment(request,id):
    temp = "comment/delete_comment.html"
    obj = CommentSection.objects.get(id=id)
    parent_id = obj.parent.id
    # obj2 = CommentSection.objects.get(id=26)

    # if obj2.is_parent:
    #     print("yes")
    # else:
    #     ("no")

    if request.method == "POST":
        obj.delete()
        return redirect(f'/comments/{parent_id}/comment_thread')
    context = {"object":obj}
    return render(request,temp,context)

