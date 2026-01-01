from django.urls import path
from .views import *

urlpatterns = [
    path('homepage/', homepage),
    path('dbitem/',dbitemdisp),
    path('view/',viewcart),
    path('addtocart/',addtocart),
    path('clearcart/',clearcart),
    path('getalldata/',getalldata),
    path('ser/',Search),
    path('details/<str:key>/',prod),
    path('getpro/<str:keyw>/',getproduct)
    
]

