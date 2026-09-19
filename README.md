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
│   ├── usuarios.json
│   ├── ventas.json
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   ├── usuario.py
│   └── venta.json
├── servicios/
│   ├── __init__.py
│   ├── archivo_servicio.py
│   └── restaurante.py
├── main.py
└── README.md
```

---
## Componentes Técnicos Aplicados
---

## Mejoras de Rendimiento

Para mejorar la velocidad de las operaciones, se incorporaron estructuras auxiliares en el archivo **restaurante.py**, por lo que el diccionario _indice_productos permite encontrar productos directamente mediante su **ID**, mientras que **_indice_usuarios** facilita la búsqueda de usuarios, además, **_indice_ventas_usuario** organiza las ventas según el usuario para consultar su historial sin recorrer todas las ventas, finalmente, los conjuntos **_ids_productos** y **_ids_usuarios** permiten comprobar rápidamente si un **ID** ya existe, evitando así registros duplicados y reduciendo recorridos innecesarios.

---

## Sincronización de Colecciones

Las estructuras auxiliares deben mantenerse actualizadas para que siempre coincidan con las listas principales, por esta razón, cuando el sistema inicia y recupera la información desde los archivos **JSON**, se ejecuta **_reconstruir_indices()** para volver a crear los índices en memoria, posteriormente, cada vez que se registra un **producto**, **usuario** o **venta**, la información se incorpora tanto a las colecciones principales como a los índices correspondientes, garantizando que las búsquedas y validaciones trabajen con información actualizada durante toda la ejecución.

---

## Persistencia y Pruebas

Para comprobar las mejoras implementadas se inició el sistema con información previamente almacenada y se verificó que los productos y usuarios pudieran localizarse rápidamente mediante sus identificadores, posteriormente, se realizaron varias ventas para un mismo usuario y se consultó su historial utilizando el índice correspondiente, además, se intentó registrar productos y usuarios con **IDs** existentes para comprobar que los conjuntos rechazaran los duplicados, finalmente, se realizó una venta exitosa y se verificó que el stock se actualizara correctamente tanto en memoria como en **productos.json**, mientras que la nueva transacción quedara registrada en **ventas.json**.

---

## Reflexión Final

La incorporación de diccionarios y conjuntos demuestra que la elección adecuada de las estructuras de datos puede mejorar considerablemente el funcionamiento de una aplicación, ya que permiten realizar búsquedas, validaciones y consultas de manera más eficiente sin modificar la estructura principal del sistema, de esta manera, las listas continúan siendo útiles para almacenar la información y mantener la persistencia, mientras que los índices auxiliares optimizan las operaciones más frecuentes, logrando un sistema más rápido, organizado y preparado para trabajar con una mayor cantidad de datos.

<div>
