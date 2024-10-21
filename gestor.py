from dataclasses import dataclass

class ProductoNoEncontradoError(Exception):
	pass
 
class CantidadInsuficienteError(Exception):
	pass
 
class ErrorArchivoInventario(Exception):
	pass
class ErrorEconomia(Exception):
	pass

class ErrorProductoImaginario(Exception):
	pass	

@dataclass
class Producto():
	codigo: str
	nombre: str
	precio: float
	cantidad: int

	def __str__(self):
		return f"Código producto FALSO es {self.codigo}, nombre {self.nombre},\
precio ${self.precio}. Cantidad disponible:{self.cantidad}"

@dataclass
class Libro(Producto):
	autor:str
	editorial:str

	def __str__(self):
		return f"Código libro es {self.codigo}, título {self.nombre},\
precio ${self.precio}. Cantidad disponible:{self.cantidad}"

class Revista(Producto):
	def __init__(self,codigo,nombre,precio,cantidad,nro_ed,fecha_publicacion):
		super().__init__(codigo,nombre,precio,cantidad)
		self.nro_ed=nro_ed
		self.fecha_publicacion=fecha_publicacion
	def __str__(self):
		return f"Código revista es {self.codigo}, título {self.nombre},\
precio ${self.precio}. Cantidad disponible:{self.cantidad}"

class Papeleria(Producto):
	def __str__(self):
		return f"Código artículo papeleria {self.codigo}, título {self.nombre},\
precio ${self.precio}. Cantidad disponible:{self.cantidad}"

