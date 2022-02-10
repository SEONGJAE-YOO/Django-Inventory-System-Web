import imp
from multiprocessing import context
from django.shortcuts import render, redirect

# HttpResponse: 응답에 대한 메타정보를 가지고 있는 객체
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required 
from .models import Product
from .forms import ProductForm
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User

# 데코레이터(decorator)는 @ 붙여서 실행한다.
# 데커레이터는 다른 함수를 인수로 받는 콜러블(데커레이터된 함수)이다

@login_required
def index(request):
    #return HttpResponse('<h1> 메인 페이지 </h1>')
    return render(request, 'dashboard/index.html') # templates 폴더에서 index.html 불러옴 
    
    '''
    예시)
     return render(request, 'polls/index.html', context) 
     render() 함수는 request 객체를 첫번째 인수로 받고, 템플릿 이름을 두번째 인수로 받으며, context 사전형 객체를 세전째 선택적(optional) 인수로 받습니다. 인수로 지정된 context로 표현된 템플릿의 HttpResponse 객체가 반환됩니다.
  
    '''
@login_required
def staff(request):
    #return HttpResponse('관리자 페이지')
    workers = User.objects.all()
    context={
        'workers':workers
    }
    return render(request, 'dashboard/staff.html',context)

@login_required
def staff_detail(request, pk):
    workers = User.objects.get(id=pk)
    context={
        'workers':workers,
    } 
    return render(request, 'dashboard/staff_detail.html',context)


@login_required
def product(request):
    items = Product.objects.all() # db 가져오기
    
    #items = Product.objects.raw('SELECT * FROM dashboard_product') # db 가져오기
    if request.method =='POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save() 
            return redirect('dashboard-product')
    else:
        form = ProductForm()
    context = {
        'items' : items,
        'form' : form,

    }
    return render(request, 'dashboard/product.html', context)    


@login_required
def product_delete(request, pk):
    item = Product.objects.get(id=pk) 
    if request.method=='POST':
        item.delete()
        return redirect('dashboard-product')
    return render(request, 'dashboard/product_delete.html') 

# edit 누르면 이함수 작동함
@login_required
def product_update(request, pk):
    item = Product.objects.get(id=pk)
    if request.method=='POST':
        form = ProductForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('dashboard-product')
    else:
        form = ProductForm(instance=item)

    context={
        'form':form, 


    }
    return render(request, 'dashboard/product_update.html',context)


@login_required
def order(request):
    return render(request, 'dashboard/order.html')   

