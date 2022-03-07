from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('log',views.log,name='log'),
    path('regis',views.regis,name='regis'),
    path('lout',views.lout,name='lout')

]