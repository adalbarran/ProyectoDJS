from django.urls import path, include
from  . import views
from django.conf.urls.static import static
from django.conf import settings 
from django.contrib import admin


urlpatterns = [

  path('', views.index, name='index'),
  



] 

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
