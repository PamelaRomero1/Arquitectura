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
