from django.shortcuts import render
from .models import Taller, Perfil
from django.contrib.auth.decorators import login_required



def index(request):
    context = {}
    return render(request, 'index.html', context)

def taller(request): 
    return render(request, 'taller.html')

def Taller_view(request):
    talleres = Taller.objects.all()  # Recupera todos los registros
    raise Exception(f"Talleres recuperados: {talleres}")
    return render(request, 'taller.html', {'talleres': talleres})

def perfil(request):
    return render(request, 'perfil.html')

def login(request):
    return render(request, 'login.html')

@login_required
def ver_perfil(request):
    # Obtiene el perfil del usuario autenticado
    perfil = Perfil.objects.get(usuario=request.user)
    return render(request, 'perfil.html', {'perfil': perfil})
