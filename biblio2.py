from dataclasses import dataclass

from datetime import datetime


class IDError(Exception):
	pass
class LibroNoRegistradoError(Exception):
	pass
class FechaInvalidaError(Exception):
	pass
class LibroNoEncontradoError(Exception):
	pass	
class LibroNoDisponibleError(Exception):
	pass
RegistroUsuarios=[]

class Usuario():
	__id_usuarios={}
	def __init__(self,nombre:str,id:str):
		self.__nombre=nombre.upper().strip()
		self.__id=id.upper().strip()

		try:
			if self.ValidarID(self.__id,Usuario.__id_usuarios):
				Usuario.__id_usuarios[self.__id]=nombre
				if self.__class__.__name__=="Lector":
					print("Usuario registrado")
			else:
				raise IDError(f"El ID '{self.__id}' ya está registrado.\n")
		except IDError as e:
			print(f"Error {e}")

	def get_nombre(self):
		return self.__nombre

	def get_id(self):
		return self.__id

	@staticmethod
	def ValidarID(algo,contenedor):
		return algo not in contenedor

	@classmethod
	def contar_usuarios(cls):
		return len(cls.__id_usuarios)

	def __str__(self):
		return f"Nombre de usuario '{self.__nombre}', ID de usuario '{self.__id}'."

	def __repr__(self):
		return f"Usuario(nombre={self.__nombre},ID={self.__id})"

@dataclass
class Lector(Usuario):

	def __init__(self, nombre: str, id: str):
		super().__init__(nombre, id)
		self._LibrosEnUso=[]

	@property
	def LibrosEnUso(self):
		return self._LibrosEnUso

	@LibrosEnUso.setter
	def PrestarLibros(self,libro):
		self._LibrosEnUso.append(libro)
		print("Libro registrado como prestamo.")

	def DevolverLibro(self,libro):
		try:
			if not libro in self._LibrosEnUso:
				raise LibroNoRegistradoError("El libro no está en uso.")
			else:
				self._LibrosEnUso.remove(libro)
				libro.GestionLibro=True
				print("Libro devuelto")
		
		except LibroNoRegistradoError as e:
			print(f"Error: {e}")
	

class Administrador(Usuario):

	_InventarioLibrosDisponibles=[]

	@staticmethod
	def AgregarLibro(inventario,libro):
		inventario.append(libro)
		print("Libro agregado.")

	@staticmethod
	def EliminarLibro(inventario,libro):
		inventario.remove(libro)
		print("Libro Eliminado")

	@classmethod
	def ContarLibros(cls):
		return len(Administrador._InventarioLibrosDisponibles)


class LectorAdministrador(Lector,Administrador):
	pass

class Libro():
	_InventarioLibros=[]
	def __init__(self,titulo:str,autor:str,codigo:str,disponible:bool=True):
		self.titulo=titulo
		self.autor=autor
		self.codigo=codigo
		self.__disponible=disponible
		Libro._InventarioLibros.append(self)

	@property
	def EstadoDisponibilidad(self):
		return self.__disponible

	@EstadoDisponibilidad.setter
	def GestionLibro(self,estado):
		self.__disponible=estado

	@classmethod
	def TotalLibros(cls):
		return len(_InventarioLibros)

	@classmethod
	def MostrarLibros(cls):
		for i in cls._InventarioLibros:
			print(i)

	def __str__(self):
		disponibilidad = "Disponible" if self.__disponible else "Prestado"
		return f"El título del libro es '{self.titulo}', su autor '{self.autor}',\
		\nsu código '{self.codigo}', y su estado es '{disponibilidad}'."

	def __repr__(self):
		disponibilidad = "Disponible" if self.__disponible else "Prestado"
		return f"Título='{self.titulo}';autor='{self.autor}',código='{self.codigo}',estado='{disponibilidad}'."

