from django.shortcuts import render, HttpResponse
from pprint import pprint
import random

# Create your views here.
def index(request):
    # print(request)
    # print(type(request))
    # pprint(request.META)
    return HttpResponse('goed morgen!')
    
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