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
