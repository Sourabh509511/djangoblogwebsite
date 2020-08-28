from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Blog(models.Model):
    Bid=models.AutoField(primary_key=True)
    Author_name=models.CharField(max_length=50)
    Blog_title=models.CharField(max_length=100)
    Blog_slug=models.CharField(max_length=150)
    Blog_category=models.CharField(max_length=150)
    Blog_content=models.TextField(max_length=5000)
    Blog_time=models.DateTimeField()
    Blog_image=models.ImageField(upload_to='blog/Images',default="")

    def __str__(self):
        return self.Author_name+"-"+self.Blog_content[0:15]+"..."


class Comment(models.Model):
    c_id=models.AutoField(primary_key=True)
    c_text=models.TextField(max_length=500)
    post=models.ForeignKey(Blog, on_delete=models.CASCADE)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    parent=models.ForeignKey('self',on_delete=models.CASCADE,null=True)
    timestamp=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.c_text[:14]+"... by "+self.user.username