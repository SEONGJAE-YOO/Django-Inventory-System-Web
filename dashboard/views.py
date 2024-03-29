import imp
from multiprocessing import context
from pickle import FALSE
from django.shortcuts import render, redirect

# HttpResponse: 응답에 대한 메타정보를 가지고 있는 객체
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from pyparsing import Or 
from .models import Product, Order
from .forms import ProductForm ,OrderForm  #forms 파일에서 함수 불러옴
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib import messages


# 데코레이터(decorator)는 @ 붙여서 실행한다.
# 데커레이터는 다른 함수를 인수로 받는 콜러블(데커레이터된 함수)이다

@login_required
def index(request):
    #return HttpResponse('<h1> 메인 페이지 </h1>')
    orders = Order.objects.all()
    products = Product.objects.all()
    orders_count = orders.count()
    product_count = products.count()
    workers_count = User.objects.all().count() # db 가져오기

    if request.method=='POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.staff = request.user
            instance.save()
            return redirect('dashboard-index')
    else:
        form = OrderForm()
    context={
        'orders':orders,
        'form':form,
        'products':products,
        'product_count':product_count,
        'workers_count':workers_count,
        'orders_count':orders_count,
        
    }
    return render(request, 'dashboard/index.html',context) # templates 폴더에서 index.html 불러옴 
    
    '''
    예시)
     return render(request, 'polls/index.html', context) 
     render() 함수는 request 객체를 첫번째 인수로 받고, 템플릿 이름을 두번째 인수로 받으며, context 사전형 객체를 세전째 선택적(optional) 인수로 받습니다. 인수로 지정된 context로 표현된 템플릿의 HttpResponse 객체가 반환됩니다.
  
    '''
@login_required
def staff(request):
    #return HttpResponse('관리자 페이지')
    workers = User.objects.all()
    workers_count = workers.count()
    orders_count = Order.objects.all().count()
    product_count = Product.objects.all().count() # db 가져오기

    context={
        'workers':workers,
        'workers_count':workers_count,
        'orders_count':orders_count,
        'product_count':product_count,
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
    product_count = items.count()
    #items = Product.objects.raw('SELECT * FROM dashboard_product') # db 가져오기
    workers_count = User.objects.all().count()
    orders_count = Order.objects.all().count()

    if request.method =='POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save() 
            product_name = form.cleaned_data.get('name')
            messages.success(request,f'{product_name} has been added')
            return redirect('dashboard-product')
    else:
        form = ProductForm()
    context = {
        'items' : items,
        'form' : form,
        'workers_count':workers_count,
        'orders_count':orders_count,
        'product_count':product_count,
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
    orders = Order.objects.all()
    orders_count = orders.count()
    workers_count = User.objects.all().count()
    product_count = Product.objects.all().count() # db 가져오기

    context={
        'orders':orders,
        'workers_count':workers_count,
        'orders_count':orders_count,
        'product_count':product_count,
    }
    return render(request, 'dashboard/order.html',context)   

