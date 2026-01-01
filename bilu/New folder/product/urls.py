from django.urls import path
from .views import *

urlpatterns = [
    path('homepage/', homepage, name='homepage'),
    path('dbitems/', dbitems, name='dbitems'),
    path('productdetail/<int:id>/', productdetail, name='productdetail'),
    path('view/', view, name='view'),
    path('addcart/', addcart, name='addcart'),
    path('clearcart/', clearcart, name='clearcart'),
    path('search/', search, name='search'),
    path('getalldata/', getalldata, name='getalldata'),
    path('getproduct/<str:keyw>/', getproduct, name='getproduct'),
]
