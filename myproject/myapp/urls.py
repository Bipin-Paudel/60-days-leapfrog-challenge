from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashbord, name='dashboard'),
    path('htmc/', views.htmc, name='htmc')
]
