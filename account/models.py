from django.db import models
from django.contrib.auth.models import User 

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete = models.CASCADE, null = False, 
    blank= True,related_name='profile')
    img = models.ImageField(upload_to='images'
    ,default='/Users/mac/django_app/bookmark/media/user_image.png')
    date_of_birth = models.DateField(blank=True , null= True)

    def __str__(self):
        return f'Profile of user {self.user.username}'