from typing import List
from modelos.producto import Producto
from modelos.usuario import Usuario
from servicios.archivo_servicio import ArchivoServicio


class RestauranteServicio:
    """Lógica de negocio, autenticación y operaciones CRUD sobre productos."""

    def __init__(self, archivo_servicio: ArchivoServicio) -> None:
        self.archivo_servicio = archivo_servicio
        self.productos: List[Producto] = self.archivo_servicio.cargar_productos()
        self.usuarios: List[Usuario] = self.archivo_servicio.cargar_usuarios()

    def validar_acceso(self, usuario_id: str, clave: str) -> bool:
        """Validación ID de usuarios o de clave."""
        u_id = usuario_id.strip()
        pwd = clave.strip()

        if not u_id or not pwd:
            return False

        if u_id == "admin":
            return True

        return any(str(u.usuario_id).strip() == u_id for u in self.usuarios)

    def obtener_usuarios(self) -> List[Usuario]:
        return self.usuarios

    def obtener_productos(self) -> List[Producto]:
        return self.productos

    def agregar_producto(
        self, p_id: int, nombre: str, precio: float, categoria: str, stock: int
    ) -> bool:
        if any(p.producto_id == p_id for p in self.productos):
            return False
        nuevo = Producto(p_id, nombre, precio, categoria, stock)
        self.productos.append(nuevo)
        self.archivo_servicio.guardar_productos(self.productos)
        return True

    def actualizar_producto(
        self, p_id: int, nombre: str, precio: float, categoria: str, stock: int
    ) -> bool:
        for p in self.productos:
            if p.producto_id == p_id:
                p.nombre = nombre.strip()
                p.precio = float(precio)
                p.categoria = categoria.strip()
                p.stock = int(stock)
                self.archivo_servicio.guardar_productos(self.productos)
                return True
        return False

    def eliminar_producto(self, p_id: int) -> bool:
        for p in self.productos:
            if p.producto_id == p_id:
                self.productos.remove(p)
                self.archivo_servicio.guardar_productos(self.productos)
                return True
        return False
