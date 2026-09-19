import tkinter as tk
from servicios.archivo_servicio import ArchivoServicio
from servicios.restaurante_servicio import RestauranteServicio
from ui.login_view import LoginView
from ui.main_view import MainView


class AplicacionPrincipal:
    """Controla la ventana principal y los cambios entre vistas."""

    def __init__(self) -> None:
        self.root = tk.Tk()
        self.root.title("Sistema de Gestión de Restaurante")
        self.root.geometry("700x520")

        # Inicialización de servicios
        self.archivo_servicio = ArchivoServicio()
        self.restaurante_servicio = RestauranteServicio(self.archivo_servicio)

        # Vistas
        self.login_view = LoginView(
            self.root, self.restaurante_servicio, self.mostrar_main
        )
        self.main_view = MainView(
            self.root, self.restaurante_servicio, self.mostrar_login
        )

        self.mostrar_login()

    def mostrar_login(self) -> None:
        self.main_view.pack_forget()
        self.login_view.pack(fill="both", expand=True)

    def mostrar_main(self) -> None:
        self.login_view.pack_forget()
        self.main_view.pack(fill="both", expand=True)

    def ejecutar(self) -> None:
        self.root.mainloop()


if __name__ == "__main__":
    app = AplicacionPrincipal()
    app.ejecutar()
