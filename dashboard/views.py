from django.shortcuts import render

# HttpResponse: 응답에 대한 메타정보를 가지고 있는 객체
from django.http import HttpResponse

def index(request):
    return HttpResponse('메인 페이지')

