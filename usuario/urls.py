from django.urls import path, include
from . import views
from .views import index, taller, Taller_view, perfil, login, perfil_view, perfil, logout_view, CustomLogoutView, registro
from django.contrib.auth.views import LogoutView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name="index"),
    path('taller/', taller, name='taller'),
    path('talleres/', views.Taller_view, name='taller'),
    path('perfil/', perfil, name='perfil'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='index'), name='logout'),
    path('perfil/', views.perfil_view, name='perfil'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('registro/', registro, name='registro'),

    
]
