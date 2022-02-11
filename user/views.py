from multiprocessing import context
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group
from .forms import CreateUserForm, UserUpdateForm, ProfileUpdateForm
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages


def register(request):
    if request.method =='POST':
        form = CreateUserForm(request.POST)
        if form.is_valid(): #유효하면 저장하라
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account has been created for {username}. Continue to Log in')
            return redirect('user-login') 
    else:
        form = CreateUserForm()
    context = {
        'form':form


    }
    return render(request, 'user/register.html',context)


def profile(request):
    return render(request, 'user/profile.html')

def profile_update(request):
    if request.method =='POST':
        user_form = UserUpdateForm(request.POST)
        profile_form= ProfileUpdateForm(request.POST, request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('user-profile')
    else:
        user_form =  UserUpdateForm()
        profile_form = ProfileUpdateForm() 

    context ={
        'user_form' : user_form,
        'profile_form': profile_form,
        
    }

    return render(request, 'user/profile_update.html', context)

