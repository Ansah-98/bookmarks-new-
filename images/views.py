from django.shortcuts import redirect, render
from django.contrib import messages
# Create your views here.
from .models import Images
from django.contrib.auth.decorators import login_required
from .forms import ImageForm
@login_required
def image_create(request):
    if request.method  == 'POST':
        form = ImageForm(data = request.POST)
        if form.is_valid():
            cd  = form.cleaned_data
            new_item = form.save(commit=False)
            new_item.user = request.user
            new_item.save()
            messages.success(request,'image added successfully')
            return redirect(new_item.get_absolute_url())
    else:
        #print(request.GET['url'])
        form = ImageForm(data = request.GET)
    return render(request,'images/create.html',
    {'section':'images', 'form':form})

def image_detail(request,id):
    image  = Images.objects.get(pk =id)
    return render(request,'image/detail.html', {'section':'detail','image':image})