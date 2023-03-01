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
    


class Contact(models.Model):
    user_from = models.ForeignKey(User, related_name='rel_from_set',on_delete=models.CASCADE)
    user_to = models.ForeignKey(User, related_name='rel_to_set', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True,db_index=True)

    class Meta:
        ordering = ('-created') 
    def __str__(self):
        return f'{self.user_from} follows {self.user_to}'
user_model = User()
user_model.add_to_class('following',models.ManyToManyField('self',
                                                           through=Contact,
                                                           symmetrical=False))
