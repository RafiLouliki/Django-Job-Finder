from unicodedata import name
from home import views
from django.urls import path

from django.urls.conf import include

"""the app_name variable provided for {% url 'namespace-for-url-ofproject:the nameofviewinpath' and relate it with id%}"""
app_name='home'



urlpatterns = [
    path('',views.home_index,name="home-page"),

]