from django import forms
from .models import Employess

class EmployessForm(forms.ModelForm):
    class Meta:
        model = Employess
        fields = ['name', 'DNI', 'birthdate', 'email', 'phone']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'DNI': forms.NumberInput(attrs={'class': 'form-control'}),
            'birthdate': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone': forms.NumberInput(attrs={'class': 'form-control'}),
        }
    def clean_DNI(self):
        dni = self.cleaned_data.get('DNI', '')
        if len(str(dni)) < 10:
            raise forms.ValidationError("La cédula debe tener al menos 10 dígitos.")
        return dni

    def clean_phone(self):
        phone = self.cleaned_data.get('phone', '')
        if len(str(phone)) < 10:
            raise forms.ValidationError("El teléfono debe tener al menos 10 dígitos.")
        return phone
    
    def clean_birthdate(self):
        birthdate = self.cleaned_data.get('birthdate')
        if not birthdate:
            raise forms.ValidationError("La fecha de nacimiento es obligatoria.")
        return birthdate