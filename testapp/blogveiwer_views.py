from django.shortcuts import render

from testapp.models import Postblog


def view_blogposts(request):
    data=Postblog.objects.all()
    print(data)
    return render(request,'Blogviewer/viewblogs.html',{'data':data})






