from django.shortcuts import render, HttpResponse
from pprint import pprint
import random
from datetime import datetime

# Create your views here.
def index(request):
    # print(request)
    # print(type(request))
    # pprint(request.META)
    # return HttpResponse('goed morgen!')
    return render(request, 'index.html')
    
def dinner(request):
    menus = ['닭볶음탕', '치킨', '소고기']
    # return HttpResponse(random.choice(menu))
    pick = random.choice(menus)
    return render(request, 'dinner.html', {'menus': menus, 'pick': pick})

def hello(request, name):
    return render(request, 'hello.html', {'name': name})
    
def cube(request,num):
    ans = num **3
    return render(request, 'cube.html', {'ans': ans, 'num': num})
    
def ping(request):
    return render(request, 'ping.html')
    
def pong(request):
    print(request.GET)
    data = request.GET.get('data')
    return render(request, 'pong.html', {'data': data})

def user_new(request):
    # 닉네임, 패스워드를 받아서
    return render(request, 'user_new.html')
    
    
def user_create(request):
    nickname = request.POST.get('nickname')
    pw = request.POST.get('pw')
    return render(request, 'user_create.html', {'nickname' : nickname, 'pw': pw})
    #post 방식으로

def template_example(request):
    my_list = ['짜장면', '탕수육', '제육볶음', '육회']
    my_sentence = 'life is short, you need python'
    messages = ['apple', 'avocado', 'pair', 'mango']
    empty_list = []
    datetimenow = datetime.now()
    return render(request, 'template_example.html', 
                {'my_list' : my_list,'my_sentence': my_sentence,
                'messages': messages, 'empty_list' : empty_list,
                'datetimenow' : datetimenow
                })

def static_example(request):
    return render(request, 'static_example.html')