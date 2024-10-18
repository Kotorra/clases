from dataclasses import dataclass

@dataclass
class Vehiculo():
	placa:str
	marca:str

	def __str__(self):
		return f"La marca del vehículo es '{self.marca}' y su placa es '{self.placa}'."

class Automovil(Vehiculo):
	def __init__(self,placa,marca,tarifa=2):
		super().__init__(placa,marca)
		self.tarifa_por_hora=tarifa

	def calcular_tarifa(self,horas):
		return self.tarifa_por_hora*horas

@dataclass
class Motocicleta(Vehiculo):
	tarifa_por_hora:int=1

	def calcular_tarifa(self,horas):
		return self.tarifa_por_hora*horas

class VehiculoNoEncontradoError(Exception):
	pass
class Estacionamiento():
	def __init__(self):
		self.vehiculos=[]

	def RegistrarVehiculo(self,*tuplavehiculos):
		for vehiculo in tuplavehiculos:
			self.vehiculos.append(vehiculo)

	def CalcularTarifa(self):
		aux=False
		SeleccionVehiculo=input("Ingrese la placa del vehículo: ").upper().strip()
		try:
			for vehiculo in self.vehiculos:
				if vehiculo.placa==SeleccionVehiculo:
					horas=float(input("Ingrese tiempo de permanencia del vehiculo: "))
					aux=True
					if Cronos.ValidarTiempo(horas):
						return (vehiculo,horas,(vehiculo.calcular_tarifa(horas)))
			if aux==False:
				raise VehiculoNoEncontradoError("VEHICULO NO REGISTRADO.")
		except VehiculoNoEncontradoError as e:
			print(f"Error {e}")


@dataclass
class Recibo():
	vehiculo:object
	tiempo:float
	total:float

	def __str__(self):
		return (f"El vehículo {(self.vehiculo).marca} estuvo {self.tiempo} horas. El total es ${self.total}.")

class TiempoInvalidoError(Exception):
    pass
@dataclass
class ControlDeTiempo(Automovil,Motocicleta):
	placa:str="XD"
	marca:str="XD"
	def ValidarTiempo(self,tiempo):
		try:
			if tiempo<0:
				raise TiempoInvalidoError("El tiempo no puede ser negativo. Física FAIL.")
			else:
				return True
		except (ValueError,TiempoInvalidoError) as e:
			print(f"Entrada no válida. Revísese. {e}")

Cronos=ControlDeTiempo()
auto1=Automovil("12345","TOYOTA")
auto2=Automovil("XDXDXD","HYUNDAI")
moto1=Motocicleta("ABC567","YAMAHA")
estacionamiento1=Estacionamiento()
estacionamiento1.RegistrarVehiculo(auto1,auto2,moto1)

def registro():
	marca=input("Ingrese marca: ").upper().strip()
	placa=input("Ingrese placa patente: ").upper().strip()
	
	return (marca,placa)

print("***CONTROL DE ESTACIONAMIENTO BY LADPYTHON.INC***")
while True:
	print("\n***CONTROL ESTACIONAMIENTO V.0.1***")
	print("OPCIONES:")
	print("1.-Ver vehiculos registrados.")
	print("2.-Registrar vehículo.")
	print("3.-Mirar tarifa de un vehículo.")
	print("4.-Generar recibo de un vehículo.")
	print("5.-Borrar vehículo registrado.")
	print("6.-Cerrar programa.")
	
	opciones=input("Ingresa opcion elegida: ")

	match opciones:
		case "1":
			print("-----------------------------")
			for vehiculo in estacionamiento1.vehiculos:
				print(vehiculo)
		case "2":
			print("1.-Registrar auto.")
			print("2.-Registrar moto.")
			reg=input("Ingrese opcion: ")
			if reg=="1":
				registro=registro()
				auto=Automovil(registro[1],registro[0])
				estacionamiento1.RegistrarVehiculo(auto)
				print("Nae registrada.")
			elif reg=="2":
				registro=registro()
				moto=Motocicleta(registro[1],[0])
				print("Moto registrada.")
			else:
				print("NOOOOOOO")

		case "3":
			aux=estacionamiento1.CalcularTarifa()
			print(f"La tarifa es ${aux[2]}.")

		case "4":
			aux=estacionamiento1.CalcularTarifa()
			try:
				recibo=Recibo(aux[0],aux[1],aux[2])
				print(recibo)
			except TypeError:
				print("No se pudo generar el recibo.")

		case "5":
			aux=False
			SeleccionVehiculo=input("Ingrese la placa del vehículo: ")
			try:
				for vehiculo in estacionamiento1.vehiculos:
					if vehiculo.placa==SeleccionVehiculo:
						(estacionamiento1.vehiculos).remove(vehiculo)
						print("Vehículo borrado")
						aux=True
				if aux==False:
					raise VehiculoNoEncontradoError("VEHICULO NO REGISTRADO.")
			except VehiculoNoEncontradoError as e:
				print(f"Error {e}")

		case "6":
			print("***DESARROLLADO POR LADPYTHON.INC***")
			break
		case _:
			print("***INGRESE OPCIÓN VALIDA****")

