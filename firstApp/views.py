from django.http.response import HttpResponse
from django.shortcuts import render, redirect, HttpResponse
from .models import *

# Create your views here.
def index(request):
    context = {
        "all_users": User.objects.all()
    }
    return render(request, "index.html", context)

def new(request):
    return HttpResponse('placeholder to display a new form to create a new blog')

def create(request):
    if request.method == 'POST' or request.method == 'FILES':
        new_user = User.objects.create(
            first_name = request.POST['first_name'],
            last_name = request.POST['last_name'],
            email = request.POST['email'],
            password = request.POST['password'],
            image = request.FILES['image'],
        )
    return redirect('/')

def show(request, user_id):
    user = User.objects.get(id = user_id)
    context= {
        "user": user
    }
    return render(request,'result.html', context)

def edit(request, blog_num):
    return HttpResponse(f'placeholder to edit blog {blog_num}')

def destroy(request, blog_num):
    return redirect('/')