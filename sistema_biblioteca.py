import json
import datetime
from tkinter import messagebox, simpledialog

class SistemaBiblioteca:
    def __init__(self):
        self.libros = self.cargar_datos('libros.json')
        self.socios = self.cargar_datos('socios.json')
        self.prestamos = self.cargar_datos('prestamos.json')

    def registrar_libro(self):
        titulo = simpledialog.askstring("Registrar Libro", "Título del libro:")
        if not titulo: return
        autor = simpledialog.askstring("Registrar Libro", "Autor del libro:")
        if not autor: return
        editorial = simpledialog.askstring("Registrar Libro", "Editorial del libro:")
        if not editorial: return
        anio_publicacion = simpledialog.askinteger("Registrar Libro", "Año de publicación del libro:")
        if not anio_publicacion: return
        genero = simpledialog.askstring("Registrar Libro", "Género del libro:")
        if not genero: return
        cantidad = simpledialog.askinteger("Registrar Libro", "Cantidad disponible del libro:")
        if not cantidad: return
        
        id_libro = len(self.libros) + 1
        self.libros.append({
            'id': id_libro,
            'titulo': titulo,
            'autor': autor,
            'editorial': editorial,
            'anio_publicacion': anio_publicacion,
            'genero': genero,
            'cantidad': cantidad
        })
        self.guardar_datos(self.libros, 'libros.json')
        messagebox.showinfo("Éxito", "Libro registrado con éxito.")
        
    def editar_libro(self):
        id_libro = simpledialog.askinteger("Editar Libro", "ID del libro:")
        libro = next((libro for libro in self.libros if libro['id'] == id_libro), None)
        if not libro:
            messagebox.showerror("Error", "Libro no encontrado.")
            return

        titulo = simpledialog.askstring("Editar Libro", "Título del libro:", initialvalue=libro['titulo'])
        if not titulo: return
        autor = simpledialog.askstring("Editar Libro", "Autor del libro:", initialvalue=libro['autor'])
        if not autor: return
        editorial = simpledialog.askstring("Editar Libro", "Editorial del libro:", initialvalue=libro['editorial'])
        if not editorial: return
        anio_publicacion = simpledialog.askinteger("Editar Libro", "Año de publicación del libro:", initialvalue=libro['anio_publicacion'])
        if not anio_publicacion: return
        genero = simpledialog.askstring("Editar Libro", "Género del libro:", initialvalue=libro['genero'])
        if not genero: return
        cantidad = simpledialog.askinteger("Editar Libro", "Cantidad disponible del libro:", initialvalue=libro['cantidad'])
        if not cantidad: return

        libro.update({
            'titulo': titulo,
            'autor': autor,
            'editorial': editorial,
            'anio_publicacion': anio_publicacion,
            'genero': genero,
            'cantidad': cantidad
        })
        self.guardar_datos(self.libros, 'libros.json')
        messagebox.showinfo("Éxito", "Libro actualizado con éxito.")

    def eliminar_libro(self):
        id_libro = simpledialog.askinteger("Eliminar Libro", "ID del libro:")
        libro = next((libro for libro in self.libros if libro['id'] == id_libro), None)
        if not libro:
            messagebox.showerror("Error", "Libro no encontrado.")
            return

        confirm = messagebox.askyesno("Confirmar Eliminación", f"¿Está seguro de eliminar el libro '{libro['titulo']}'?")
        if confirm:
            self.libros.remove(libro)
            self.guardar_datos(self.libros, 'libros.json')
            messagebox.showinfo("Éxito", "Libro eliminado con éxito.")

    def registrar_socio(self):
        nombre = simpledialog.askstring("Registrar Socio", "Nombre del socio:")
        if not nombre: return
        apellido = simpledialog.askstring("Registrar Socio", "Apellido del socio:")
        if not apellido: return
        fecha_nacimiento = None
        while not fecha_nacimiento:
            fecha_nacimiento_texto = simpledialog.askstring("Registrar Socio", "Fecha de nacimiento del socio (DD/MM/YYYY):")
            if not fecha_nacimiento_texto: return
            fecha_nacimiento = self.validar_fecha(fecha_nacimiento_texto)
        direccion = simpledialog.askstring("Registrar Socio", "Dirección del socio:")
        if not direccion: return
        correo = simpledialog.askstring("Registrar Socio", "Correo electrónico del socio:")
        if not correo: return
        telefono = simpledialog.askstring("Registrar Socio", "Teléfono del socio:")
        if not telefono: return

        id_socio = len(self.socios) + 1
        self.socios.append({
            'id': id_socio,
            'nombre': nombre,
            'apellido': apellido,
            'fecha_nacimiento': fecha_nacimiento.isoformat(),
            'direccion': direccion,
            'correo': correo,
            'telefono': telefono
        })
        self.guardar_datos(self.socios, 'socios.json')
        messagebox.showinfo("Éxito", "Socio registrado con éxito.")

    def editar_socio(self):
        id_socio = simpledialog.askinteger("Editar Socio", "ID del socio:")
        socio = next((socio for socio in self.socios if socio['id'] == id_socio), None)
        if not socio:
            messagebox.showerror("Error", "Socio no encontrado.")
            return

        nombre = simpledialog.askstring("Editar Socio", "Nombre del socio:", initialvalue=socio['nombre'])
        if not nombre: return
        apellido = simpledialog.askstring("Editar Socio", "Apellido del socio:", initialvalue=socio['apellido'])
        if not apellido: return
        fecha_nacimiento = None
        while not fecha_nacimiento:
            fecha_nacimiento_texto = simpledialog.askstring("Editar Socio", "Fecha de nacimiento del socio (DD/MM/YYYY):", initialvalue=socio['fecha_nacimiento'])
            if not fecha_nacimiento_texto: return
            fecha_nacimiento = self.validar_fecha(fecha_nacimiento_texto)
        direccion = simpledialog.askstring("Editar Socio", "Dirección del socio:", initialvalue=socio['direccion'])
        if not direccion: return
        correo = simpledialog.askstring("Editar Socio", "Correo electrónico del socio:", initialvalue=socio['correo'])
        if not correo: return
        telefono = simpledialog.askstring("Editar Socio", "Teléfono del socio:", initialvalue=socio['telefono'])
        if not telefono: return

        socio.update({
            'nombre': nombre,
            'apellido': apellido,
            'fecha_nacimiento': fecha_nacimiento.isoformat(),
            'direccion': direccion,
            'correo': correo,
            'telefono': telefono
        })
        self.guardar_datos(self.socios, 'socios.json')
        messagebox.showinfo("Éxito", "Socio actualizado con éxito.")

    def eliminar_socio(self):
        id_socio = simpledialog.askinteger("Eliminar Socio", "ID del socio:")
        socio = next((socio for socio in self.socios if socio['id'] == id_socio), None)
        if not socio:
            messagebox.showerror("Error", "Socio no encontrado.")
            return

        confirm = messagebox.askyesno("Confirmar Eliminación", f"¿Está seguro de eliminar al socio '{socio['nombre']} {socio['apellido']}'?")
        if confirm:
            self.socios.remove(socio)
            self.guardar_datos(self.socios, 'socios.json')
            messagebox.showinfo("Éxito", "Socio eliminado con éxito.")
            
    def registrar_prestamo(self):
        id_socio = simpledialog.askinteger("Registrar Préstamo", "ID del socio:")
        if not id_socio: return
        if not any(socio['id'] == id_socio for socio in self.socios):
            messagebox.showerror("Error", "Socio no encontrado.")
            return
        id_libro = simpledialog.askinteger("Registrar Préstamo", "ID del libro:")
        if not id_libro: return
        libro = next((libro for libro in self.libros if libro['id'] == id_libro), None)
        if not libro:
            messagebox.showerror("Error", "Libro no encontrado.")
            return
        if libro['cantidad'] < 1:
            messagebox.showerror("Error", "No hay suficientes copias disponibles para el préstamo.")
            return

        fecha_prestamo = datetime.date.today().isoformat()
        costo = simpledialog.askfloat("Registrar Préstamo", "Costo del préstamo (opcional, ingrese 0 si no aplica):")
        if costo is None: return

        id_prestamo = len(self.prestamos) + 1
        self.prestamos.append({
            'id': id_prestamo,
            'id_socio': id_socio,
            'id_libro': id_libro,
            'fecha_prestamo': fecha_prestamo,
            'costo': costo,
            'fecha_devolucion': None,
            'estado': 'En Curso'
        })
        libro['cantidad'] -= 1
        self.guardar_datos(self.libros, 'libros.json')
        self.guardar_datos(self.prestamos, 'prestamos.json')
        messagebox.showinfo("Éxito", "Préstamo registrado con éxito.")
               
    def devolver_prestamo(self):
        id_prestamo = simpledialog.askinteger("Devolver Préstamo", "ID del préstamo:")
        if not id_prestamo: return
        fecha_devolucion = datetime.date.today().isoformat()

        for prestamo in self.prestamos:
            if prestamo['id'] == id_prestamo:
                prestamo['fecha_devolucion'] = fecha_devolucion
                prestamo['estado'] = 'Devuelto'
                libro = next((libro for libro in self.libros if libro['id'] == prestamo['id_libro']), None)
                if libro:
                    libro['cantidad'] += 1
                self.guardar_datos(self.prestamos, 'prestamos.json')
                self.guardar_datos(self.libros, 'libros.json')
                messagebox.showinfo("Éxito", "Préstamo devuelto con éxito.")
                return
        messagebox.showerror("Error", "Préstamo no encontrado.")
              
    def cargar_datos(self, archivo):
        try:
            with open(archivo, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def guardar_datos(self, datos, archivo):
        with open(archivo, 'w') as f:
            json.dump(datos, f, indent=4)

    def validar_fecha(self, fecha_texto):
        try:
            return datetime.datetime.strptime(fecha_texto, '%d/%m/%Y').date()
        except ValueError:
            messagebox.showerror("Error", "Formato de fecha incorrecto. Use DD/MM/YYYY.")
            return None

    def mostrar_socios(self):
        if not self.socios:
            messagebox.showinfo("Socios", "No hay socios registrados.")
            return

        socios_texto = "\n".join(
            [f"ID: {socio['id']}, Nombre: {socio['nombre']}, Apellido: {socio['apellido']} " for socio in self.socios]
        )
        messagebox.showinfo("Lista de Socios", socios_texto)
        
    def mostrar_libros(self):
        if not self.libros:
            messagebox.showinfo("Libros", "No hay libros registrados.")
            return

        libros_texto = "\n".join(
            [f"ID: {libro['id']}, Titulo: {libro['titulo']}, Cantidad: {libro['cantidad']}" for libro in self.libros]
        )
        messagebox.showinfo("Lista de Libros", libros_texto)

    def buscar_libros(self):
        termino_busqueda = simpledialog.askstring("Buscar Libro", "Buscar libro por titulo, genero, autor o editorial:")
        if not termino_busqueda: return
        resultados = []
        for libro in self.libros:
            if (termino_busqueda.lower() in libro['titulo'].lower() or 
                termino_busqueda.lower() in libro['genero'].lower() or 
                termino_busqueda.lower() in libro['autor'].lower() or 
                termino_busqueda.lower() in libro['editorial'].lower()):
                resultados.append(libro)
        if resultados:
            resultado_texto = "\n".join([f"ID: {libro['id']}, Título: {libro['titulo']}, Autor: {libro['autor']}, Editorial: {libro['editorial']}, Género: {libro['genero']}" for libro in resultados])
            messagebox.showinfo("Resultados de la Búsqueda", resultado_texto)
        else:
            messagebox.showinfo("Resultados de la Búsqueda", "No se encontraron resultados.")
        
    def generar_reporte(self):
        tipo_reporte = simpledialog.askstring("Generar Reporte", "Generar reporte por socio, libro o rango de fechas:")
        if tipo_reporte.lower() == 'socio':
            id_socio = simpledialog.askinteger("Generar Reporte", "ID del socio:")
            if not id_socio: return
            prestamos = [prestamo for prestamo in self.prestamos if prestamo['id_socio'] == id_socio]
            if prestamos:
                reporte_texto = "\n".join([f"ID del préstamo: {prestamo['id']}, ID del libro: {prestamo['id_libro']}, Fecha de préstamo: {prestamo['fecha_prestamo']}, Fecha de devolución: {prestamo.get('fecha_devolucion', 'No devuelto')}, Estado: {prestamo['estado']}" for prestamo in prestamos])
                messagebox.showinfo("Reporte de Préstamos del Socio", reporte_texto)
            else:
                messagebox.showinfo("Reporte de Préstamos del Socio", "No se encontraron préstamos para el socio.")
        elif tipo_reporte.lower() == 'libro':
            id_libro = simpledialog.askinteger("Generar Reporte", "ID del libro:")
            if not id_libro: return
            prestamos = [prestamo for prestamo in self.prestamos if prestamo['id_libro'] == id_libro]
            if prestamos:
                reporte_texto = "\n".join([f"ID del préstamo: {prestamo['id']}, ID del socio: {prestamo['id_socio']}, Fecha de préstamo: {prestamo['fecha_prestamo']}, Fecha de devolución: {prestamo.get('fecha_devolucion', 'No devuelto')}, Estado: {prestamo['estado']}" for prestamo in prestamos])
                messagebox.showinfo("Reporte de Préstamos del Libro", reporte_texto)
            else:
                messagebox.showinfo("Reporte de Préstamos del Libro", "No se encontraron préstamos para el libro.")
        elif tipo_reporte.lower() == 'rango de fechas':
            fecha_inicio = None
            fecha_fin = None
            while not fecha_inicio:
                fecha_inicio_texto = simpledialog.askstring("Generar Reporte", "Fecha de inicio (DD/MM/YYYY):")
                if not fecha_inicio_texto: return
                fecha_inicio = self.validar_fecha(fecha_inicio_texto)
            while not fecha_fin:
                fecha_fin_texto = simpledialog.askstring("Generar Reporte", "Fecha de fin (DD/MM/YYYY):")
                if not fecha_fin_texto: return
                fecha_fin = self.validar_fecha(fecha_fin_texto)
            prestamos = [prestamo for prestamo in self.prestamos if fecha_inicio.isoformat() <= prestamo['fecha_prestamo'] <= fecha_fin.isoformat()]
            if prestamos:
                reporte_texto = "\n".join([f"ID del préstamo: {prestamo['id']}, ID del socio: {prestamo['id_socio']}, ID del libro: {prestamo['id_libro']}, Fecha de préstamo: {prestamo['fecha_prestamo']}, Fecha de devolución: {prestamo.get('fecha_devolucion', 'No devuelto')}, Estado: {prestamo['estado']}" for prestamo in prestamos])
                messagebox.showinfo("Reporte de Préstamos en el Rango de Fechas", reporte_texto)
            else:
                messagebox.showinfo("Reporte de Préstamos en el Rango de Fechas", "No se encontraron préstamos en el rango de fechas.")

        

