from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from testapp.forms import AddblogForm
from testapp.models import Blogger, Postblog

@login_required(login_url='login')
def blog(request):
    blogger  = request.user   #  to get user id
    print(blogger)
    obj = Blogger.objects.get(user = blogger)# to get seller id
    print(obj.id)
    data1=AddblogForm()

    if request.method == 'POST':
        user2 = AddblogForm(request.POST,request.FILES)
        if user2.is_valid():
            form1 = user2.save(commit=False)
            form1.user = obj
            form1.save()
            return redirect('bloggerbase')
    return render(request,'Blogger/addblog.html',{'data1':data1})



@login_required(login_url='login')
def blogview(request):
    user = request.user  # user id
    obj = Blogger.objects.get(user=user)
    data = Postblog.objects.filter(user=obj)
    return render(request,'Blogger/view postedblogs.html',{'data':data})

@login_required(login_url='login')
def postupdate(request,id):

    data = Postblog.objects.get(id=id)
    form = AddblogForm(instance=data)
    if request.method == 'POST':
        updated_data = AddblogForm(request.POST, request.FILES, instance=data)
        updated_data.is_valid()
        updated_data.save()
        return redirect('bloggerbase')

    return render(request, 'Blogger/postupdate.html', {'form': form})
@login_required(login_url='login')
def postdelete(request,id):
    data=Postblog.objects.get(id=id)
    data.delete()
    return redirect('bloggerbase')



