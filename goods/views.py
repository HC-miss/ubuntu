from django.http import HttpResponse
from django.shortcuts import render
from goods.models import *


def index(request):
    typegoods = TypeGoods.objects.all()
    goods = list(zip(["fruit", "seafood", "meet", "egg", "vegetables", "ice"],typegoods))
    print(goods)
    return render(request,'index1.html', {'goods': goods})
