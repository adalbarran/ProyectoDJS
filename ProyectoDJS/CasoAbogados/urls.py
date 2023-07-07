from django.urls import path, include
from  . import views
from django.conf.urls.static import static
from django.conf import settings 
from django.contrib import admin


urlpatterns = [

  path('', views.index, name='index'),
  
  path('servicios', views.servicios, name='servicios'),

  path("accounts/", include("django.contrib.auth.urls")),

  path('nuevoser', views.nuevoser, name='nuevoser'),  

  path('gestionser', views.gestionser, name='gestionser'),

  path('editarservicio/<ID_servicio>', views.editarservicio, name='editarservicio'),
  path('borrarservicio/<ID_servicio>', views.borrarservicio, name='borrarservicio'),
] 

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
