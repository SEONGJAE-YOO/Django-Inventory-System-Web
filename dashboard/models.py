from calendar import c
from curses.ascii import NUL
from datetime import date
from sre_constants import CATEGORY
from unicodedata import category, name
from django.db import models
from numpy import product
from django.contrib.auth.models import User

CATEGORY = (
    ('Stationary','Stationary'),
    ('Electronics','Electronics'),
    ('Food','Food'),

)


class Product(models.Model):
    name = models.CharField(max_length=100, null=True)
    category = models.CharField(max_length=20, choices=CATEGORY, null=True)
    quantity = models.PositiveIntegerField(null=True)


    def __str__(self):   # Product 제품 이름 보이게 설정
        return f'{self.name}'

class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    staff = models.ForeignKey(User,models.CASCADE, null=True)
    order_quantity = models.PositiveIntegerField(null=True )
    date = models.DateTimeField(auto_now_add=True)

# str : 인스턴스 출력 형식 함수
    def __str__(self):
        return f'{self.product} ordered by {self.staff.username}'


