import os
import sys
import django
from datetime import date

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portafolio_ing.settings')
django.setup()

from catalogo.models import Producto

proyectos = [
    {
        'nombre': 'Portafolio Personal',
        'descripcion': 'Sitio web personal desarrollado para mostrar mis proyectos y habilidades como estudiante de Ingeniería de Software.',
        'tecnologia': 'HTML/CSS/JS',
        'fecha': date(2024, 10, 1),
        'link': 'https://github.com/vasco140123/portafolio',
    },
    {
        'nombre': 'Manipulación del DOM y Funciones Avanzadas',
        'descripcion': 'Proyecto en JavaScript y TypeScript explorando manipulación del DOM, eventos y funciones avanzadas del lenguaje.',
        'tecnologia': 'JavaScript/TypeScript',
        'fecha': date(2025, 3, 15),
        'link': 'https://github.com/vasco140123/JavaScript-TypeScript-Manipulaci-n-del-DOM-Funciones-Avanzadas',
    },
    {
        'nombre': 'Unificación de Datos Presupuestales',
        'descripcion': 'Sistema de procesamiento y unificación de datos presupuestales, consolidando información de múltiples fuentes.',
        'tecnologia': 'Python',
        'fecha': date(2025, 5, 20),
        'link': 'https://github.com/vasco140123/UNIFICACION-DE-DATOS-PRESUPUESTALES',
    },
    {
        'nombre': 'Geek Dashboard',
        'descripcion': 'Dashboard interactivo con temática geek para visualización de datos e información en tiempo real.',
        'tecnologia': 'JavaScript/CSS',
        'fecha': date(2025, 8, 10),
        'link': 'https://github.com/vasco140123/geek-dashboard',
    },
    {
        'nombre': 'App Web con Django MTV',
        'descripcion': 'Aplicación web fullstack usando Django 5.x con patrón MTV, vistas FBV/CBV, plantillas con herencia y ORM para SQLite.',
        'tecnologia': 'Django/Python',
        'fecha': date(2026, 6, 17),
        'link': 'https://github.com/vasco140123/seman-11-web-funcional-con-Django-5.x',
    },
]

Producto.objects.all().delete()

for p in proyectos:
    obj = Producto.objects.create(**p)
    print(f"Creado: {obj.nombre}")

print(f"\nTotal en BD: {Producto.objects.count()} proyectos")
print("\nConsulta filter (Python):")
for p in Producto.objects.filter(tecnologia__icontains='Python'):
    print(f"  - {p.nombre}")
