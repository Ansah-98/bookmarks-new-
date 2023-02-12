from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms
from .models import Profile

class LoginForm(forms.Form):
    username = forms.CharField(max_length=200)
    password = forms.CharField(widget=forms.PasswordInput)

class UserRegistrationForm(ModelForm):
    password = forms.CharField(label='Password', widget =forms.PasswordInput)
    password2 = forms.CharField(label='Repeat Password' , widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username','first_name','email']
    
    def cleaned_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError(' the passwords provided dont match ')
        return cd['password2']

class Profile_form(ModelForm):
    class Meta:
        model = Profile
        fields = ['date_of_birth','img']