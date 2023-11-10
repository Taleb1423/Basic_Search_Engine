from django.urls import path

from .views import success_page
from .views import mainA

from . import views

urlpatterns = [

   # path('', main),

    path('', views.main, name='main'),
    path('success/', success_page, name='success_page'),
    path('',mainA, name="mainA")
]