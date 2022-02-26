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

    path('api/jobs',viewsapi.Job_ListApi.as_view(),name='job_list_api'),
    path('api/jobs/<int:id>',viewsapi.Job_DetailApi.as_view(),name='job_detail_api'),
    path('api/category',viewsapi.Category_ListApi.as_view(),name='category_list_api'),
    path('api/category/<int:id>',viewsapi.Category_DetailApi.as_view(),name='category_detail_api'),

    path('api/apply',viewsapi.Apply_ListApi.as_view(),name='apply_list_api'),
    path('api/apply/<int:id>',viewsapi.Apply_DetailApi.as_view(),name='apply_detail_api'),

    
]
