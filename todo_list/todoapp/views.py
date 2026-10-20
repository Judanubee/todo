from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Todo

# 1. Vista para Listar Tareas (Reemplaza a tu lista principal)
class TodoListView(ListView):
    model = Todo
    template_name = "todo/index.html"
    context_object_name = "todo" # El nombre de la variable que usas en el HTML

# 2. Vista para Crear una Tarea
class TodoCreateView(CreateView):
    model = Todo
    fields = ['titulo', 'descripcion', 'complete'] # Campos del formulario
    success_url = reverse_lazy('todoapp') # A dónde redirigir al guardar

# 3. Vista para Editar una Tarea
class TodoUpdateView(UpdateView):
    model = Todo
    fields = ['titulo', 'descripcion', 'complete']
    template_name = "todo/editar.html" # Tu plantilla para editar
    success_url = reverse_lazy('todoapp')

# 4. Vista para Eliminar una Tarea
class TodoDeleteView(DeleteView):
    model = Todo
    success_url = reverse_lazy('todoapp')