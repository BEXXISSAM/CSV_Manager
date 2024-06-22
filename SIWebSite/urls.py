from django.contrib import admin
from django.urls import path, include
from SIWebSite import views

urlpatterns = [
    # path('upload/', views.import_and_upload, name='upload'),
    path('', views.home, name='home'),
    path('search/', views.search, name='search'),
    path('upload/', views.upload_file, name='upload'),

]
