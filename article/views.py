from django.shortcuts import render,HttpResponse, redirect, get_object_or_404, reverse
from . import forms
from .models import article, comment
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.

def addComment(request,id):
	articles = get_object_or_404(article, id=id)
	if request.method == 'POST':
		comment_author = request.user
		comment_content = request.POST.get('comment_content')
		newComment = comment(comment_author = comment_author, comment_content = comment_content)
		newComment.Article = articles
		newComment.save()
	return redirect(reverse('article:detail', kwargs={'id':id}))

def articlesi(request):
	keyword = request.GET.get('keyword')
	if keyword:
		articles = article.objects.filter(title__contains = keyword)
		return render(request, 'articles/articlesi.html',{'articles':articles})
	
	articles = article.objects.all()
	return render(request, 'articles/articlesi.html',{'articles':articles})

def detail(request, id):
	articles = get_object_or_404(article, id=id)
	comments = articles.comments.all()
	return render(request, 'articles/detail.html', {'article':articles, 'comments':comments})

def index(request):
	return render(request, 'index.html')
	
def about(request):
	return render(request, 'about.html')
	
@login_required(login_url='user:login')
def dashboard(request):
	articles = article.objects.filter(author = request.user)
	context = {
		'articles':articles
	}	
	return render(request, 'articles/dashboard.html', context)

@login_required(login_url='user:login')
def uptadeArticle(request, id):
	values = get_object_or_404(article, id = id)
	form = forms.addArticle(request.POST or None, request.FILES or None, instance=values )		
	if values.author == request.user:
		if form.is_valid():
			values = form.save(commit=False)
			values.author = request.user
			values.save()
			messages.success(request,'Makale Güncellendi')
			idurl = str(values.id)
			idurl = '/gonderi/detay/' + idurl
			
			return redirect(idurl)
	else:
		messages.error(request, 'Güncelleme yetkiniz yok')
		return redirect('article:list')
	context = {
		'form' : form
	}
	return render(request, 'articles/updateArticle.html', context)

@login_required(login_url='user:login')
def addArticle(request):
	form = forms.addArticle(request.POST or None, request.FILES or None )
	
	if form.is_valid():
		article = form.save(commit=False)
		article.author = request.user
		article.save()
		messages.success(request,'Makale Eklendi')
		return redirect('article:list')
	context = {
		'form' : form
	}
	return render(request, 'articles/addArticle.html', context)
	
@login_required(login_url='user:login')
def deleteArticle(request, id):
	articled = get_object_or_404(article, id = id)
	if articled.author == request.user:
		articled.delete()
		messages.warning(request, 'Makale silindi')
		return redirect('article:list')
	else:
		messages.warning(request, 'Silme yetkiniz yok')
		return redirect('article:list')