class Inventario():
	inventario=[]
	regventas=[]

	def agregar_producto(self):
		aux=False

		def registroLista(producto):
				self.inventario.append(producto)
				print("Producto registrado en el inventario.")

		codigoProducto=input("Ingrese código de producto: ").upper().strip()
		for producto in self.inventario:
			if producto.codigo==codigoProducto:
				print("Producto ya registrado. Si desea modificar, use la otra opción.")
				aux=True

		if aux==False:
			print("***Categorias****")
			print("1.-Libro")
			print("2.-Revista")
			print("3.-Papelería")
			categoria=input("Ingrese el número correspondiente: ")

			match categoria:
				case "1":
					titulo=input("Ingrese título del libro: ")
					try:
						precio=float(input("Ingrese precio del libro: "))
						if precio<=0:
							raise ErrorEconomia("Error precio inválido.")
						cantidad=int(input("Ingrese cantidad: "))
						autor=input("Ingrese autor: ")
						editorial=input("Ingrese editorial: ")
						libro=Libro(codigoProducto,titulo,precio,cantidad,autor,editorial)
						registroLista(libro)

					except (ValueError,ErrorEconomia) as e:
						print(f"Eu macaco {e}")

				case "2":
					titulo=input("Ingrese título de la revista: ")
					try:
						precio=float(input("Ingrese precio de la revista: "))
						cantidad=int(input("Ingrese cantidad: "))
						nro_ed=input("Ingrese número de edición: ")
						fecha_publicacion=input("Ingrese fecha publicacion(día/mes/año): ")
						revista=Revista(codigoProducto,titulo,precio,cantidad,nro_ed,fecha_publicacion)
						registroLista(revista)

					except ValueError:
						print("Póngase serio.")

				case "3":
					nombre=input("Ingrese nombre del artículo: ")
					try:
						precio=float(input("Ingrese precio del artículo: "))
						cantidad=int(input("Ingrese cantidad: "))
						papeleria=Papeleria(codigoProducto,nombre,precio,cantidad)
						registroLista(papeleria)

					except ValueError:
						print("Póngase serio.")

	def eliminar_producto(self):
		aux=False
		codigoProducto=input("Ingrese código de producto: ").upper().strip()
		for producto in self.inventario:
			if producto.codigo==codigoProducto:
				self.inventario.remove(producto)
				print("Producto eliminado.")
				aux=True
				break
		if aux==False:
			print("Producto no encontrado.")

	def modificar_producto(self):
		aux=False
		codigoProducto=input("Ingrese código de producto: ").upper().strip()
		for producto in self.inventario:
			if producto.codigo==codigoProducto:
				aux=True
				print("Producto encontrado.")
				print(f"El producto tiene estas características: \n\
					{producto.__str__()}")
				if producto.__class__.__name__=="Libro":
					print("Seleccione que va a modificar.")
					print("1.-Título")
					print("2.-Precio")
					print("3.-Cantidad")
					print("4.-Autor")
					print("5.-Editorial")
					print("6.-Código de producto")

					mod=input("Ingrese selección: ")

					match mod:
						case "1":
							titulo=input("Ingrese nuevo título: ")
							producto.nombre=titulo
							print("Título modificado.")

						case "2":
							ControlPrecio(producto)

						case "3":

							ControlCantidad(producto)

						case "4":
							autor=input("Ingrese nuevo autor: ")
							producto.autor=autor
							print("Autor modificado.")

						case "5":
							editorial=input("Ingrese nueva editorial: ")
							producto.editorial=editorial
							print("Editorial modificada.")

						case "6":
							codigo=input("Ingrese el nuevo código: ").upper().strip()
							producto.codigo=codigo
							print("Código modificado.")

						case _:
							print("OK")


				elif producto.__class__.__name__=="Revista":
					print("Seleccione que va a modificar.")
					print("1.-Título")
					print("2.-Precio")
					print("3.-Cantidad")
					print("4.-Número de edición")
					print("5.-Fecha publicación")
					print("6.-Código de producto")

					mod=input("Ingrese selección: ")

					match mod:
						case "1":
							titulo=input("Ingrese nuevo título: ")
							producto.nombre=titulo
							print("Título modificado.")

						case "2":
							ControlPrecio(producto)

						case "3":
							ControlCantidad(producto)

						case "4":
							ed=input("Ingrese nuevo número de edición: ")
							producto.nro_ed=ed
							print("Número de edición modificado.")

						case "5":
							fecha=input("Ingrese nueva fecha de publicación(día/mes/año): ")
							producto.fecha_publicacion=fecha
							print("Fecha de publicacion modificada.")

						case "6":
							codigo=input("Ingrese el nuevo código: ").upper().strip()
							producto.codigo=codigo
							print("Código modificado.")

						case _:
							print("OK")

				elif producto.__class__.__name__=="Papeleria":
					print("Seleccione que va a modificar.")
					print("1.-Nombre artículo")
					print("2.-Precio")
					print("3.-Cantidad")
					print("4.-Código de producto")

					mod=input("Ingrese selección: ")

					match mod:
						case "1":
							titulo=input("Ingrese nuevo título: ")
							producto.nombre=titulo
							print("Título modificado.")

						case "2":
							ControlPrecio(producto)

						case "3":

							ControlCantidad(producto)

						case "4":
							codigo=input("Ingrese el nuevo código: ").upper().strip()
							producto.codigo=codigo
							print("Código modificado.")

						case _:
							print("OK")
			
				break

		if aux==False:
			print("Producto no encontrado")


	def registrar_venta(self):
		aux=False
		print("Registro de venta.")
		venta=input("Ingrese código de producto a vender: ").upper().strip()
		for producto in self.inventario:
			if producto.codigo==venta:
				aux=True
				print("Producto encontrado.")
				print(f"Cantidad: {producto.cantidad}")
				cantidad=input("Ingresa las unidades a vender: ")
				if cantidad.isnumeric():
					cantidad=int(cantidad)
					delta=producto.cantidad-cantidad
					try:
						if delta<0:
							raise CantidadInsuficienteError("No hay suficiente stock.")
						else:
							producto.cantidad=producto.cantidad-cantidad
							venta=Venta(producto,cantidad)
							total=venta.calcular_total()
							ventareg=[producto.codigo,producto.nombre,cantidad,total]
							self.regventas.append(ventareg)
							print("Venta registrada")

					except CantidadInsuficienteError as e:
						print(f"Error: {e}")
				else:
					print("Use un número entero positivo.")

				break

						
		if aux==False:
			print("Producto no encontrado.")

	def ControlPrecio(producto):
		try:
			precio=float(input("Ingrese nuevo precio: "))
			if precio<=0:
				raise ErrorEconomia("Error precio inválido.")
			producto.precio=precio
			print("Precio modificado")
		except (ValueError,ErrorEconomia) as e:
			print(f"CUEK {e}")

	def ControlCantidad(producto):
		try:
			cantidad=float(input("Ingrese nuevo precio: "))
			if precio<0:
				raise ErrorProductoImaginario("Error cantidad negativa.")
			producto.cantidad=cantidad
			print("Cantidad modificada.")
		except (ValueError,ErrorProducto) as e:
			print(f"CUEK {e}")

	def guardar_inventario(self):
		with open("inventario.txt", "w", encoding="utf-8") as Archivo:
			Archivo.write("")
		for i in self.inventario:
			if i.__class__.__name__=="Producto":
				string=(f"PRODUCTO;{i.codigo};{i.nombre};{i.precio};{i.cantidad};\n")

			elif i.__class__.__name__=="Libro":
				string=(f"LIBRO;{i.codigo};{i.nombre};{i.precio};{i.cantidad};{i.autor};{i.editorial}\n")

			elif i.__class__.__name__=="Revista":
				string=(f"REVISTA;{i.codigo};{i.nombre};{i.precio};{i.cantidad};{i.nro_ed};{i.fecha_publicacion}\n")

			elif i.__class__.__name__=="Papeleria":
				string=(f"PAPELERIA;{i.codigo};{i.nombre};{i.precio};{i.cantidad};\n")

			with open("inventario.txt", "a", encoding="utf-8") as Archivo:
				Archivo.write(string)

	def cargar_inventario(self):
		with open("inventario.txt","r", encoding="utf-8") as Archivo:
			lineas=Archivo.readlines()
			for i in lineas:
				elementos=i.split(";")

				if elementos[0]=="PRODUCTO":
					producto=Producto(elementos[1],elementos[2],float(elementos[3]),int(elementos[4]))
					self.inventario.append(producto)

				elif elementos[0]=="LIBRO":
					libro=Libro(elementos[1],elementos[2],float(elementos[3]),int(elementos[4]),elementos[5],elementos[6])
					self.inventario.append(libro)

				elif elementos[0]=="REVISTA":
					revista=Revista(elementos[1],elementos[2],float(elementos[3]),int(elementos[4]),elementos[5],elementos[6])
					self.inventario.append(revista)

				elif elementos[0]=="PAPELERIA":
					papeleria=Papeleria(elementos[1],elementos[2],float(elementos[3]),int(elementos[4]))
					self.inventario.append(papeleria)
				else:
					pass

