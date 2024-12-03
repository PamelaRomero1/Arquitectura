from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Taller(models.Model):
    categoria = models.CharField(max_length=100)
    tipo = models.CharField(max_length=100)
    nombreTaller = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    horario1 = models.CharField(max_length=20)
    profesor = models.CharField(max_length=100)

    def __str__(self):
        return self.nombreTaller

class Perfil(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name='perfil')  # Relación con el modelo User
    nombre = models.CharField(max_length=255, null=True, blank=True)
    apellido = models.CharField(max_length=255, null=True, blank=True)
    fecha_nacimiento = models.DateField(null=True, blank=True)  # Ejemplo de campo adicional
    direccion = models.CharField(max_length=255, null=True, blank=True)
    telefono = models.CharField(max_length=20, null=True, blank=True)
    email = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f"Perfil de {self.usuario.username}"

# Signal para crear el perfil automáticamente cuando se crea un usuario
@receiver(post_save, sender=User)
def crear_perfil(sender, instance, created, **kwargs):
    if created:
        Perfil.objects.create(usuario=instance)  # Crea un perfil vacío para el usuario recién registrado

# Signal para guardar el perfil cada vez que el usuario se guarda
@receiver(post_save, sender=User)
def guardar_perfil(sender, instance, **kwargs):
    instance.perfil.save()  # Guarda el perfil cuando el usuario se guarda
