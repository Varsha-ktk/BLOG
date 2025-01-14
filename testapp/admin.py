from django.contrib import admin

from testapp import models

# Register your models here..
admin.site.register(models.Login_view)
admin.site.register(models.Blogger)
admin.site.register(models.Blogveiwer)
admin.site.register(models.Addblog)