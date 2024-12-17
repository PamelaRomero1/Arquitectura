from django.urls import path, include
from . import views
from .views import index, taller, Taller_view, perfil, login, perfil, logout_view, CustomLogoutView, registro, lista_perfiles, instructor, editar, eliminar_perfil, editar_perfil, LogoutView
from django.contrib.auth.views import LogoutView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name="index"),
    path('taller/', taller, name='taller'),
    path('talleres/', views.Taller_view, name='taller'),
    path('perfil/', perfil, name='perfil'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('instructor/', instructor, name='instructor'),
    path('editar/', editar, name='editar'),
    path('eliminar-perfil/<int:perfil_id>/', views.eliminar_perfil, name='eliminar_perfil'),
    
    path('registro/', registro, name='registro'),
    path('perfiles/', views.lista_perfiles, name='perfil'),
    path('editar-perfil/<int:perfil_id>/', views.editar_perfil, name='editar_perfil'),

    
]
