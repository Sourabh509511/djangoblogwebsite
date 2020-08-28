from django.db import models

# Create your models here.
class Contact(models.Model):
    Id=models.AutoField(primary_key=True)
    Name=models.CharField(max_length=60)
    Email=models.CharField(max_length=100)
    Phone=models.CharField(max_length=15)
    Content=models.TextField(max_length=6000)
    Timestamp=models.DateTimeField(auto_now_add=True,blank=True)
    def __str__(self):
        return "Message from"+" "+self.Name+"-"+self.Content[0:12]+"..."