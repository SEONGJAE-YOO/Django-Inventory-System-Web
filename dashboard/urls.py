from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.index, name='dashboard-index'),
    path('staff/',views.staff, name='dashboard-staff'), # topnav.html에 url 연결시켜주기
    path('staff/detail/<int:pk>/',views.staff_detail, name='dashboard-staff-detail'), # topnav.html에 url 연결시켜주기
    path('product/',views.product, name='dashboard-product'),
    path('product/delete/<int:pk>/',views.product_delete, name='dashboard-product-delete'),
    path('product/update/<int:pk>/',views.product_update, name='dashboard-product-update'),
    path('order/',views.order, name='dashboard-order'),
]
 

