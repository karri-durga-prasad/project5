from django.urls import path

from request.views import *

urlpatterns=[
    path('friend/',friend,name='friend'),
    path('unfriend/',unfriend,name='unfriend'),
]