class Prestamo():

	RegistroPrestamos=[]

	@classmethod
	def HacerPrestamo(cls,libro,usuario):
		aux=False
		try:

			for j in Libro._InventarioLibros:
				if j.titulo==libro:
					aux=True
					if j.EstadoDisponibilidad:
						fecha=input("Ingresa fecha de devolución con el siguiente formato 'dd/mm/aaaa': ")
						if Prestamo.ValidarFecha(fecha):
							j.GestionLibro=False
							usuario.PrestarLibros=j
							hoy=datetime.today().strftime("%d%m%Y")
							Prestamo.RegistroPrestamos.append([j,hoy,fecha,usuario])
					else:
						raise LibroNoDisponibleError("Libro no disponible.")

			if aux==False:
				raise LibroNoEncontradoError("Libro no encontrado en el inventario.")

		except LibroNoEncontradoError as e:
			print(e)

		except LibroNoDisponibleError as e:
			print(e)


	@staticmethod
	def ValidarFecha(fecha):
	    try:
	        fechaSalida = datetime.strptime(fecha, "%d/%m/%Y")
	        fechaValidar = int(fechaSalida.strftime("%Y%m%d"))
	        fechaHoy = int(datetime.today().strftime("%Y%m%d"))

	        if fechaValidar <= fechaHoy:
	            raise FechaInvalidaError("Error. La fecha debe ser futura.")
	        return True

	    except FechaInvalidaError as e:
	        print(f"{e}")
	        return False

	    except ValueError:
	        print("Ingrese la fecha en su formato correcto (dd/mm/aaaa).")
	        return False
    
	def RetornoLibro(self,libro,usuario):
		libro.GestionLibro(True)
		usuario.DevolverLibro(libro)

admin=Administrador("ADMIN","ADMIN1")
adminlector=LectorAdministrador("LECTORADMIN","LECTOR")
user1=Lector("PEPE","ABC123")
user2=Lector("PEPE","ABC453")
RegistroUsuarios.append(user1)
RegistroUsuarios.append(user2)

libro1 = Libro("DON QUIJOTE", "MIGUEL DE CERVANTES", "L001")
libro2 = Libro("CIEN AÑOS DE SOLEDAD", "GABRIEL GARCÍA MÁRQUEZ", "L002")
libro3 = Libro("EL ALEPH", "JORGE LUIS BORGES", "L003")
libro4 = Libro("LA CASA DE LOS ESPÍRITUS", "ISABEL ALLENDE", "L004")


print("***GESTOR BIBLIOTECA V.0.0.0.001 BY LAD.PYTHON INDUSTRIES***\n")


while True:
	print("***MENU GESTOR BIBLIOTECA V.0.0.0.001***\n")
	print("OPCIONES:")
	print("1.-REGISTRAR USUARIO LECTOR")
	print("2.-ACCEDER COMO USUARIO LECTOR")
	print("3.-ACCEDER COMO ADMINISTRADOR")
	print("4.-ACCEDER COMO LECTOR/ADMINISTRADOR")
	print("5.-VER USUARIOS REGISTRADOS")
	print("6.-MIRAR BIBLIOTECA")
	print("7.-SALIR")

	opciones=input("INGRESE SELECCIÓN: ")

	match opciones:

		case "1":
			print("\nMENU REGISTRO USUARIO LECTOR")
			nombre=input("Ingrese nombre de usuario: ").upper().strip()
			id=input("Ingrese ID de usuario: ").upper().strip()
			usuariolector=Lector(nombre,id)
			RegistroUsuarios.append(usuariolector)

		case "2":
			while True:

				print("\nMENU USUARIO LECTOR")
				print("OPCIONES:")
				print("1.-VER LIBROS EN USO")
				print("2.-GENERAR PRESTAMO")
				print("3.-DEVOLVER LIBRO")
				print("4.-SALIR")

				menu=input("INGRESE SELECCIÓN: ")
				match menu:
					case "1":
						ingresoUsuario=input("Ingrese ID: ").upper()
						aux=False
						for i in RegistroUsuarios:
							if i.get_id()==ingresoUsuario:
								if i.__class__.__name__=="Lector":
									aux=True
									if i.LibrosEnUso:
										for j in i.LibrosEnUso:
											print(j)
									else:
										print("No hay libros registrados.\n")
						if aux==False:
							print("Error-ID incorrecto o ID no pertenece a lector.\n")

					case "2":
						print("\nMENU PRESTAMO LIBRO")
						ingresoUsuario=input("Ingrese ID: ").upper()
						aux=False
						for i in RegistroUsuarios:
							if i.get_id()==ingresoUsuario:
								if i.__class__.__name__=="Lector":
									aux=True
									libroselect=input("Ingresa título del libro: ").upper().strip()
									Prestamo.HacerPrestamo(libroselect,i)
						if aux==False:
							print("Error-ID incorrecto o ID no pertenece a lector.\n")

					case "3":
						print("\nMENU DEVOLVER LIBRO")
						ingresoUsuario=input("Ingrese ID: ").upper()
						aux=False
						aux1=False
						for i in RegistroUsuarios:
							if i.get_id()==ingresoUsuario:
								if i.__class__.__name__=="Lector":
									aux=True
									libroselect=input("Ingresa título del libro: ").upper().strip()
									for j in Libro._InventarioLibros:
										if j.titulo==libroselect:
											i.DevolverLibro(j)
											aux1=True
									if aux1==False:
										print("Libro no existe en el inventario.")

						if aux==False:
							print("Error-ID incorrecto o ID no pertenece a lector.\n")

					case "4":
						break

					case _:
						print("OK")


		

		case "3":
			while True:
				print("\nMENU ADMINISTRADOR")
				print("OPCIONES")
				print("1.-AGREGAR LIBRO")
				print("2.-ELIMINAR LIBRO")
				print("3.-SALIR")

				menu=input("INGRESE SELECCIÓN: ")

				match menu:
					case "1":
						print("\nMENU AGREGAR LIBRO")
						print("*POR DEFECTO LOS LIBROS AGREGADOS QUEDAN COMO DISPONIBLES*")
						titulo=input("INGRESE TÍTULO: ").upper().strip()
						autor=input("INGRESE AUTOR: ").upper().strip()
						codigo=input("INGRESE CÓDIGO: ").upper().strip()
						libronuevo=Libro(titulo,autor,codigo)
						print("LIBRO CREADO")

					case "2":
						print("\nMENU ELIMINAR LIBRO")
						aux=False
						titulo=input("INGRESA TITULO: ").upper().strip()
						for i in Libro._InventarioLibros:
							if i.titulo==titulo:
								aux=True
								Administrador.EliminarLibro(Libro._InventarioLibros,i)
						if aux==False:
							print("LIBRO NO ENCONTRADO.")


					case "3":
						break

					case _:
						print("I DON'T UNDERSTAND")

		case "4":
			pass

		case "5":
			print("USUARIOS REGISTRADOS\n")
			print("***************")
			for i in RegistroUsuarios:
				print(i)
			print("***************\n")

		case "6":
			print("INVENTARIO DE LIBROS\n")
			print("***************")
			for i in Libro._InventarioLibros:
				print(i)
			print("***************\n")


		case "7":
			print("\nEL PROGRAMA SE CERRARÁ")
			print("***DESARROLLADO POR LAD.PYTHON INDUSTRIES***")
			break
		case _:
			print("INGRESE OPCIÓN VÁLIDA\n")


