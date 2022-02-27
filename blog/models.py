from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

# Create your models here.
def image_upload(instance,filename):
    txt='imgpost_'
    imagename,extension=filename.split('.')
    return "post/%s%s.%s"%(txt,instance.id,extension)


class Post(models.Model):

    title =  models.CharField(max_length=200, unique=True)
    slug=models.SlugField(blank=True,null=True)
    author = models.ForeignKey(User,related_name='post_owner',on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    image=models.ImageField(upload_to=image_upload)
    content = models.TextField()


    class Meta:
        ordering = ['-created_on']

    def save(self,*args,**kwargs):
        self.slug=slugify(self.title)
        super(Post,self).save(*args, **kwargs)

    def __str__(self) :
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    username = models.CharField(max_length=25)
    email = models.EmailField()
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['date_added']

