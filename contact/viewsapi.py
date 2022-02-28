from .models import Information
from .serializers import InformationSerializer
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.decorators import api_view

# Create your views here.

#Generic Based Views

class Information_ListApi(generics.ListCreateAPIView):
    queryset = Information.objects.all()
    serializer_class = InformationSerializer


class Information_DetailApi(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = InformationSerializer
    queryset = Information.objects.all()
    lookup_field = 'id'
    


#End Of Generic Class Based Views



#Function Based Views
@api_view(['GET'])
def information_list_func_api(request):
    all_information = Information.objects.all()
    data = InformationSerializer(all_information, many=True).data
    return Response({'data':data})


@api_view(['GET'])
def information_detail_func_api(request,id):
    information_detail = Information.objects.get(id=id)
    data = InformationSerializer(information_detail).data
    return Response({'data':data})



#ُEnd Fuction Based Views Api



