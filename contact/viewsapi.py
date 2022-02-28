from .models import Job,apply,Category
from .serializers import JobSerializer,ApplySerializer,CategorySerializer
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.decorators import api_view

# Create your views here.

#Generic Based Views

class Job_ListApi(generics.ListCreateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer


class Job_DetailApi(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = JobSerializer
    queryset = Job.objects.all()
    lookup_field = 'id'
    

class Category_ListApi(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class Category_DetailApi(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    lookup_field = 'id'


class Apply_ListApi(generics.ListCreateAPIView):#{GET&POST}
    queryset = apply.objects.all()
    serializer_class = ApplySerializer

class Apply_DetailApi(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ApplySerializer
    queryset = apply.objects.all()
    lookup_field = 'id'

#End Of Generic Class Based Views



#Function Based Views
@api_view(['GET'])
def job_list_func_api(request):
    all_jobs = Job.objects.all()
    data = JobSerializer(all_jobs, many=True).data
    return Response({'data':data})


@api_view(['GET'])
def job_detail_func_api(request,id):
    job_detail = Job.objects.get(id=id)
    data = JobSerializer(job_detail).data
    return Response({'data':data})


@api_view(['GET'])
def Category_list_func_api(request):
    all_Category = Category.objects.all()
    data = CategorySerializer(all_Category, many=True).data
    return Response({'data':data})



@api_view(['GET'])
def Category_detail_func_api(request,id):
    Category_detail = Category.objects.get(id=id)
    data = CategorySerializer(Category_detail).data
    return Response({'data':data})


@api_view(['GET'])
def Apply_list_func_api(request):
    all_Apply = apply.objects.all()
    data = ApplySerializer(all_Apply, many=True).data
    return Response({'data':data})



@api_view(['GET'])
def Apply_detail_func_api(request,id):
    Apply_detail = apply.objects.get(id=id)
    data = ApplySerializer(Apply_detail).data
    return Response({'data':data})

#ُEnd Fuction Based Views Api



