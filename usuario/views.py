from django.shortcuts import render, get_object_or_404
from .models import Taller, Perfil
from django.contrib.auth.decorators import login_required
from django import forms
from django.shortcuts import redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.views import LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.db import IntegrityError




def index(request):
    return render(request, 'index.html')


def lista_perfiles(request):
    perfiles = Perfil.objects.all()  # Obtener todos los perfiles de la tabla
    return render(request, 'perfil.html', {'perfiles': perfiles})

def editar(request): 
    return render(request, 'editar.html')

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
def instructor(request):
    return render(request, 'instructor.html')



def logout_view(request):
    logout(request)
    return redirect('login')

class CustomLogoutView(LogoutView):
    def dispatch(self, request, *args, **kwargs):
        messages.success(request, "¡Has cerrado sesión correctamente!")
        return super().dispatch(request, *args, **kwargs)

        
class RegistroForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput())
    email = forms.EmailField()

def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            # Obtener los datos del formulario
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']

            try:
                # Crear el usuario
                user = User.objects.create_user(username=username, password=password, email=email)
                user.is_staff = True  # Asignar como staff, si es necesario
                user.save()

                # Autenticar al usuario
                user = authenticate(request, username=username, password=password)

                if user is not None:
                    # Iniciar sesión con el usuario autenticado
                    

                    # Redirigir a la página principal
                    return redirect('index')
                else:
                    form.add_error(None, 'Hubo un error al autenticar el usuario.')

            except IntegrityError:
                # Si el nombre de usuario ya existe, mostrar un mensaje de error
                form.add_error('username', 'Este nombre de usuario ya está registrado.')

    else:
        form = RegistroForm()

    return render(request, 'registro.html', {'form': form})


def inscribir_taller(request, taller_id):
    # Obtiene el taller que coincide con el ID proporcionado
    taller = get_object_or_404(Taller, id=taller_id)
    
    # Aquí podrías registrar la inscripción del usuario en la base de datos si fuera necesario
    # Por ejemplo, podrías crear un modelo de inscripción para vincular al usuario con el taller
    
    # Envía un mensaje de éxito al usuario
    messages.success(request, f"Te has inscrito correctamente al taller '{taller.nombreTaller}'. Te llegará la información a tu correo electrónico.")
    
    # Redirige a la página de talleres o a la página de perfil, como prefieras
    return redirect('taller')

def eliminar_perfil(request, perfil_id):
    # Obtiene el perfil por ID o lanza un error 404 si no se encuentra
    perfil = get_object_or_404(Perfil, id=perfil_id)
    perfil.delete()  # Elimina el perfil de la base de datos
    return redirect('perfil') 

def editar_perfil(request, perfil_id):
    perfil = get_object_or_404(Perfil, id=perfil_id)  # Obtiene el perfil o lanza error 404
    if request.method == 'POST':
        perfil.nombre = request.POST.get('nombre')
        perfil.apellido = request.POST.get('apellido')
        perfil.fecha_nacimiento = request.POST.get('fecha_nacimiento')
        perfil.direccion = request.POST.get('direccion')
        perfil.telefono = request.POST.get('telefono')
        perfil.email = request.POST.get('email')
        perfil.save()  # Guarda los cambios en la base de datos
        return redirect('nombre_de_tu_vista')  # Cambia 'nombre_de_tu_vista' por la vista a la que deseas redirigir después de la edición
    
    context = {'perfil': perfil}
    return render(request, 'editar_perfil.html', context)
    