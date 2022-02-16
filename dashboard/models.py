from calendar import c
from sre_constants import CATEGORY
from tabnanny import verbose
from unicodedata import category, name
from django.db import models
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

    # Meta 옵션이란 다음과 같이 Inner class로 사용하여 상위 클래스에게 meta data를 제공하는것입니다.
    class Meta:
        verbose_name_plural = 'Product'


    def __str__(self):   # Product 제품 이름 보이게 설정
        return f'{self.name}'

class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    staff = models.ForeignKey(User,models.CASCADE, null=True)
    order_quantity = models.PositiveIntegerField(null=True )
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Order'
# str : 인스턴스 출력 형식 함수
    def __str__(self):
        return f'{self.product} ordered by {self.staff.username}'


