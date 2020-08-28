from django.shortcuts import render,HttpResponse,redirect
from .models import Blog,Comment
from django.contrib import messages



# Create your views here.
def home(request):
    posts=Blog.objects.all()
    content={'allposts':posts}
    return render(request,'blog/index.html',content)


def blogger(request,slug):
    post=Blog.objects.filter(Blog_slug=slug).first()
    allcomments=Comment.objects.filter(post=post,parent=None)
    allreplies=Comment.objects.filter(post=post).exclude(parent=None)
    repdict={}
    for reply in allreplies:
        if reply.parent.c_id not in repdict.keys():
            repdict[reply.parent.c_id]=[reply]
        else:
            repdict[reply.parent.c_id].append(reply)
    content={'fullpost':post,'comments':allcomments,'allreply':repdict}
    # print(f'content is : {content}')
    # print(f'repliy dic is : {repdict}')
    # for key,value in repdict:
    #     print(f'all reply is : {key},{value}')
    return render(request,'blog/blogger.html',content)

def postcomment(request):
    if request.method=="POST":
        content=request.POST.get('comment')
        post_id=request.POST.get('postid')
        comment_id=request.POST.get('commentid')
        # print(content,post_id)
        User=request.user
        post=Blog.objects.get(Bid=post_id)
        if comment_id =="":
            comment=Comment.objects.create(c_text=content,post=post,user=User)
            messages.success(request,"Comment added successfully")
        else:
            parentsno=Comment.objects.get(c_id=comment_id)
            comment=Comment.objects.create(c_text=content,post=post,user=User,parent=parentsno)
            messages.success(request,"Reply added successfully")
        comment.save()
        return redirect(f"blogger/{post.Blog_slug}")