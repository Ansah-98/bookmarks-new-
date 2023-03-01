from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from common.decorators import ajax_required
from django.http import HttpResponse, JsonResponse
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


@ajax_required
@login_required
def image_likes(request):
    image_id = request.POST.get('id')
    action = request.POST.get('action')
    if image_id and action:
        try:
            image  = Images.objects.get(pk = image_id)
            if action == 'like':
                image.user_likes.add(request.user)
            else:
                image.user_likes.remove(request.user)
            return JsonResponse({'status': 'ok'})
        except:
            pass        
    return JsonResponse({'status': 'error'})

@login_required
def image_list(request):
    images = Images.objects.all()
    paginator = Paginator(images , 8)
    page = request.GET['pages']
    try:
        images = paginator.page(page)

    except PageNotAnInteger:
        images = paginator.page(1)
    except EmptyPage:
        if request.is_ajax:
            return HttpResponse('')
        images = paginator.page(paginator.num_pages)
    if request.is_ajax():
        return render(request,'images/list_ajax.html', {'section':images, 'images':images})
    return render(request, 'images/list.html',{'section':'images','images':images})