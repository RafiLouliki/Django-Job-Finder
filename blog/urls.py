from unicodedata import name
from blog import views
from django.urls import path
from django.urls.conf import include

"""the app_name variable provided for {% url 'namespace-for-url-ofproject:the nameofviewinpath' and relate it with id%}"""
app_name='blog'


urlpatterns = [
    path('',views.blog_list,name="blog_list"),
    path('addpost',views.create_post,name="blog_create_post"),
    path('post_detail/<str:slug>',views.blog_detail,name="blog_detail"),
    
    
]
