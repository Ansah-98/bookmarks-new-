
from .models import Contact
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from common.decorators import ajax_required
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

def profile_register(request):
    if request.method == 'POST':
        form = Profile_form(request.POST,request.FILES)
        if form.is_valid(): 
            cd  = form.save(commit=False)
            cd.user = request.user
            cd.save()
            return redirect('dashboard')
    else:
        form = Profile_form()
    return render(request,'account/profile_form.html', {'form':form})


def registration(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit = False )
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            login(request, new_user)
            return redirect('profile-register')
    else:
        form = UserRegistrationForm()
    return render(request,'account/register.html', {'form':form})

@login_required
def user_list(request):
    users = User.objects.all()
    return render(request, 'account/list_users.html',{'section':'people','users':users})

@login_required
def user_detail(request,username):
    user  = User.objects.filter(username=username)

    return render(request,'account/user_detail.html',{'section':'people','user':user})

@ajax_required
@login_required
def user_follow(request):
    user_id = request.POST.get('id')
    action = request.POST.get('action')
    if user_id and action:
        try:
            user = User.objects.get(pk = user_id)
            if action == 'follow':
                Contact.objects.get_or_create(
                    user_from= request.user,
                    user_to = user)
            else:
                Contact.objects.filter(user_from = request.user,user_to  = user).delete()
        except User.DoesNotExist:
            return JsonResponse({'status':'error'})
    return JsonResponse({'status':'error'})