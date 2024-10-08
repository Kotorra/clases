class Libro():
	def __init__(self,tituloLibro,autorLibro,idLibro):
		self.__tituloLibro=tituloLibro.upper()
		self.__autorLibro=autorLibro.upper()
		self.__idLibro=idLibro
		self.__estadoDeUso=False
	def mostrarLibro(self):
		print(f"Título: {self.__tituloLibro} - Autor: {self.__autorLibro}")
		print("----------------------------------------")
	def get_id(self):
		return self.__idLibro

	def get_titulo(self):
		return self.__tituloLibro

	def get_estadoLibro(self):
		return self.__estadoDeUso

	def set_gestionEstado(self,estado):
		self.__estadoDeUso=estado



class Usuario():
	def __init__(self,nombre,idUsuario):
		self.__nombre=nombre.upper()
		self.__idUsuario=idUsuario
		self.librosEnUso=[]

	def mostrarLibrosUsuario(self):
		if (len(self.librosEnUso)==0):
			print(f"El usuario {self.__nombre} no tiene libros en uso.")
		else:
			print(f"El usuario {self.__nombre} tiene los siguientes libros en uso:")
			for i in self.librosEnUso:
				print(i.get_titulo())
	
	def get_idUsuario(self):
		return self.__idUsuario

	def get_nombre(self):
		return self.__nombre
	def agregar_libro(self,libro):
		self.librosEnUso.append(libro)

class Prestamo():
	def __init__(self):
		self.auxError=False

	def prestarLibro(self):
		print("Estás usando la gestión de préstamo de libros.")
		libroGestion=input("Ingresa el libro que vas a solicitar: ").upper()
		for libro in listaLibros:
			if libro.get_titulo()==libroGestion:
				if libro.get_estadoLibro()==False:
					print("El libro está seleccionado y disponible para préstamo.")
					self.auxError=True
					nombreUsuario=input("Ingrese el nombre del Usuario: ").upper()
					for usuario in listaUsuarios:
						if usuario.get_nombre()==nombreUsuario:
							libro.set_gestionEstado(True)
							usuario.agregar_libro(libro)
							print("Libro prestado y asociado al usuario")
						else:
							print("Usuario no encontrado.")
		
		if self.auxError==False:
			print("Libro no encontrado.")
		self.auxError=False
	def devolverLibro(self):
		pass


prestador=Prestamo()


class Creador():
	def crearLibro(self):
		error=False
		print("Estás registrando un libro.")
		titulo=input("Ingresa el título del libro: ")
		autor=input("Ingresa el autor del libro: ")
		idRegistroLibro=input("Ingresa el ID del libro: ")

		for i in listaLibros:
			if i.get_id()==idRegistroLibro:
				print("Choque de ID de libros, ERROR ERROR")
				error=True

		if error!=True:
			libro=Libro(titulo,autor,idRegistroLibro)
			listaLibros.append(libro)
			print("Libro registrado exitosamente.\n")
	def crearUsuario(self):
		error=False
		print("Estás creando un usuario.")
		nombre=input("Ingresa el nombre del usuario: ")
		id=input("Ingresa el ID del usuario: ")
		for i in listaUsuarios:
			if i.get_idUsuario()==id:
				print("Choque de ID - ID Registrado - ERROR ERROR")
				error=True
		if error==False:
			usuarioNuevo=Usuario(nombre,id)
			listaUsuarios.append(usuarioNuevo)
			print("Usuario registrado exitosamente")


creadorMagico=Creador()


libro1=Libro("La peste","Albert Camus","1234")
libro2=Libro("Noches Blancas","Fiodor Dostoievski","fjfdsaf")
libro3=Libro("El extranjero","Albert Camus","1j3fjasf")
libro4=Libro("El túnel","Ernesto Sábato","wejfajaf")

usuario1=Usuario("Canelita","chicheñol")

listaLibros=[libro1,libro2,libro3,libro4]
listaUsuarios=[usuario1]

print("Bienvenidos a la biblioteca 'El Saber'.")
while True:
	print("Library Software 0.0.0.1 - 'El Saber' \nMenú de opciones: ")
	print("1.- Mostrar libros.")
	print("2.- Crear Usuario.")
	print("3.- Crear registro de un libro nuevo.")
	print("4.- Prestar un libro.")
	print("5.- Devolver un libro.")
	print("6.- Cerrar programa")

	opcion=input("Ingresa la opción: ")

	if opcion=="6":
		print("El programa se despide")
		print("Desarrollado por LadPython INC.")
		break

	elif opcion=="1":
		print("Los libros disponibles son: ")
		for i in listaLibros:
			if i.get_estadoLibro()==False:
				print(i.get_titulo())
		print("Los libros ya prestados son: ")
		for i in listaLibros:
			if i.get_estadoLibro()==True:
				print(i.get_titulo())

	elif opcion=="2":
		creadorMagico.crearUsuario()

	elif opcion=="3":
		creadorMagico.crearLibro()

	elif opcion=="4":
		prestador.prestarLibro()

	elif opcion=="5":
		

	else:
		print("Revísate")
