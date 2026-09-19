import tkinter as tk
from tkinter import ttk, messagebox
from typing import Callable
from servicios.restaurante_servicio import RestauranteServicio


class MainView(ttk.Frame):
    """Panel principal para la gestión del restaurante."""

    def __init__(
        self, parent: tk.Widget, servicio: RestauranteServicio, on_logout: Callable
    ) -> None:
        super().__init__(parent, padding=10)
        self.servicio = servicio
        self.on_logout = on_logout
        self._crear_interfaz()

    def _crear_interfaz(self) -> None:
        # Encabezado
        frame_top = ttk.Frame(self)
        frame_top.pack(fill="x", pady=5)

        ttk.Label(
            frame_top,
            text="Sistema de Gestión de Restaurante",
            font=("Arial", 14, "bold"),
        ).pack(side="left")

        ttk.Button(frame_top, text="Cerrar Sesión", command=self.on_logout).pack(
            side="right"
        )

        # Pestañas principales
        notebook = ttk.Notebook(self)
        notebook.pack(fill="both", expand=True, pady=10)

        tab_productos = ttk.Frame(notebook, padding=10)
        notebook.add(tab_productos, text="Gestión de Productos")
        self._construir_pestana_productos(tab_productos)

        tab_usuarios = ttk.Frame(notebook, padding=10)
        notebook.add(tab_usuarios, text="Consulta de Usuarios")
        self._construir_pestana_usuarios(tab_usuarios)

    def _construir_pestana_productos(self, parent: ttk.Frame) -> None:

        # Formulario
        f_form = ttk.LabelFrame(parent, text=" Formulario de Producto ", padding=10)
        f_form.pack(fill="x", pady=5)

        ttk.Label(f_form, text="ID:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.ent_id = ttk.Entry(f_form, width=8)
        self.ent_id.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(f_form, text="Nombre:").grid(
            row=0, column=2, padx=5, pady=5, sticky="e"
        )
        self.ent_nombre = ttk.Entry(f_form, width=20)
        self.ent_nombre.grid(row=0, column=3, padx=5, pady=5)

        ttk.Label(f_form, text="Precio:").grid(
            row=1, column=0, padx=5, pady=5, sticky="e"
        )
        self.ent_precio = ttk.Entry(f_form, width=8)
        self.ent_precio.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(f_form, text="Categoría:").grid(
            row=1, column=2, padx=5, pady=5, sticky="e"
        )
        self.ent_categoria = ttk.Entry(f_form, width=20)
        self.ent_categoria.grid(row=1, column=3, padx=5, pady=5)

        ttk.Label(f_form, text="Stock:").grid(
            row=0, column=4, padx=5, pady=5, sticky="e"
        )
        self.ent_stock = ttk.Entry(f_form, width=8)
        self.ent_stock.grid(row=0, column=5, padx=5, pady=5)

        # Botones
        f_botones = ttk.Frame(parent)
        f_botones.pack(fill="x", pady=5)

        ttk.Button(f_botones, text="Registrar", command=self._registrar_prod).pack(
            side="left", padx=5
        )
        ttk.Button(f_botones, text="Actualizar", command=self._actualizar_prod).pack(
            side="left", padx=5
        )
        ttk.Button(f_botones, text="Eliminar", command=self._eliminar_prod).pack(
            side="left", padx=5
        )
        ttk.Button(f_botones, text="Limpiar Campos", command=self._limpiar_campos).pack(
            side="left", padx=5
        )

        # Tabla
        f_tabla = ttk.LabelFrame(parent, text=" Productos Registrados ", padding=10)
        f_tabla.pack(fill="both", expand=True, pady=5)

        self.tabla_prod = ttk.Treeview(
            f_tabla,
            columns=("ID", "Nombre", "Precio", "Categoría", "Stock"),
            show="headings",
        )
        self.tabla_prod.heading("ID", text="ID")
        self.tabla_prod.heading("Nombre", text="Nombre")
        self.tabla_prod.heading("Precio", text="Precio ($)")
        self.tabla_prod.heading("Categoría", text="Categoría")
        self.tabla_prod.heading("Stock", text="Stock")

        self.tabla_prod.column("ID", width=50, anchor="center")
        self.tabla_prod.column("Nombre", width=180)
        self.tabla_prod.column("Precio", width=70, anchor="e")
        self.tabla_prod.column("Categoría", width=110)
        self.tabla_prod.column("Stock", width=60, anchor="center")

        self.tabla_prod.pack(fill="both", expand=True)
        self.tabla_prod.bind("<<TreeviewSelect>>", self._seleccionar_producto)

        self._cargar_tabla_productos()

    def _cargar_tabla_productos(self) -> None:
        for row in self.tabla_prod.get_children():
            self.tabla_prod.delete(row)
        for p in self.servicio.obtener_productos():
            self.tabla_prod.insert(
                "",
                "end",
                values=(
                    p.producto_id,
                    p.nombre,
                    f"{p.precio:.2f}",
                    p.categoria,
                    p.stock,
                ),
            )

    def _registrar_prod(self) -> None:
        try:
            p_id = int(self.ent_id.get().strip())
            nombre = self.ent_nombre.get().strip()
            precio = float(self.ent_precio.get().strip())
            categoria = self.ent_categoria.get().strip()
            stock = int(self.ent_stock.get().strip())

            if not nombre or not categoria:
                messagebox.showwarning("Atención", "Complete todos los campos.")
                return

            if self.servicio.agregar_producto(p_id, nombre, precio, categoria, stock):
                self._cargar_tabla_productos()
                self._limpiar_campos()
                messagebox.showinfo("Éxito", "Producto registrado correctamente.")
            else:
                messagebox.showerror("Error", "El ID de producto ya existe.")
        except ValueError:
            messagebox.showerror(
                "Error", "Asegúrese de ingresar ID, Precio y Stock válidos."
            )

    def _actualizar_prod(self) -> None:
        try:
            p_id = int(self.ent_id.get().strip())
            nombre = self.ent_nombre.get().strip()
            precio = float(self.ent_precio.get().strip())
            categoria = self.ent_categoria.get().strip()
            stock = int(self.ent_stock.get().strip())

            if self.servicio.actualizar_producto(
                p_id, nombre, precio, categoria, stock
            ):
                self._cargar_tabla_productos()
                self._limpiar_campos()
                messagebox.showinfo("Éxito", "Producto actualizado correctamente.")
            else:
                messagebox.showerror(
                    "Error", "No existe un producto registrado con ese ID."
                )
        except ValueError:
            messagebox.showerror(
                "Error", "Asegúrese de que los datos numéricos sean válidos."
            )

    def _eliminar_prod(self) -> None:
        try:
            p_id = int(self.ent_id.get().strip())
            if self.servicio.eliminar_producto(p_id):
                self._cargar_tabla_productos()
                self._limpiar_campos()
                messagebox.showinfo("Éxito", "Producto eliminado correctamente.")
            else:
                messagebox.showerror("Error", "No se encontró un producto con ese ID.")
        except ValueError:
            messagebox.showerror("Error", "Ingrese un ID de producto válido.")

    def _seleccionar_producto(self, event) -> None:
        item = self.tabla_prod.focus()
        if item:
            val = self.tabla_prod.item(item, "values")
            self.ent_id.delete(0, tk.END)
            self.ent_id.insert(0, val[0])
            self.ent_nombre.delete(0, tk.END)
            self.ent_nombre.insert(0, val[1])
            self.ent_precio.delete(0, tk.END)
            self.ent_precio.insert(0, val[2])
            self.ent_categoria.delete(0, tk.END)
            self.ent_categoria.insert(0, val[3])
            self.ent_stock.delete(0, tk.END)
            self.ent_stock.insert(0, val[4])

    def _limpiar_campos(self) -> None:
        self.ent_id.delete(0, tk.END)
        self.ent_nombre.delete(0, tk.END)
        self.ent_precio.delete(0, tk.END)
        self.ent_categoria.delete(0, tk.END)
        self.ent_stock.delete(0, tk.END)

    def _construir_pestana_usuarios(self, parent: ttk.Frame) -> None:
        f_tabla = ttk.LabelFrame(
            parent, text=" Lista de Usuarios Registrados ", padding=10
        )
        f_tabla.pack(fill="both", expand=True)

        tabla_usr = ttk.Treeview(
            f_tabla, columns=("ID", "Nombre", "Rol"), show="headings"
        )
        tabla_usr.heading("ID", text="Cédula / ID")
        tabla_usr.heading("Nombre", text="Nombre Completo")
        tabla_usr.heading("Rol", text="Rol de Usuario")

        tabla_usr.column("ID", width=120, anchor="center")
        tabla_usr.column("Nombre", width=220)
        tabla_usr.column("Rol", width=100, anchor="center")

        tabla_usr.pack(fill="both", expand=True)

        for u in self.servicio.obtener_usuarios():
            tabla_usr.insert("", "end", values=(u.usuario_id, u.nombre, u.rol))
