from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.urls import reverse
from .models import Post
from .forms import CommentForm,PostForm
from django.views import generic 
from django.contrib.auth.decorators import login_required

# Create your views here.

 
def blog_list(request):
    blog_list=Post.objects.all()
    
    paginator=Paginator(blog_list,2)
    page_number=request.GET.get('page')
    page_obj=paginator.get_page(page_number)

    context={'blogs':page_obj,}
    return render(request,'blog/blog_list.html',context)

@login_required
def blog_detail(request,slug):
    blog_detail=Post.objects.get(slug=slug)
    if request.method=='POST':
        form=CommentForm(request.POST,request.FILES)
        if form.is_valid():
            myform=form.save(commit=False)
            myform.post=blog_detail
            myform.username=str(request.user)
            myform.save()
            return redirect('blogs:blog_detail',slug=slug)
            form=CommentForm() #this line is for clear all form fields after submitting
            print('Succesfully Submit')
    else:
        form=CommentForm()


    context={'blog':blog_detail,'CommentForm':form}
    return render(request,'blog/blog_detail.html',context)

@login_required
def create_post(request):


    if request.method=="POST":

        form=PostForm(request.POST,request.FILES)
        if form.is_valid():
            
            myform=form.save(commit=False)
            myform.author=request.user
            myform.save()
            form=PostForm() #this line is for clear all form fields after submitting
            return redirect(reverse('blogs:blog_list'))
            
            
    else:
        form=PostForm()
    
    return render(request,'blog/create_post.html',{'CREATEPOSTFORM':form})
