from django.shortcuts import render, redirect

from testapp.forms import BloggerForm, BlogveiwerForm
from testapp.models import Blogveiwer, Blogger, Postblog


def bloggers_view(request):
    data=Blogger.objects.all()
    return render(request,'Admin/blogger_table.html',{'data':data})
def blogger_delete(request,id):
    data = Blogger.objects.get(id=id)
    data.delete()
    return render(request, 'Admin/blogger_table.html', {'data': data})
def blogviewers_table(request):
    data=Blogveiwer.objects.all()
    return render(request,'Admin/blogviewers_table.html',{'data':data})
def blogviewer_delete(request,id):
    data = Blogveiwer.objects.get(id=id)
    data.delete()
    return render(request, 'Admin/blogviewers_table.html', {'data': data})

def blogger_update(request,id):
    data=Blogger.objects.get(id=id)
    form=BloggerForm(instance=data)
    if request.method=='POST':
        updated_data=BloggerForm(request.POST,request.FILES,instance = data)
        updated_data.is_valid()
        updated_data.save()
        return redirect('adminbase')

    return render(request,'Admin/blogger_update.html',{'form':form})

def blogviewer_update(request,id):
    data=Blogveiwer.objects.get(id=id)
    form=BlogveiwerForm(instance=data)
    if request.method=='POST':
        updated_data=BlogveiwerForm(request.POST,request.FILES,instance = data)
        updated_data.is_valid()
        updated_data.save()
        return redirect('adminbase')

    return render(request,'Admin/blogger_update.html',{'form':form})
def viewblog(request):
    data=Postblog.objects.all()
    return render(request,'Admin/viewblogs.html',{'data':data})