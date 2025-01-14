from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect

from testapp.forms import LoginForm, BloggerForm, BlogveiwerForm
from testapp.models import Blogger, Blogveiwer


# Create your views here.
def home(request):
    return render(request,'home.html')

def adminbase(request):
    return render(request,'Admin/adminbase.html')

def bloggerbase(request):
    return render(request,'Blogger/bloggerbase.html')

def blogveiwerbase(request):
    return render(request,'Blogviewer/blogviewerbase.html')


def blogger(request):
    data1 = LoginForm()
    data2 = BloggerForm()

    if request.method == 'POST':
        user1=LoginForm(request.POST)
        user2 = BloggerForm(request.POST)
        if user1.is_valid() and  user2.is_valid():
            form1 = user1.save(commit=False)
            form1.is_blogger = True
            form1.save()

            form2 = user2.save(commit=False)
            form2.user = form1
            form2.save()
            return redirect('login')

    return render(request,'register.html',{'form1':data1,'form2':data2})

def blogveiwer(request):
    data1=LoginForm()
    data2=BlogveiwerForm()
    if request.method == 'POST':
        user1=LoginForm(request.POST)
        user2 = BlogveiwerForm(request.POST)
        print(user1)
        print(user2)
        if user1.is_valid() and  user2.is_valid():
            form1=user1.save(commit=False)
            form1.is_blogveiwer = True
            form1.save()

            form2 = user2.save(commit=False)
            form2.user=form1
            form2.save()
            return redirect('login')

    return render(request,'register.html',{'form1':data1,'form2':data2})

def loginpage(request):
    if request.method == 'POST':
        username = request.POST.get('uname')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        print(username)
        print(password)
        print(user)
        if user is not None:
            login(request, user)
            if user.is_staff:
                print("admin")
                return redirect('adminbase')
            if user.is_blogger:
                print("is_blogger")
                return redirect('bloggerbase')
            if user.is_blogveiwer:
                print("is_blogveiwer")
                return redirect('blogveiwerbase')
        else:
            messages.info(request, 'invalid credential')

    return render(request, 'login.html')
def logout_view(request):
    logout(request)
    return redirect('login')