from django.urls import path
from . import views

app_name = 'account'

urlpatterns = [
  path('sign/', views.sign, name='sign'),
  path('login/', views.log, name='login'),
]