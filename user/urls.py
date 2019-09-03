from django.contrib import admin
from django.urls import path
from . import views

app_name = 'user'

urlpatterns = [
	path('giris', views.logina, name = 'login'),
	path('kaydol', views.register, name = 'register'),
	path('cikis', views.logouta, name = 'logout')
]