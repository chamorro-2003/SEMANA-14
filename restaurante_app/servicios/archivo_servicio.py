import json
import os
from typing import List
from modelos.producto import Producto
from modelos.usuario import Usuario


class ArchivoServicio:
    """Encargado de la lectura y escritura de archivos JSON."""

    def __init__(self, carpeta_datos: str = "datos") -> None:
        self.carpeta_datos: str = carpeta_datos
        self.ruta_productos: str = os.path.join(carpeta_datos, "productos.json")
        self.ruta_usuarios: str = os.path.join(carpeta_datos, "usuarios.json")
        self._asegurar_directorio()

    def _asegurar_directorio(self) -> None:
        if not os.path.exists(self.carpeta_datos):
            os.makedirs(self.carpeta_datos)

    def cargar_productos(self) -> List[Producto]:
        productos: List[Producto] = []
        try:
            with open(self.ruta_productos, "r", encoding="utf-8") as f:
                datos = json.load(f)
                for item in datos:
                    productos.append(
                        Producto(
                            producto_id=item["producto_id"],
                            nombre=item["nombre"],
                            precio=item["precio"],
                            categoria=item["categoria"],
                            stock=item.get("stock", 0),
                        )
                    )
        except (FileNotFoundError, json.JSONDecodeError):
            pass
        return productos

    def guardar_productos(self, productos: List[Producto]) -> None:
        """Guarda la lista de productos actualizados."""
        datos = [p.a_diccionario() for p in productos]
        with open(self.ruta_productos, "w", encoding="utf-8") as f:
            json.dump(datos, f, ensure_ascii=False, indent=2)

    def cargar_usuarios(self) -> List[Usuario]:
        usuarios: List[Usuario] = []
        try:
            with open(self.ruta_usuarios, "r", encoding="utf-8") as f:
                datos = json.load(f)
                for item in datos:
                    usuarios.append(
                        Usuario(
                            usuario_id=item["usuario_id"],
                            nombre=item["nombre"],
                            rol=item.get("rol", "Cliente"),
                        )
                    )
        except (FileNotFoundError, json.JSONDecodeError):
            pass
        return usuarios
