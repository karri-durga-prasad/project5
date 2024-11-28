from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

def scroll(request):
    return HttpResponse('video was not good')

def stop(request):
    return HttpResponse('video was good')