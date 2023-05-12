from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
   # path('',views.welcome),
    # path('hold',views.holdHtmlMsg),
    # path('user',views.showhum),
    # path('',views.your),
    # path('',views.home,name='home'),
    path('home',views.home,name='home'),
    path('result',views.result,name='result'),
    path('graph1',views.graph1,name='graph1'),
    path('',views.graph1,name='graph1'),
    # path('graph1',views.graph1,name='graph1'),
    path('summary',views.summary,name='summary'),
    path('summary3',views.summary3,name='summary3'),
    path('summary4',views.summary4,name='summary4'),
    path('summary5',views.summary4,name='summary4'),
    path('kmeanAlgo',views.kmeanAlgo,name='kmeanAlgo'),
    path('nutrients',views.nutrients,name='condition'),
]


