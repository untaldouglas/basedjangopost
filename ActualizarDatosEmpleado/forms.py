from django import forms
from .models import Empleado

class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = '__all__'

def __init__(self, *args, **kwargs):
    super(EmpleadoForm,self).__init__(*args, **kwargs)
    self.fields['genero'].empty_label = "Seleccionar"
