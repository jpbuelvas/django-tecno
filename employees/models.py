from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Employess(models.Model):
    name = models.CharField(max_length=200)
    DNI = models.CharField(max_length=20)   # en vez de IntegerField
    created = models.DateTimeField(auto_now_add=True)
    birthdate = models.DateField(null=True, blank=True)  # Cambiado a DateField
    email = models.EmailField(max_length=100)  # Cambiado a EmailField
    phone = models.CharField(max_length=20) # en vez de IntegerField
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.name} - {self.user.username}"