from django.urls import path, include
from  . import views
from django.conf.urls.static import static
from django.conf import settings 
from django.contrib import admin


urlpatterns = [

  path('', views.index, name='index'),
  
  path('servicios', views.servicios, name='servicios'),
  path('abogados', views.abogados, name='abogados'),

  path("accounts/", include("django.contrib.auth.urls")),
#CRUDSERVICIOS
  path('nuevoser', views.nuevoser, name='nuevoser'),  
  path('gestionser', views.gestionser, name='gestionser'),
  path('editarservicio/<ID_servicio>', views.editarservicio, name='editarservicio'),
  path('borrarservicio/<ID_servicio>', views.borrarservicio, name='borrarservicio'),

  path('logout', views.signout, name='logout'),
  path('login/', views.signin, name='login'),

  #CRUDABOGADOS
  path('nuevoabogado', views.nuevoabogado, name='nuevoabogado'),  
  path('gestionabo', views.gestionabo, name='gestionabo'),
  path('editarabogado/<rut>', views.editarservicio, name='editarabogado'),
  path('borrarabogado/<rut>', views.borrarservicio, name='borrarabogado'),
] 

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
