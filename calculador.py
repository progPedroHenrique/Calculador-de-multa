#import

from time import sleep
import datetime

#functions

def calc(velocity):
	return (velocity * 7) - 80

#vars

velocityUser = None

#console

print("-=-" * 19)

print("Gopher ------ 2021")

print("-=-" * 19)

print("\n")

print("-=-" * 19)

print("Calculador de multa")

print("-=-" * 19)

while (True):
	USERinputOne = input("(1).Calcular (2).Sobre (3).Sair\nDigite: ")

	if (USERinputOne == "1"):
		idCar = input("Insira a placa do veiculo: ")
		velocityUser = float(input("\n\nInsira a velocidade do veiculo: "))
		print("\n\nCalculando...")
		calc(velocityUser)
		sleep(3)

		if (velocityUser <= 80):
			print("O veiculo com a placa {} nao está multado.\nTenha um bom dia e dirija com seguranca.".format(idCar))
		else:
			print("MULTADO! O veiculo com placa {} está MULTADO.\nPreco: {:.2F}\nTenha um bom dia, dirija com seguranca.".format(idCar, velocityUser))

	if(USERinputOne == "2"):
		print("\nEste programa é para calcular multa de velocidade acima de 80 km/h.\n")

	if(USERinputOne == "3"):
		break
