from multiprocessing import context
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm

def register(request):
    if request.method =='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid(): #유효하면 저장하라
            form.save()
            return redirect('dashboard-index') 
    else:
        form = UserCreationForm()
    context = {
        'form':form,


    }
    return render(request, 'user/register.html',context)

