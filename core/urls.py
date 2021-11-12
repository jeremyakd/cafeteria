from django.urls import path
from core import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('sample/', views.sample, name='sample'),
    path('store/', views.store, name='store'),
]
