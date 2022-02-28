from django.shortcuts import render

# Create your views here.


def home_index(request):
    return render(request,'home/homepage.html')