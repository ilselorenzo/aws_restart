# -*- coding: utf-8 -*-
"""
Tipo de datos de cadena

"""
#Ejercicio 1: Presentar el tipo de dto de cadena
myString = "This is a string."
print(myString)

print("tipo de dato", type(myString))

print("convertir el valor de retorno del tipo en una cadena", (myString + " is of the data type " + str(type(myString))))

#Ejercicio 2: Trabajar con concatenación de cadenas
firstString = "water"
secondString = "fall"
thirdString = firstString + " " + secondString
print("concatenación de cadenas", thirdString)

#Ejercicio 3: Trabajar con cadenas de entrada
name = input("What is your name? ")
print(name)

#Ejercicio 4: Dar formato a las cadenas de salida
#Creará una encuesta y enviará la información recopilada de vuelta al usuario.
color = input("What is your favorite color?  ")
animal = input("What is your favorite animal?  ")
print("{}, you like a {} {}!".format(name,color,animal))
