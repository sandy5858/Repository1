from . import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('', views.index, name='home'),
    path('bloodTips', views.bloodTips, name='bloodTips'),
    path('reg', views.reg, name='reg'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('about', views.about, name='about'),
    path('donate', views.donate, name='donate'),
]
