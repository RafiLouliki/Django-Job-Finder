from contact import views
from django.urls import path

from django.urls.conf import include
from contact import viewsapi
"""the app_name variable provided for {% url 'namespace-for-url-ofproject:the nameofviewinpath' and relate it with id%}"""
app_name='contact'


urlpatterns = [
    path('',views.sendmsg,name="contact_sendmsg"),

          #Generic Class Based Views Api
    path('api/information',viewsapi.Information_ListApi.as_view(),name='information_list_api'),
    path('api/information/<int:id>',viewsapi.Information_DetailApi.as_view(),name='information_detail_api'),
    #End of Generic Class Based Views Api

    #Function Based Views Api
    path('api/informationfunc',viewsapi.information_list_func_api , name='information_list_func_api'),
    path('api/informationfunc/<int:id>',viewsapi.information_detail_func_api , name='information_detail_func_api'),


    #End of Function Based Views Api
    
    
    
]
