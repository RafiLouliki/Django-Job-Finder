from .models import Job,apply,Category
from .serializers import JobSerializer,ApplySerializer,CategorySerializer
from rest_framework.response import Response
from rest_framework import generics
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