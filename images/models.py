from django.urls import reverse
from django.utils.text import slugify
from django.db import models

# Create your models here.
from django.conf import Settings
from django.contrib.auth.models import User


class Images(models.Model):
    user  = models.ForeignKey(User,on_delete=models.CASCADE , null = False, related_name='images_created')
    title = models.CharField(max_length=150)
    slug = models.SlugField(max_length=200, blank=True)
    url = models.URLField()
    image = models.ImageField(upload_to='images')
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    user_likes = models.ManyToManyField(User ,blank=True ,related_name='images_liked')


    def __str__(self):
        return self.title
    
    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    def get_absolute_url(self):
        return reverse('images:detail' , args=[self.id])