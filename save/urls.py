from django.urls import path

from save.views import *

urlpatterns=[
    path('save/',save,name='save'),
    path('unsave/',unsave,name='unsave'),
]