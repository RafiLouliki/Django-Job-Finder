from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from .forms import SignupForm,ProfileForm,UserForm
from .models import Profile
from django.urls import reverse
# Create your views here.

def register(request):
    if request.method=='POST':
        form=SignupForm(request.POST)
        if form.is_valid:
            form.save()
            #send username and password to authenticate and login to profile after signup
            username=form.cleaned_data['username']
            password=form.cleaned_data['password1']
            user=authenticate(username=username,password=password)
            login(request,user)
            return redirect('/accounts/profile')
            
    else:
        form=SignupForm()

    return render(request,'registration/signup.html',{'signupform':form})


def profile(request):
    profile = Profile.objects.get(user=request.user)
    return render(request,'accounts/profile.html',{'profile': profile})


def profile_edit(request):
    profile = Profile.objects.get(user=request.user)

    if request.method=='POST':
        user_form=UserForm(request.POST,instance=request.user)
        profile_form=ProfileForm(request.POST,request.FILES,instance=profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            myprofile_form=profile_form.save(commit=False)
            myprofile_form.user = request.user
            myprofile_form.save()

            return redirect(reverse('accounts:profile'))

    else:
        user_form=UserForm(instance=request.user)
        profile_form=ProfileForm(instance=profile)



    return render(request,'accounts/profile_edit.html',{"User_Form":user_form,"Profile_Form":profile_form})
