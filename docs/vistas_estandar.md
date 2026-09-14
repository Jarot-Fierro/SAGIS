# Guía de Uso: Vistas Estándar (`StandardViews`)

Esta guía explica cómo utilizar las clases base definidas en `core/standard/views.py` para crear vistas CRUD
consistentes en el proyecto ERP.

## Clases Disponibles

Todas las vistas heredan de `StandardBaseView`, lo que les otorga automáticamente:

- **Protección de Login:** Requieren que el usuario esté autenticado (`LoginRequiredMixin`).
- **Filtrado por Establecimiento:** Si el modelo tiene un campo `establecimiento`, los resultados se filtran
  automáticamente según el establecimiento del usuario (a menos que sea superusuario).
- **Filtrado de Actividad:** Solo muestra registros donde `is_active=True` o `activo=True` si dichos campos existen en
  el modelo.

---

## 1. `StandardListView` (Listado)

Se usa para mostrar una tabla con los registros del modelo.

### Atributos Clave:

- `search_fields`: Lista de campos por los que se puede buscar (por defecto `['name']`).
- `list_url_name`: Nombre de la URL para el listado (para redirecciones).
- `create_url_name`: Nombre de la URL para crear un nuevo registro.
- `update_url_name`: Nombre de la URL para editar.
- `delete_url_name`: Nombre de la URL para desactivar/eliminar.

### Ejemplo de uso:

```python
from core.standard.views import StandardListView
from .models import Producto

class ProductoListView(StandardListView):
    model = Producto
    template_name = 'productos/list.html'
    title = 'Listado de Productos'
    module_name = 'Inventario'
    search_fields = ['nombre', 'codigo']
    list_url_name = 'productos:list'
    create_url_name = 'productos:create'
    update_url_name = 'productos:update'
    delete_url_name = 'productos:delete'
```

---

## 2. `StandardCreateView` (Creación)

Maneja el formulario de creación.

### Características Automáticas:

- Asigna el `establecimiento` del usuario actual al objeto.
- Asigna el usuario actual al campo `created_by` si existe.
- Muestra un mensaje de éxito tras la creación.

### Ejemplo de uso:

```python
from core.standard.views import StandardCreateView
from .models import Producto
from .forms import ProductoForm

class ProductoCreateView(StandardCreateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'productos/form.html'
    success_url = reverse_lazy('productos:list')
    title = 'Crear Producto'
    module_name = 'Inventario'
    list_url_name = 'productos:list'
```

---

## 3. `StandardUpdateView` (Edición)

Similar a la de creación, pero para editar registros existentes.

### Características Automáticas:

- Asigna el usuario actual al campo `updated_by` si existe.
- Muestra un mensaje de éxito tras la actualización.

### Ejemplo de uso:

```python
from core.standard.views import StandardUpdateView
from .models import Producto
from .forms import ProductoForm

class ProductoUpdateView(StandardUpdateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'productos/form.html'
    success_url = reverse_lazy('productos:list')
    title = 'Editar Producto'
    module_name = 'Inventario'
    list_url_name = 'productos:list'
```

---

## 4. `StandardDetailView` (Detalle en Modal)

Diseñada para ser visualizada en un modal, extrayendo campos automáticamente.

### Ejemplo de uso:

```python
from core.standard.views import StandardDetailView
from .models import Producto

class ProductoDetailView(StandardDetailView):
    model = Producto
    title = 'Detalles del Producto'
    module_name = 'Inventario'
    exclude_fields = ['id', 'created_at'] # Campos a ocultar
```

---

## 5. Función `catalogo_desactivar`

Para desactivaciones lógicas mediante peticiones POST.

### Ejemplo en `urls.py`:

```python
from core.standard.views import catalogo_desactivar
from .models import Producto

path('productos/<int:pk>/desactivar/', 
     lambda r, pk: catalogo_desactivar(r, pk, Producto, 'productos:list'), 
     name='delete'),
```
