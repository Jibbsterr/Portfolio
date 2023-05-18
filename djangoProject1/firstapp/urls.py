from django.urls import path, include
from django.contrib import admin
from . import views

admin.site.site_title = "Jiby's Dashboard"
admin.site.site_header = "Jiby's Portfolio"
admin.site.index_title = "Welcome to Jiby's Dashboard"

urlpatterns=[

 path('', views.index, name='index'),
 path('contact/', views.contact, name='contact'),
 path('about/', views.about, name='about'),
]