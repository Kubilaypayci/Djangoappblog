from django.shortcuts import render, redirect
from . import forms
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate,logout
from django.contrib import messages
# Create your views here.

def logouta(request):
	logout(request)
	messages.success(request,'Çıkış yaptınız')
	return redirect('user:login')
	
def register(request):
	
	form = forms.Register(request.POST or None )
	if form.is_valid():
		try:
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			newUser = User(username=username)
			newUser.set_password = password
			newUser.save()
			login(request, newUser)
			messages.success(request, 'Başarıyla Kayıt Oldun')
			return redirect('index')
		except:
			messages.warning(request, 'Bu kullanıcı adı mevcut')
			context = {
				'form' : form,
			}
	
			return render(request, 'user/register.html', context)
	
	context = {
		'form' : form,
	}
	
	return render(request, 'user/register.html', context)
	
def logina(request):
	form = forms.Login(request.POST or None)
	context = {
		'form' : form
	}
	
	if form.is_valid():
		username = form.cleaned_data.get('username')
		password = form.cleaned_data.get('password')
		user = authenticate(username=username,password=password)
		if user is None:
			messages.warning(request,'Kullanıcı adı veya parola hatalı!')
			return render(request, 'user/login.html', context)
		messages.success(request,'Başarıyla giriş yaptınız')
		login(request, user)
		return redirect('index')
	return render(request, 'user/login.html',context)
	
