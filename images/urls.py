from django.urls import path
from .views import image_create,image_detail,image_likes, image_list

urlpatterns = [path('image-create/', image_create,name = 'create-image') , 
                path('detail/<int:id>',image_detail, name = 'detail'),
                path('likes',image_likes,name = 'likes'),
                path('', image_list, name='list'),]