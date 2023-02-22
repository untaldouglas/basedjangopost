from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.empleado_form, name='empleado_insertar'),
    path('<int:id>/', views.empleado_form, name='empleado_actualizar'),
    path('delete/<int:id>/', views.empleado_borrar, name = 'empleado_borrar'),
    path('list/', views.empleado_lista, name='empleado_lista')
]