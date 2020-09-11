from django.shortcuts import render,HttpResponse,redirect
from .models import Contact
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
# from blogger.models import Blog
from django.db.models import Q
from blogger.documents import blogDocument
from django.views import View




# Create your views here.
class welcome(View):
    def get(self,request):
        return render(request,'home/index.html')


class contact(View):
    def get(self,request):
        return render(request,'home/contact.html')
    def post(self,request):
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        msg=request.POST.get('message')
        if len(name) < 2 or len(email) < 6 or (len(phone) > 13 or len(phone)< 9) or len(msg) < 10:
            messages.error(request,"Please fill the form correctly!!!")
            messages.error(request,"Length of name should be grater then 2 characters!!!")
            messages.error(request,"Length of email should be grater then 6 characters!!!")
            messages.error(request,"Length of phone should be grater then 9 characters and smaller then 9 character!!!")
            messages.error(request,"Length of message should be grater then 10 characters!!!")
        else:
            contact=Contact.objects.create(Name=name,Email=email,Phone=phone,Content=msg)
            contact.save()
            messages.success(request,"Form submitted successfully...")
        return render(request,'home/contact.html')

class about(View):
    def get(self,request):
        return render(request,'home/about.html')


class search(View):
    def get(self,request):
        name=request.GET.get('search')
        if (len(name)) < 50:
                posts=blogDocument.search().query({"multi_match": {"query": name, "fields": ["Blog_content", "Blog_title","Blog_slug","Blog_category","Author_name"]}})
                print(posts)
                # posts=Blog.objects.none()
                # posts=Blog.objects.filter(Q(Blog_title__icontains=name)|Q(Blog_content__icontains=name)|Q(Author_name__icontains=name)|Q(Blog_category__icontains=name))
                # posts_content=Blog.objects.filter(Blog_content__icontains=name)
                # allpost=posts_title.Union(posts_content)
                # posts_a_name=Blog.objects.filter(Author_name__icontains=name)
                # allpost=allpost.Union(posts_a_name)
                # posts_cat=Blog.objects.filter(Blog_category__icontains=name)
                # allpost=allpost.Union(posts_cat)
                if posts:
                    param={'allposts':posts}
                    return render(request,'home/search.html',param)
                else:
                    messages.error(request,"No results found!!!")
                messages.error(request,"No articles have given given KEYWORD in their heading.")
                return render(request,'home/search.html')
        else:
            messages.error(request,"Too long query... Try small keyword")
            return render(request,'home/search.html')


class authentication(View):
    def get(self,request):
        return render(request,'home/index.html')

    def post(self,request):
        username=request.POST.get('Username')
        name=request.POST.get('name')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1==pass2:
            user=User.objects.create_user(username,email,pass1)
            user.name=name
            user.save()
            messages.success(request,"Your account has been successfully created")
            return redirect('index')

        if len(username)<10:
            messages.error(request,"Username is too small...  It must be greater then 10 characters")
            return redirect('index')

        if not username.isalnum():
            messages.error(request,"Username should only contain letters and digit")
            return redirect('index')
        else:
            messages.error(request,"Password must be same in both fields")
            return redirect('index')

class loginView(View):
    def post(self,request):
        loginusername=request.POST.get('username')
        loginpassword=request.POST.get('password')
        print(loginusername,loginpassword)
        user= authenticate(username=loginusername, password=loginpassword)
        print(user)
        if user is not None:
            login(request,user)
            messages.success(request,f"Successfully logged In as {user}")
            return redirect("index")
        else:
            messages.error(request,"Invalid Credentials!!!")
            return redirect("index")

class logoutView(View):
    def get(self,request):
        logout(request)
        messages.success(request,"Successfully logged out")
        return redirect("/")

# from django.views import View

# class LoginClassView(View):
#     def get(self,request):
#         return redirect("index")
    
#     def fun(self,request,data):
#         return request.POST.get(data)
    
#     def post(self,request):
#         loginusername=self.fun(request,'username')
#         loginpassword=self.fun(request,'password')
#         print(loginusername,loginpassword)
#         user= authenticate(username=loginusername, password=loginpassword)
#         print(user)
#         if user is not None:
#             login(request,user)
#             messages.success(request,"Successfully logged In")
#             return redirect("index")
#         else:
#             messages.error(request,"Invalid Credentials!!!")

#         return HttpResponse("login")