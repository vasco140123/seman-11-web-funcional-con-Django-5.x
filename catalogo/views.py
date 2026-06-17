from django.shortcuts import render
from django.views.generic import ListView
from .models import Producto


def home(request):
    context = {
        'nombre': 'Ramos Mercado Vasco Qori',
        'carrera': 'Ingeniería de Sistemas',
        'semestre': 'IX Semestre',
        'descripcion': (
            'Estudiante de Ingeniería de Sistemas con interés en el desarrollo web '
            'fullstack, bases de datos y automatización de procesos. '
            'Actualmente aprendiendo Django, Python y tecnologías web modernas.'
        ),
        'github': 'https://github.com/vasco140123',
    }
    return render(request, 'catalogo/home.html', context)


class CatalogoListView(ListView):
    model = Producto
    template_name = 'catalogo/catalogo.html'
    context_object_name = 'proyectos'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Mis Proyectos'
        return context
