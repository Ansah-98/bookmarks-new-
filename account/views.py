from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse
from django.shortcuts import redirect, render
from .forms import LoginForm,UserRegistrationForm,Profile_form
# Create your views here.

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,username = cd['username'], password = cd['password'])

            if user is not None :
                login(request,user)
                return HttpResponse('Authenticated successfully')
        else:
            return HttpResponse("invalid login")
    else :
        form = LoginForm() 
    return render(request, 'account/login.html',{'form':form,})
@login_required
def dashboard(request):
    return render(request,'account/dashboard.html',{'section':'dashboard'})

def registration(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit = False )
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            return redirect('profile_registration')
    form = UserRegistrationForm()
    return render(request,'account/register.html', {'form':form})

def profile_registration(request):
    if request.method == 'POST':
        form = Profile_form(request.POST)
        if form.is_valid():
            cd  = form.save(commit=False)
            cd.user = request.user
            cd.save()
            return redirect('dashboard')
    else:
        form = Profile_form()
    return render(request,'account/profile_form.html', {'form':form})
        