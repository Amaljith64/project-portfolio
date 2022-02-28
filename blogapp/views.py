from django.shortcuts import render, redirect

from .models import BlogPost

from .forms import BlogPostForm

# Create your views here.

# def check(request):
#     return render(request,'view.html')

def index(request):
    posts = BlogPost.objects.all()
    context = {'posts': posts}
    return render(request, 'blog.html', context)

def detail(request,post_id):
    post = BlogPost.objects.get(id=post_id)
    context = {'posts': post}
    return render(request, 'view.html', context)

def new_post(request):
    if request.method == "POST":
        name = request.POST.get('name')
        job = request.POST.get('job')
        desc = request.POST.get('desc')
        img = request.FILES['img']
        phone = request.POST.get('phone')
        s = BlogPost(name=name, job=job, desc=desc, img=img,phone=phone)
        s.save()
        print('product added')
    return render(request, "new_post.html")

def edit_post(request, post_id):
    obj = BlogPost.objects.get(id=post_id)
    form = BlogPostForm(request.POST or None, request.FILES, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('blogs:index')
    return render(request, 'edit.html', {'form': form, 'post': obj})



def delete(request,post_id):
    if request.method=='POST':
     obj=BlogPost.objects.get(id=post_id)
     obj.delete()
     return redirect('blogs:index')

    return render(request,'delete.html')