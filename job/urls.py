from unicodedata import name
from job import views
from django.urls import path

from django.urls.conf import include
from job import viewsapi
"""the app_name variable provided for {% url 'namespace-for-url-ofproject:the nameofviewinpath' and relate it with id%}"""
app_name='job'


urlpatterns = [
    path('',views.job_list,name="job_list"),
    path('add',views.add_job,name="add_job"),
    path('<str:slug>',views.job_detail,name="job_detail"),
    #Generic Class Based Views Api
    path('api/jobs',viewsapi.Job_ListApi.as_view(),name='job_list_api'),
    path('api/jobs/<int:id>',viewsapi.Job_DetailApi.as_view(),name='job_detail_api'),
    path('api/category',viewsapi.Category_ListApi.as_view(),name='category_list_api'),
    path('api/category/<int:id>',viewsapi.Category_DetailApi.as_view(),name='category_detail_api'),
    path('api/apply',viewsapi.Apply_ListApi.as_view(),name='apply_list_api'),
    path('api/apply/<int:id>',viewsapi.Apply_DetailApi.as_view(),name='apply_detail_api'),
    #End of Generic Class Based Views Api

    #Function Based Views Api
    path('api/jobsfunc',viewsapi.job_list_func_api , name='job_list_func_api'),
    path('api/jobsfunc/<int:id>',viewsapi.job_detail_func_api , name='job_detail_func_api'),
    path('api/categoryfunc',viewsapi.Category_list_func_api , name='Category_list_func_api'),
    path('api/categoryfunc/<int:id>',viewsapi.Category_detail_func_api , name='Category_detail_func_api'),
    path('api/applyfunc',viewsapi.Apply_list_func_api , name='Apply_list_func_api'),
    path('api/applyfunc/<int:id>',viewsapi.Apply_detail_func_api , name='Apply_detail_func_api'),
    #End of Function Based Views Api
    
]
