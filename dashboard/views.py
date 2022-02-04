from django.shortcuts import render

# HttpResponse: 응답에 대한 메타정보를 가지고 있는 객체
from django.http import HttpResponse

def index(request):
    #return HttpResponse('<h1> 메인 페이지 </h1>')
    return render(request, 'dashboard/index.html') # templates 폴더에서 index.html 불러옴 
    
    '''
    예시)
     return render(request, 'polls/index.html', context) 
     render() 함수는 request 객체를 첫번째 인수로 받고, 템플릿 이름을 두번째 인수로 받으며, context 사전형 객체를 세전째 선택적(optional) 인수로 받습니다. 인수로 지정된 context로 표현된 템플릿의 HttpResponse 객체가 반환됩니다.
    '''
def staff(request):
    #return HttpResponse('관리자 페이지')
    return render(request, 'dashboard/staff.html')