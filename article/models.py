from django.db import models

# Create your models here.

class article(models.Model):
	author = models.ForeignKey('auth.User', on_delete = models.CASCADE, verbose_name = 'Yazar' )
	title = models.CharField(max_length = 60, verbose_name = 'Başlık')
	content = models.TextField(verbose_name = 'İçerik')
	created_date = models.DateTimeField(auto_now_add = True , verbose_name = 'Tarih')
	image = models.ImageField(blank= True, null = True, verbose_name = 'Resim')
	def __str__(self):
		return self.title
	def __iter__(self):
		return [
			self.title,
			self.content,
			self.created_date,
			self.image,
			self.author,
			]
	class Meta:
		ordering = ['-created_date']
class comment(models.Model):
	Article = models.ForeignKey('article.article', on_delete = models.CASCADE, verbose_name = 'Makale' , related_name='comments')
	comment_author = models.CharField(max_length=50, verbose_name='İsim')
	comment_content = models.TextField(max_length=200, verbose_name='Yorum')
	comment_date = models.DateTimeField(auto_now_add=True)
	def __str__(self):
		return self.comment_content
	def __iter__(self):
		return [
			self.Article,
			self.comment_author,
			self.comment_date,
			self.comment_content,
			]
	class Meta:
		ordering = ['-comment_date']