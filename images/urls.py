from django.urls import path
from .views import image_create,image_detail

urlpatterns = [path('image-create/', image_create,name = 'create-image') , 
                path('detail/<int:id>',image_detail, name = 'detail')]