# Clase 6: Prestamo
# Descripción: Gestiona los préstamos de libros. Cada préstamo debe registrar qué
# lector tomó el libro, qué libro fue prestado, la fecha de préstamo y la fecha
# de devolución.
# Propiedades:
# Gestionar las fechas de préstamo y devolución utilizando propiedades
# para asegurar que las fechas sean válidas (por ejemplo, la fecha de
# devolución no puede ser anterior a la fecha de préstamo).
# Métodos:
# Métodos de instancia para manejar las operaciones de préstamo, como
# registrar un préstamo o devolver un libro.
# Excepciones Personalizadas
# 1. LibroNoDisponibleError:
# Descripción: Esta excepción se debe lanzar cuando un lector intenta
# tomar un libro que ya está prestado.
# 2. LibroNoEncontradoError:
# Descripción: Se lanza cuando se intenta buscar o gestionar un libro que
# no está registrado en el sistema.
# Manejo de Archivos
# 1. Guardar y cargar libros:
# Los libros deben almacenarse en un archivo de texto para persistir la
# información entre sesiones.
# Se debe implementar una función para cargar los datos de los libros
# desde el archivo al iniciar el sistema.
# 2. Registro de préstamos:
# Los préstamos deben registrarse en un archivo de texto para mantener un
# historial de los libros prestados y quién los ha tomado.
# Tareas del Grupo
# 1. Gestionar libros:
# El administrador debe poder agregar y eliminar libros utilizando métodos
# estáticos.
# Implementar un método de clase para contar cuántos libros están
# disponibles en la biblioteca.
# 2. Préstamos de libros:
# El lector debe tomar y devolver libros utilizando métodos de instancia.
# Implementar propiedades en la clase Libro para manejar el estado de los
# libros (disponible o prestado).
# 3. Cargar y guardar archivos:
# El sistema debe cargar y guardar los datos de los libros y préstamos en
# archivos de texto.
# 4. Herencia múltiple:
# La clase LectorAdministrador debe ser capaz de gestionar tanto la
# administración de libros como los préstamos.
# 5. Excepciones:
# Crear y utilizar excepciones personalizadas para capturar errores cuando
# los libros no están disponibles o no se encuentran.