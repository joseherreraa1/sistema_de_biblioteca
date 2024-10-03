import tkinter as tk
from tkinter import ttk
from sistema_biblioteca import SistemaBiblioteca

class VentanaPrincipal(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Sistema de Biblioteca")
        self.geometry("500x700")
        self.sistema_biblioteca = SistemaBiblioteca()
        self.configurar_interfaz()

    def configurar_interfaz(self):
        ttk.Label(self, text="Bienvenido al Sistema de Biblioteca", font=("Helvetica", 16, "bold")).pack(pady=10)

        # Frame para Registros
        frame_registros = ttk.LabelFrame(self, text="Registros")
        frame_registros.pack(pady=10, padx=20, fill=tk.BOTH, expand=True)
        
        ttk.Button(frame_registros, text="Registrar Libro", command=self.sistema_biblioteca.registrar_libro).pack(pady=5, padx=20, fill=tk.X)
        ttk.Button(frame_registros, text="Registrar Socio", command=self.sistema_biblioteca.registrar_socio).pack(pady=5, padx=20, fill=tk.X)
        ttk.Button(frame_registros, text="Registrar Préstamo", command=self.sistema_biblioteca.registrar_prestamo).pack(pady=5, padx=20, fill=tk.X)
        ttk.Button(frame_registros, text="Devolver Préstamo", command=self.sistema_biblioteca.devolver_prestamo).pack(pady=5, padx=20, fill=tk.X)
        
        # Frame para Ediciones
        frame_ediciones = ttk.LabelFrame(self, text="Ediciones")
        frame_ediciones.pack(pady=10, padx=20, fill=tk.BOTH, expand=True)

        ttk.Button(frame_ediciones, text="Editar Libro", command=self.sistema_biblioteca.editar_libro).pack(pady=5, padx=20, fill=tk.X)
        ttk.Button(frame_ediciones, text="Editar Socio", command=self.sistema_biblioteca.editar_socio).pack(pady=5, padx=20, fill=tk.X)

        # Frame para Eliminaciones
        frame_eliminaciones = ttk.LabelFrame(self, text="Eliminaciones")
        frame_eliminaciones.pack(pady=10, padx=20, fill=tk.BOTH, expand=True)

        ttk.Button(frame_eliminaciones, text="Eliminar Libro", command=self.sistema_biblioteca.eliminar_libro).pack(pady=5, padx=20, fill=tk.X)
        ttk.Button(frame_eliminaciones, text="Eliminar Socio", command=self.sistema_biblioteca.eliminar_socio).pack(pady=5, padx=20, fill=tk.X)

        # Frame para Consultas
        frame_consultas = ttk.LabelFrame(self, text="Consultas")
        frame_consultas.pack(pady=10, padx=20, fill=tk.BOTH, expand=True)

        ttk.Button(frame_consultas, text="Mostrar Lista de Socios", command=self.sistema_biblioteca.mostrar_socios).pack(pady=5, padx=20, fill=tk.X)
        ttk.Button(frame_consultas, text="Mostrar Lista de Libros", command=self.sistema_biblioteca.mostrar_libros).pack(pady=5, padx=20, fill=tk.X)
        ttk.Button(frame_consultas, text="Buscar Libro", command=self.sistema_biblioteca.buscar_libros).pack(pady=5, padx=20, fill=tk.X)
        ttk.Button(frame_consultas, text="Generar Reporte", command=self.sistema_biblioteca.generar_reporte).pack(pady=5, padx=20, fill=tk.X)
        
        ttk.Button(self, text="Salir", command=self.quit).pack(pady=10, padx=20, fill=tk.X)

def main():
    app = VentanaPrincipal()
    app.mainloop()

if __name__ == '__main__':
    main()

