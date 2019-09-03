from django import forms
from . import models

class addArticle(forms.ModelForm):
	class Meta:
		model = models.article
		fields = ['title','content','image']