from app import views
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('hab',views.HAB,name='hab'),
    path('senate',views.senate,name='senate'),
    path('technical',views.technical,name='technical'),
    path('cultural',views.cultural,name='cultural'),
    path('sports',views.sports,name='sports'),
    path('welfare',views.welfare,name='welfare'),
    path('complaint',views.complaint,name='complaint'),
]
