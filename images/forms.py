from django.core.files.base import ContentFile
import requests
from urllib import request
from django.utils.text import slugify
from django import forms
from .models import Images
from django.forms import ModelForm

class ImageForm(ModelForm):
    class Meta:
        model = Images
        fields =['title','url','description']
        widgets = {'url':forms.HiddenInput}

    def clean_url(self):
        url = self.cleaned_data['url']
        valid_extensions = ['jpeg','jpg','png']
        extension = url.rsplit('.',1)[1].lower()
        if extension not in valid_extensions:
            raise forms.ValidationError('there is a problem with the image extension')
        return url
    
    def save(self,force_insert=False, commit = True,force_update = False):
        image  = super().save(commit=False)
        image_url = self.cleaned_data['url']
        name = slugify(image.title)
        extension = image_url.rsplit('.',1)[1].lower()
        image_name  = f"{name}.{extension}"
        #response = request.urlopen(image_url)
        response = requests.get(image_url)
        image.image.save(image_name,ContentFile(response.read(),save=False))
        
        if commit:
            image.save()
        return image
        