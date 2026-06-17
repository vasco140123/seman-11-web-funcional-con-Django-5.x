# Guía Práctica Semana 11 — Aplicación Web con Django 5.x

**Asignatura:** Desarrollo de Aplicaciones Web (IS093A)  
**Unidad:** II — Desarrollo Web Fullstack  
**Apellidos y Nombres:** Ramos Mercado Vasco  
**Fecha:** 17/06/2026  
**Repositorio:** https://github.com/vasco140123/seman-11-web-funcional-con-Django-5.x

---

## Objetivo

Construir una aplicación web funcional con Django 5.x aplicando el patrón MTV (Model-Template-View), configurando enrutamiento con `urls.py`, desarrollando vistas FBV y CBV, implementando plantillas con herencia y filtros, y definiendo modelos con el ORM de Django para persistencia en SQLite.

La aplicación desarrollada es un **portafolio personal** como estudiante de Ingeniería de Software, donde la página principal muestra mi perfil y `/catalogo/` lista mis proyectos académicos reales.

---

## Recursos utilizados

- Python 3.11.9
- Django 5.2.15
- Visual Studio Code con extensiones: Python, Django, SQLite Viewer
- Navegador + DevTools
- GitHub para control de versiones

---

## Estructura del proyecto

```
portafolio_ing/
├── manage.py
├── requirements.txt
├── .gitignore
├── poblar_datos.py
├── portafolio_ing/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── catalogo/
    ├── migrations/
    │   └── 0001_initial.py
    ├── templates/
    │   └── catalogo/
    │       ├── base.html
    │       ├── home.html
    │       └── catalogo.html
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── models.py
    ├── urls.py
    └── views.py
```

---

## Desarrollo paso a paso

### Paso 1 — Entorno virtual, instalación de Django y creación del proyecto

Se creó un entorno virtual para aislar las dependencias del proyecto:

```bash
py -m venv venv
.\venv\Scripts\pip install django
.\venv\Scripts\django-admin startproject portafolio_ing .
.\venv\Scripts\django-admin startapp catalogo
```

La app `catalogo` fue registrada en `INSTALLED_APPS` dentro de `settings.py`.

Se verificó el servidor con `python manage.py runserver` accediendo a `http://127.0.0.1:8000/`.

> 📸 Captura 1: Terminal con comandos de instalación y estructura de carpetas en VS Code  
> 📸 Captura 2: Navegador mostrando la página de inicio de Django en `127.0.0.1:8000`

---

### Paso 2 — Configuración de rutas (urls.py)

Se creó `catalogo/urls.py` mapeando las rutas de la app:

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('catalogo/', views.CatalogoListView.as_view(), name='catalogo'),
]
```

En el `urls.py` del proyecto se usó `include()` para incluir las rutas de la app:

```python
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('catalogo.urls')),
]
```

Los templates usan `{% url 'nombre' %}` para nunca hardcodear URLs.

> 📸 Captura 3: `urls.py` de la app abierto en VS Code con las rutas definidas

---

### Paso 3 — Vistas: FBV y CBV

Se implementó una vista basada en función (`home`) y una basada en clase (`CatalogoListView`):

```python
def home(request):
    context = {
        'nombre': 'Ramos Mercado Vasco',
        'carrera': 'Ingeniería de Software',
        ...
    }
    return render(request, 'catalogo/home.html', context)


class CatalogoListView(ListView):
    model = Producto
    template_name = 'catalogo/catalogo.html'
    context_object_name = 'proyectos'
```

> 📸 Captura 4: `views.py` abierto en VS Code  
> 📸 Captura 5: Navegador en `http://127.0.0.1:8000/` mostrando la página de inicio

---

### Paso 4 — Plantillas con herencia, bloques, tags y filtros

Se creó `base.html` con bloques reutilizables y navbar con `{% url %}`:

```html
{% block title %}...{% endblock %}
{% block content %}...{% endblock %}
```

`catalogo.html` extiende la base y usa tags de Django:

```html
{% extends 'catalogo/base.html' %}
{% for proyecto in proyectos %}
    {% if proyecto.link %}...{% endif %}
    {{ proyecto.nombre|title }}
    {{ proyecto.fecha|date:"d/m/Y" }}
{% endfor %}
```

> 📸 Captura 6: `base.html` y `catalogo.html` abiertos en VS Code  
> 📸 Captura 7: Navegador en `http://127.0.0.1:8000/catalogo/` con el listado de proyectos

---

### Paso 5 — Modelo, migraciones y consultas ORM

Se definió el modelo `Producto` en `catalogo/models.py`:

```python
class Producto(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    tecnologia = models.CharField(max_length=100)
    fecha = models.DateField()
    link = models.URLField(blank=True)

    def __str__(self):
        return self.nombre
```

Se ejecutó la verificación, las migraciones y se pobló la base de datos:

```bash
python manage.py check
python manage.py makemigrations catalogo
python manage.py migrate
python poblar_datos.py
```

Consultas con el ORM:
- `Producto.objects.all()` — retorna todos los proyectos
- `Producto.objects.filter(tecnologia__icontains='Python')` — filtra por tecnología

> 📸 Captura 8: Terminal con `makemigrations` y `migrate` aplicados  
> 📸 Captura 9: SQLite Viewer en VS Code mostrando la tabla `catalogo_producto` con datos  
> 📸 Captura 10: Estructura de carpetas completa en el explorador de VS Code

---

## Evidencias

Las capturas de pantalla de cada paso se encuentran en la carpeta `capturas/` del repositorio.

---

## Cómo ejecutar el proyecto

```bash
# Clonar el repositorio
git clone https://github.com/vasco140123/seman-11-web-funcional-con-Django-5.x.git
cd seman-11-web-funcional-con-Django-5.x

# Crear entorno virtual e instalar dependencias
py -m venv venv
.\venv\Scripts\pip install -r requirements.txt

# Aplicar migraciones
py manage.py migrate

# Poblar datos iniciales
py poblar_datos.py

# Iniciar servidor
py manage.py runserver
```

Acceder a `http://127.0.0.1:8000/`

---

## Conclusiones

- El patrón **MTV** de Django separa claramente el modelo (datos), el template (presentación) y la vista (lógica), lo que facilita el mantenimiento del código.
- Las **FBV** son simples y directas, ideales para vistas sencillas. Las **CBV** reducen código repetitivo al encapsular comportamiento común como el listado de objetos.
- La **herencia de templates** con `{% extends %}` y `{% block %}` permite mantener un diseño consistente sin duplicar HTML.
- El **ORM de Django** abstrae el SQL, permitiendo hacer consultas complejas con sintaxis Python. Los QuerySets son lazy, es decir, solo ejecutan la consulta cuando se necesitan los datos.
- Las **migraciones** permiten versionar los cambios en el esquema de la base de datos de forma controlada.
