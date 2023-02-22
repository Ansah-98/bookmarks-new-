from django.urls import path
from .views import image_create

urlpatterns = [path('image-create/', image_create,name = 'create-image')]