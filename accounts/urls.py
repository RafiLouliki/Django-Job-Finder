from accounts import views
from django.urls import path

from django.urls.conf import include

"""the app_name variable provided for {% url 'namespace-for-url-ofproject:the nameofviewinpath' and relate it with id%}"""
app_name='accounts'


urlpatterns = [
    path('signup',views.signup,name="signup"),
    
]
