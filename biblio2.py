from dataclasses import dataclass,field

from datetime import datetime


class IDError(Exception):
	pass
class LibroNoRegistradoError(Exception):
	pass
class FechaInvalidaError(Exception):
	pass


class Usuario():
	__id_usuarios={}
	def __init__(self,nombre:str,id:str):
		self.__nombre=nombre
		self.__id=id

		try:
			if self.ValidarID(self.__id,Usuario.__id_usuarios):
				Usuario.__id_usuarios[self.__id]=nombre
				print("Usuario creado.")
			else:
				raise IDError(f"El ID '{self.__id}' ya está registrado.")
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

	def __repr__(self):
		return f"Usuario(nombre={self.__nombre},ID={self.__id})"

	def __repr__(self):
		return f"Usuario(nombre={self.__nombre},ID={self.__id})"

@dataclass
class Lector(Usuario):
	#_"DE USO INTERNO"
	_LibrosEnUso:list=field(default_factory=list)

	@property
	def LibrosEnUso(self):
		return self._LibrosEnUso

	@LibrosEnUso.setter
	def PrestarLibros(self,libro):
		if libro in self._LibrosEnUso:
			print("Libro en uso")
		else:
			self._LibrosEnUso.append(libro)
			print("Libro registrado como prestamo.")

	@LibrosEnUso.setter
	def DevolverLibro(self,libro):
		try:
			if libro in self._LibrosEnUso:
				raise LibroNoRegistradoError("El libro no está en uso.")
			else:
				self._LibrosEnUso.remove(libro)
				print("Libro devuelto")
		
		except LibroNoRegistradoError as e:
			print(f"Error: {e}")
	

# user1=Usuario("PEPE","ABC123")
# user2=Usuario("PEPE","ABC453")

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
		return len(Administrador._InventarioLibros)


class LectorAdministrador(Lector,Administrador):
	pass

class Libro():
	_InventarioLibros=[]
	def __init__(titulo:str,autor:str,codigo:str,disponible:bool=True):
		self.titulo=titulo
		self.autor=autor
		self.codigo=codigo
		self.__disponible=disponible

	@property
	def EstadoDisponibilidad(self):
		return self.__disponible

	@EstadoDisponibilidad.setter
	def GestionLibro(self,estado):
		self.__disponible=estado

	@classmethod
	def TotalLibros(cls):
		return len(_InventarioLibros)

	def __str__(self):
		disponibilidad = "Disponible" if self.__disponible else "Prestado"
		return f"El título del libro es '{self.titulo}', su autor '{self.autor}',\
		\nsu código '{self.código}', y su estado es '{disponibilidad}'."

	def __repr__(self):
		disponibilidad = "Disponible" if self.__disponible else "Prestado"
		return f"Título='{self.titulo}';autor='{self.autor}',código='{self.código}',estado='{disponibilidad}'."

class Prestamo():
	# def __init__(self,usuario,libro):
	# 	self.usuario=usuario
	# 	self.libro=libro
	# 	self.fecha=fecha

	def HacerPrestamo(self):
		fecha=input("Ingresa fecha de devolución con el siguiente formato 'dd/mm/aaaa': ")
		if ValidarFecha(fecha):
			libro.GestionLibro(False)
			usuario.PrestarLibros(libro)


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

    def RetornoLibro(self):
			libro.GestionLibro(True)
			usuario.DevolverLibro(libro)

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