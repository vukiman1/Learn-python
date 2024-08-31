from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Chào các bạn yêu!")


def thaytony(request):
    return HttpResponse("<h1>Thầy giáo mưa</h1>")