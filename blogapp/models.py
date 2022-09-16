import email
from numbers import Number
from xml.dom.minidom import Attr
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.



class Post(models.Model):
    title = models.CharField(max_length=200, unique=False)
    slug = models.SlugField(max_length=200, unique=False)
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blogs')
    updated_on = models.DateTimeField(auto_now= True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(default=0)
    blog_image = models.ImageField(upload_to='blog_images', blank=True, null='True')

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title
    
    
    
class CommentModel(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField(max_length=200)
    comment_date = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return 'Comment by {} on {} massege: {} '.format(self.username, self.comment_date,  self.comment)
    
    
class SubComment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField(max_length=200)
    comment_date = models.DateTimeField(default=timezone.now)
    subcom = models.ForeignKey(CommentModel, on_delete=models.CASCADE)
    
    # def __str__(self):
    #     return 'Comment by {} on {} massege: {} '.format(self.username, self.comment_date,  self.comment)