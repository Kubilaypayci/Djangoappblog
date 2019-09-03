from django.contrib import admin
from .models import article, comment
# Register your models here.
admin.site.register(comment)
@admin.register(article)
class articleAdmin(admin.ModelAdmin):
	list_display = ['author','title','created_date']
	search_fields = ['author','content','title']
	list_filter = ['created_date']
	list_display_links = ['title','created_date']
	class Meta:
		model = article
