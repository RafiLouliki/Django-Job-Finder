from django.shortcuts import redirect, render
from .models import Job
from django.core.paginator import Paginator
from django.urls import reverse
from .forms import ApplyForm,JobForm
from django.contrib.auth.decorators import login_required
from .filters import JobFilter
# Create your views here.

def job_list(request):
    job_list=Job.objects.all()
    #Filter Section:We will pass all job_list to Jobfilter to filter all the results then pass the filtering job_list to the paginator
    myfilter=JobFilter(request.GET,queryset=job_list)
    job_list=myfilter.qs

    paginator=Paginator(job_list,2)
    page_number=request.GET.get('page')
    page_obj=paginator.get_page(page_number)
    context={'jobs':page_obj,'myjobfilter':myfilter}
    return render(request,'job/job_list.html',context)





def job_detail(request,slug):
    job_detail=Job.objects.get(slug=slug)
    if request.method=='POST':
        form=ApplyForm(request.POST,request.FILES)
        if form.is_valid():
            myform=form.save(commit=False)
            myform.job=job_detail
            myform.save()
            form=ApplyForm() #this line is for clear all form fields after submitting
            print('Succesfully Submit')
    else:
        form=ApplyForm()


    context={'job':job_detail,'jobform':form}
    return render(request,'job/job_detail.html',context)
    

    #myform.job[is the name of the field in apply form]=job_detail[is for know that we are apply the same job]

#We add decorator For force the user to login first then he can post a job(only Users have login can post job)

@login_required
def add_job(request):
    if request.method=="POST":
        form=JobForm(request.POST,request.FILES)
        if form.is_valid():
            myform=form.save(commit=False)
            myform.owner=request.user
            myform.save()
            form=JobForm() #this line is for clear all form fields after submitting
            return redirect(reverse('jobs:job_list'))
    else:
        form=JobForm()
    

        
    return render(request,'job/add_job.html',{'postform':form})