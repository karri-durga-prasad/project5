from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

def like(request):
    return HttpResponse('liked the video')

def unlike(request):
    return HttpResponse('unlike the video')
