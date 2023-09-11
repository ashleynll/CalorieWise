from django.urls import path
from . import views #import views.py from CalorieCounter

urlpatterns = [
    path('',views.home,name='home'),
]