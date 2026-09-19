<div align="justify">
  
# RESTURANTE_SEMANA_14

# Universidad Estatal Amazonica (UEA)

# Sistema de Gestión de Restaurante - Componentes y Contenedores en Tkinter

**Estudiante:** Nayely Soledad Chamorro Vicente

**Asignatura:** Programación Orientada a Objetos

---

## Descripción General del Sistema

Esta versión corresponde a la evolución de la interfaz gráfica desarrollada en la Semana 13, incorporando nuevos componentes y contenedores de **Tkinter/tt** para mejorar la organización y funcionamiento de la aplicación, además se implementa la gestión de productos mediante operaciones **CRUD**, permitiendo crear, consultar, actualizar y eliminar registros directamente desde la interfaz gráfica, mientras que la información modificada se almacena automáticamente en **productos.json**, de esta manera se mantiene la separación entre la interfaz de usuario y la lógica de negocio administrada por la capa de servicios.

---

## Estructura del Proyecto

La estructura mantiene la organización modular utilizada en las semanas anteriores, donde datos/ conserva la información mediante archivos **JSON**, **modelos/** contiene las entidades **Producto** y **Usuario**, **servicios/** administra la lectura, escritura y reglas de negocio, mientras que **ui/** contiene las vistas gráficas y los componentes utilizados para interactuar con el sistema, finalmente main.py continúa funcionando como punto de entrada y controla la ventana principal de la aplicación.

```text
restaurante_app/
├── datos/
│   ├── productos.json
│   └── usuarios.json
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   └── usuario.py
├── servicios/
│   ├── __init__.py
│   ├── archivo_servicio.py
│   └── restaurante.py
├── ui/
│   ├── __init__.py
│   ├── login_view.py
│   └── main_view.py
├── main.py
└── README.md
```

---
## Componentes Técnicos Aplicados
---

## Componentes y Contenedores de Tkinter

La interfaz gráfica incorpora diferentes componentes de **Tkinter/ttk** para organizar y facilitar la interacción con el usuario, utilizando **ttk.Notebook** para distribuir la información mediante pestañas, **ttk.LabelFrame** para agrupar visualmente los campos y controles, **ttk.Treeview** para mostrar productos y usuarios en forma de tabla, además de **ttk.Entry** para ingresar información y **ttk.Button** para ejecutar las diferentes acciones del sistema, de esta manera los componentes se integran dentro de contenedores que permiten mantener una interfaz ordenada y facilitar el uso de las operaciones disponibles.

---

## Operaciones CRUD de Productos

La gestión de productos permite realizar las operaciones básicas de **Crear**, **Leer**, **Actualizar** y **Eliminar**, donde el usuario puede ingresar los datos de un nuevo producto mediante el formulario y registrarlo en el sistema, posteriormente los productos almacenados pueden visualizarse mediante **Treeview**, además se puede seleccionar un registro para modificar su información o eliminarlo cuando sea necesario, después de cada operación válida los cambios se guardan en **productos.json**, permitiendo que la información se mantenga disponible aunque la aplicación se cierre y vuelva a ejecutarse.

---

## Credenciales y Pruebas Realizadas

Para comprobar el funcionamiento del sistema se utilizaron usuarios registrados en **usuarios.json**, además se mantiene un acceso directo mediante el identificador **admin**, permitiendo utilizar cualquier contraseña no vacía, mientras que para los usuarios registrados se utilizaron las cuentas **1101234567, 1950175750, 1104567890 y 1109876543**, posteriormente se verificó el acceso a la interfaz principal y el funcionamiento de las operaciones **CRUD**, comprobando el registro de nuevos productos, la visualización de información mediante **Treeview**, la actualización y eliminación de registros y la persistencia de los cambios realizados en **productos.json**.

---

## Reflexión Final

La incorporación de nuevos componentes y contenedores en **Tkinter** permite mejorar la organización de la interfaz gráfica y ampliar las funciones del sistema, especialmente mediante la implementación de operaciones **CRUD** que permiten administrar los productos de una manera más interactiva, además la persistencia automática en **JSON** mantiene la información disponible entre diferentes ejecuciones, de esta manera se continúa fortaleciendo la estructura modular de **restaurante_app** y se facilita la integración de nuevas funcionalidades en futuras versiones.

<div>
