import os
from django.core.files import File
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
        response = requests.get(image_url,stream = True)
        try:
            response.raise_for_status()
            
        except Exception as exc:
            print('there was a problem')
        print(type(response))
        file = open(os.getcwd() + image_name, 'wb')
        for chunk in response.iter_content(1024):
            file.write(chunk)
        file.close()
        open_file = open(os.getcwd() + image_name, 'rb')

        content = File(file = open_file , name = image_name)
        image.image.save(name = image_name,content= content, save= False)

        open_file.close()
        if commit:
            image.save()
        return image
        