from django import forms
from django.contrib.auth.forms import UserCreationForm

from testapp.models import Login_view, Blogger, Blogveiwer, Addblog, Postblog


class LoginForm(UserCreationForm):

    class Meta:
        model = Login_view
        fields = ('username','email')


class BloggerForm(forms.ModelForm):
    class Meta:
        model=Blogger
        fields = '__all__'
        exclude = ('user','status1',)

class BlogveiwerForm(forms.ModelForm):

    class Meta:
        model=Blogveiwer
        fields = '__all__'
        exclude = ('user',)
class AddblogForm(forms.ModelForm):

    class Meta:
        model = Postblog
        fields = '__all__'
        exclude = ('user',)
