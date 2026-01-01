from django.urls import path
from .views import *

urlpatterns = [

      path('homecall/',homecall),
      path('add/',add),
      path('',Land)

]