from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog
from django.utils import timezone

# Create your views here.
def home(request):
    blogs = Blog.objects 
    return render(request, 'home.html', {'blogs' : blogs})

def profile(request):
    return render(request, 'profile.html')

def hobby(request):
    return render(request, 'hobby.html')

def new(request):
    return render(request, 'new.html', {'new' : new})

def detail(request, blog_id):
    details = get_object_or_404(Blog, pk = blog_id)
    return render(request, 'detail.html', {'details' : details})

def create(request):
    blog = Blog()
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.writer = request.GET['writer']
    blog.category = request.GET['category']
    blog.save()
    return redirect('home')

def edit(request, blog_id):
    blog = get_object_or_404(Blog, pk = blog_id)
    return render(request, 'edit.html', {'blog' : blog})

def update(request, blog_id):
    blog = get_object_or_404(Blog, pk = blog_id)
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.writer = request.GET['writer']
    blog.category = request.GET['category']
    blog.save()
    return redirect('home')

def delete(request, blog_id):
    blog = get_object_or_404(Blog, pk = blog_id)
    blog.delete()
    return redirect('home')