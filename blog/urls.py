"""
	Author: Kubilay Paycı
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from article import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('hakkimda', views.about, name='about'),
    path('gonderi/', include('article.urls')),
    path('user/', include('user.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)