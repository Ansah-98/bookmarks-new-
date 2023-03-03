from django.db import models
from django.contrib.auth.models import User 
from django.contrib.auth import get_user_model
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete = models.CASCADE, null = False, 
    blank= True,related_name='profile')
    img = models.ImageField(upload_to='images'
    ,default='/Users/mac/django_app/bookmark/media/user_image.png')
    date_of_birth = models.DateField(blank=True , null= True)

    def __str__(self):
        return f'Profile of user {self.user.username}'

class Contact(models.Model):
    user_from = models.ForeignKey(User, related_name='rel_from_set',on_delete=models.CASCADE)
    user_to = models.ForeignKey(User, related_name='rel_to_set', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True,db_index=True)

    class Meta:
        ordering = ('-created',) 
    def __str__(self):
        return f'{self.user_from} follows {self.user_to}'
user_model = get_user_model()
user_model.add_to_class('following',models.ManyToManyField('self',
                                                           through=Contact,
                                                           related_name='followers',
                                                           symmetrical=False
                        ))
