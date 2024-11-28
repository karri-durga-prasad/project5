from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.

def friend(request):
    return HttpResponse('we can message and look into feed')

def unfriend(request):
    return HttpResponse('spam caller')
