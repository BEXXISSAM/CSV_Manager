from django.contrib import admin
from django.urls import path, include
from SIWebSite import views

urlpatterns = [
    path('', views.home, name='home'),
    path('search/', views.search, name='search'),
    path('upload/', views.upload_file, name='upload'),

]
