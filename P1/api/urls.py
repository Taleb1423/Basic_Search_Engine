from django.urls import path

from .views import success_page

from . import views

urlpatterns = [

   # path('', main),

    path('', views.main, name='main'),
    path('success/', success_page, name='success_page'),
    
]