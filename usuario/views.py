from django.shortcuts import render, get_object_or_404
from .models import Taller, Perfil
from django.contrib.auth.decorators import login_required
from django import forms
from django.shortcuts import redirect
from django.http import HttpResponse




def index(request):
    return render(request, 'index.html')

def taller(request): 
    return render(request, 'taller.html')

def Taller_view(request):
    talleres = Taller.objects.all()
    #import pdb; pdb.set_trace()  # Pausa aquí para inspeccionar 'talleres'
    return render(request, 'taller.html', {'talleres': talleres})

def perfil(request):
    return render(request, 'perfil.html')

def login(request):
    return render(request, 'login.html')

class PerfilForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ['nombre', 'apellido', 'fecha_nacimiento', 'direccion', 'telefono', 'email']

def perfil_view(request):
    # Asegúrate de que el usuario esté autenticado
    if request.user.is_authenticated:
        # Obtén el perfil asociado al usuario actual
        perfiles = get_object_or_404(Perfil, usuario=request.user)
        return render(request, 'perfil.html', {'perfiles': perfiles})
    else:
        # Redirigir a la página de login si no está autenticado
        return redirect('login') 

def logout_view(request):
    logout(request)
    return redirect('login')
