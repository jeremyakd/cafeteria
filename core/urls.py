from django.urls import path
from core import views

urlpatterns = [
    #PATH Core
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('blog/', views.blog, name='blog'),
    path('contact/', views.contact, name='contact'),
    path('sample/', views.sample, name='sample'),
    path('store/', views.store, name='store'),
]
