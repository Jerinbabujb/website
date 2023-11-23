from . import views
from django.urls import path

import travelproject

urlpatterns = [
    path('',views.demo,name='demo'),
]
