from django.urls import path
from .views import *

urlpatterns = [
      path('',landingpage),
      path('home/',homecall),
      path('add/',add),
      # path('',land),

]