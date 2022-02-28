from unicodedata import name
from blog import views
from django.urls import path
from django.urls.conf import include
from blog import viewsapi
"""the app_name variable provided for {% url 'namespace-for-url-ofproject:the nameofviewinpath' and relate it with id%}"""
app_name='blog'


urlpatterns = [
    path('',views.blog_list,name="blog_list"),
    path('addpost',views.create_post,name="blog_create_post"),
    path('post_detail/<str:slug>',views.blog_detail,name="blog_detail"),
      #Generic Class Based Views Api
    path('api/post',viewsapi.Post_ListApi.as_view(),name='post_list_api'),
    path('api/post/<int:id>',viewsapi.Post_DetailApi.as_view(),name='post_detail_api'),
    path('api/comment',viewsapi.Comment_ListApi.as_view(),name='comment_list_api'),
    path('api/comment/<int:id>',viewsapi.Comment_DetailApi.as_view(),name='comment_detail_api'),

    #End of Generic Class Based Views Api

    #Function Based Views Api
    path('api/postfunc',viewsapi.Post_list_func_api , name='post_list_func_api'),
    path('api/postfunc/<int:id>',viewsapi.Post_detail_func_api , name='post_detail_func_api'),
    path('api/commentfunc',viewsapi.Comment_list_func_api , name='Comment_list_func_api'),
    path('api/commentfunc/<int:id>',viewsapi.Comment_detail_func_api , name='Comment_detail_func_api'),

    #End of Function Based Views Api
    
    
]
