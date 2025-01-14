from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class Login_view(AbstractUser):
    is_blogger = models.BooleanField(default=False)
    is_blogveiwer = models.BooleanField(default=False)

class Blogger(models.Model):
    user=models.ForeignKey(Login_view,on_delete=models.CASCADE,related_name='blogger')
    email=models.EmailField()
    status1=models.BooleanField(default=0)
class Blogveiwer(models.Model):
    user=models.ForeignKey(Login_view,on_delete=models.CASCADE,related_name='blogveiwer')
    email=models.EmailField()
class Addblog(models.Model):
    user = models.ForeignKey(Blogger, on_delete=models.CASCADE, related_name='addblog')
    blog_title = models.CharField(max_length=50)
    blog_content = models.TextField()
    author_image = models.FileField(upload_to='documents/')
    date = models.DateField()

class Postblog(models.Model):
    user = models.ForeignKey(Blogger, on_delete=models.CASCADE, related_name='Postblog')
    blog_title = models.CharField(max_length=50)
    blog_content = models.TextField()
    author_image = models.FileField(upload_to='documents/')
    date = models.DateField()
