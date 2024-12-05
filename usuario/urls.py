from django.urls import path, include
from . import views
from .views import index, taller, Taller_view, perfil, login, perfil_view
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.index, name="index"),
    path('taller/', taller, name='taller'),
    path('talleres/', views.Taller_view, name='taller'),
    path('perfil/', perfil, name='perfil'),
    path('login/', login, name='login'),
    path('logout/', LogoutView.as_view(next_page='index'), name='logout'),
    path('perfiles/', views.perfil_view, name='perfil'),
    
    

    
]
