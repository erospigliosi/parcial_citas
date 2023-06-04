from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")



def first_view(request):
    return HttpResponse('Esta es mi primera vista!')