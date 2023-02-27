from django.shortcuts import render, redirect
from .forms import EmpleadoForm
from .models import Empleado
from django.db.models import Q 
# Create your views here.

def empleado_lista(request):
    queryset = request.GET.get("buscar")
    context = {'empleado_lista' : Empleado.objects.all()}
    if queryset:
        context = {'empleado_lista' : Empleado.objects.filter(
            Q(apellidos__icontains = queryset)   
        ).distinct()
        }
    return render(request, "registro_empleado/empleado_lista.html", context)

def empleado_form(request, id = 0):
    if request.method=='GET':
        if id ==0:
            form = EmpleadoForm()
        else:
            empleado = Empleado.objects.get(pk=id)
            form = EmpleadoForm(instance=empleado)
        return render(request, "registro_empleado/empleado_form.html", {'form':form})
    else:
        if id == 0:
            form = EmpleadoForm(request.POST)
        else:
            empleado = Empleado.objects.get(pk=id)
            form = EmpleadoForm(request.POST,instance = empleado)
        if form.is_valid():
            form.save()
        return redirect('/list')

def empleado_borrar(request, id):
    empleado = Empleado.objects.get(pk=id)
    empleado.delete()
    return redirect('/list')