from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.

def save(request):
    return HttpResponse('post saved')

def unsave(request):
    return HttpResponse('post unsaved')