class Venta():
	def __init__(self,producto,cantidad):
		self.producto=Producto
		self.cantidad=cantidad

	def calcular_total(self):
		total=producto.precio*cantidad
		print(f"El total es de ${total}")
		return total

inventario=Inventario()

print("***Gestor Inventario V.01.10 - BY LADPYTHON INDUSTRIES***")

try:
	with open("inventario.txt", "x", encoding="utf-8") as ArchivoInventario:
		pass
	print("Archivo Creado.")

except FileExistsError:
	print("Archivo Encontrado.")

with open("inventario.txt","r+",encoding="utf-8") as ArchivoInventario:
	if ArchivoInventario.readlines()==[]:
		ArchivoInventario.write("PRODUCTO;CODIGO;PRODUCTOINICIAL;999;999;")
		print("Archivo vacío.")
		print("Se ha agregado un producto falso al inventario para que el programa funcione.")

inventario.cargar_inventario()	


while True:
	print("\n*Gestor Inventario V.01.10*")
	print("Menu opciones:")
	print("1.-Mostrar inventario")
	print("2.-Agregar producto")
	print("3.-Modificar producto")
	print("4.-Eliminar producto")
	print("5.-Ingresar venta")
	print("6.-Salir")

	opciones=input("Ingrese opción: ")

	match opciones:

		case "1":
			print("\n***Inventario de productos****")
			for i in inventario.inventario:
				print(i)

		case "2":
			print("\n***Agregar producto****")
			inventario.agregar_producto()
			inventario.guardar_inventario()

		case "3":
			print("\n***Modificar producto****")
			inventario.modificar_producto()
			inventario.guardar_inventario()

		case "4":
			print("\n***Eliminar producto****")
			inventario.eliminar_producto()
			inventario.guardar_inventario()

		case "5":
			print("\n***Ingresar venta***")
			inventario.registrar_venta()

		case "6":
			print("\nEl programa se cerrará.")
			print("****Desarrollado por LAD.PYTHON INDUSTRIES****")
			break

		case _:
			print("\n¿HOLA?")


