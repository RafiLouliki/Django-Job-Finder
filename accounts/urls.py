from accounts import views
from django.urls import path

from django.urls.conf import include

"""the app_name variable provided for {% url 'namespace-for-url-ofproject:the nameofviewinpath' and relate it with id%}"""
app_name='accounts'


urlpatterns = [
    path('register',views.register,name="register"),
    path('profile',views.profile,name="profile"),
    path('profile/edit',views.profile_edit,name="profile_edit"),
    
]
