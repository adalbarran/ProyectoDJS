from django.urls import path, include
from  . import views
from django.conf.urls.static import static
from django.conf import settings 
from django.contrib import admin
from django.contrib.auth import views as auth_views


urlpatterns = [

  path('', views.index, name='index'),
  path('abogados', views.abogados, name='abogados'),
  path('casos', views.casos, name='casos'),
  path('contact/', views.contact, name='contact'),
  path('contact_success/', views.contact, name='contact'),

  path("accounts/", include("django.contrib.auth.urls")),
  path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
#CRUDSERVICIOS
  path('nuevocaso', views.nuevocaso, name='nuevocaso'),
  path('gestioncasos', views.gestioncasos, name='gestioncasos'),
  path('editarcaso/<int:ID_caso>', views.editarcaso, name='editarcaso'),
  path('borrarcaso/<int:ID_caso>', views.borrarcaso, name='borrarcaso'),

  path('register/', views.register_view, name='register'),
  path('logout/', views.logout_view, name='logout'),
  path('login/', views.login_user, name='login'),
  
  #CRUDABOGADOS
  path('nuevoabogado', views.nuevoabogado, name='nuevoabogado'),  
  path('gestionabo', views.gestionabo, name='gestionabo'),
  path('editarabogado/<rut>', views.editarabogado, name='editarabogado'),
  path('borrarabogado/<rut>', views.borrarabogado, name='borrarabogado'),
] 

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
