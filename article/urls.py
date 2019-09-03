from django.contrib import admin
from django.urls import path
from . import views

app_name = 'article'

urlpatterns = [
	path('panel', views.dashboard, name = 'list'),
	path('ekle', views.addArticle, name = 'addArticle'),
	path('detay/<int:id>', views.detail, name = 'detail'),
	path('guncelle/<int:id>', views.uptadeArticle, name = 'update'),
	path('sil/<int:id>', views.deleteArticle, name = 'delete'),
	path('', views.articlesi, name = 'articles'),
	path('comment/<int:id>', views.addComment, name = 'comment'),

]