import random


import math
import random


class Persona:
    def __init__(self):
        # nombre, edad, DNI, sexo (H hombre, M mujer), peso y altura
        self.nombre = ""
        self.edad = 0
        self.DNI = ""
        self.sexo = "H"
        self.peso = 0.0
        self.altura = 0.0

    def calcularIMC(self):
        imc = self.peso / math.pow(self.altura, 2)
        if imc <= 18:
            return -1
        elif imc > 18 and imc <= 25:
            return 0
        elif imc > 25:
            return 1
        else:
            return 10

    def esMayorEdad(self):
        if self.edad >= 18:
            return True
        else:
            return False

    def comprobarSexo(self):
        if self.sexo.upper() != "H" and self.sexo.upper() != "M":
            self.sexo = "H"

    def imprimirInformacion(self):
        print("---------- Información de la Persona ----------")
        print("Nombre:", self.nombre)
        print("Edad:", self.edad)
        print("DNI:", self.DNI)
        print("Sexo:", self.sexo)
        print("Peso:", self.peso)
        print("Altura:", self.altura)
        print("IMC", self.calcularIMC())
        print("Es mayor de edad", self.esMayorEdad())

    def generaDNI(self):
        self.DNI = random.randint(10000000, 99999999)

    def capturarInformacion(self):
        self.nombre = input("Nombre:")
        self.edad = int(input("Edad:"))
        self.sexo = input("Sexo:")
        self.peso = float(input("Peso:"))
        self.altura = float(input("Altura:"))
        self.generaDNI()


o_persona_1 = Persona()

o_persona_1.capturarInformacion()
o_persona_1.imprimirInformacion()

o_persona_2 = Persona()

o_persona_2.capturarInformacion()
o_persona_2.imprimirInformacion()

o_persona_3 = Persona()

o_persona_3.capturarInformacion()
o_persona_3.imprimirInformacion()
