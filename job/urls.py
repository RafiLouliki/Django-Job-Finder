from job import views
from django.urls import path

from django.urls.conf import include

"""the app_name variable provided for {% url 'namespace-for-url-ofproject:the nameofviewinpath' and relate it with id%}"""
app_name='job'


urlpatterns = [
    path('',views.job_list,name="job_list"),
    path('add',views.add_job,name="add_job"),
    path('<str:slug>',views.job_detail,name="job_detail"),
    
]
