from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='dashboard-index'),
    path('staff/',views.staff, name='dashboard-staff'), # topnav.html에 url 연결시켜주기
    path('product/',views.product, name='dashboard-product'),
    path('order/',views.order, name='dashboard-order'),
]