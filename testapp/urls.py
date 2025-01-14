from django.urls import path

from testapp import views, admin_views, blogger_views, blogveiwer_views

urlpatterns=[
    path('',views.home,name='home'),
    path('login',views.loginpage,name='login'),
    path('logout_view', views.logout_view, name='logout_view'),

    path('blogger',views.blogger,name='blogger'),
    path('blogveiwer',views.blogveiwer,name='blogveiwer'),

    path('adminbase', views.adminbase, name='adminbase'),
    path('bloggerbase', views.bloggerbase, name='bloggerbase'),
    path('blogveiwerbase', views.blogveiwerbase, name='blogveiwerbase'),

    path('bloggers_view', admin_views.bloggers_view, name='bloggers_view'),
    path('blogviewers_table', admin_views.blogviewers_table, name='blogviewers_table'),

    path('blogger_delete/<int:id>/', admin_views.blogger_delete, name='blogger_delete'),
    path('blogviewer_delete/<int:id>/', admin_views.blogviewer_delete, name='blogviewer_delete'),
    path('blogger_update/<int:id>/', admin_views.blogger_update, name='blogger_update'),
    path('blogviewer_update/<int:id>/', admin_views.blogviewer_update, name='blogviewer_update'),
    path('viewblog', admin_views.viewblog, name='viewblog'),


    #blogger
    path('blog',blogger_views.blog,name='blog'),
    path('blogview',blogger_views.blogview,name='blogview'),
    path('postupdate/<int:id>/', blogger_views.postupdate, name='postupdate'),
    path('postdelete/<int:id>/', blogger_views.postdelete, name='postdelete'),

    #blogviewer

    path('view_blogposts', blogveiwer_views.view_blogposts, name='view_blogposts'),


]