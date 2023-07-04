# -*- coding: utf-8 -*-
"""
Listas, tuplas y diccionarios

"""
#Ejercicio 1: Presentar el tipo de dato de lista

#Definición de una lista
#Almacenar una colección de nombres de frutas
myFruitList = ["apple", "banana", "cherry"]
print(myFruitList)
print("tipo de dato de lista: ", type(myFruitList))

#Acceso a una lista por posición
print(myFruitList[0])
print(myFruitList[1])
print(myFruitList[2])

#Modificación de los valores de una lista
#Los valores de una lista se pueden cambiar. En esta actividad, cambiará `cherry` por `orange`.
myFruitList[2] = "orange"
print(myFruitList)


#Ejercicio 2: Presentar el tipo de dato de tupla
#Definición de una tupla
myFinalAnswerTuple = ("apple", "banana", "pineapple")
print("Tupla", myFinalAnswerTuple)
print("Tupla",type(myFinalAnswerTuple))

#Acceso auna tupla por posición
print("Tupla",myFinalAnswerTuple[0])
print("Tupla",myFinalAnswerTuple[1])
print("Tupla",myFinalAnswerTuple[2])

#Ejercicio 3: Presentar el tipo de dato de diccionario
#Definición de un diccionario
myFavoriteFruitDictionary = {
  "Akua" : "apple",
  "Saanvi" : "banana",
  "Paulo" : "pineapple"
}
print(myFavoriteFruitDictionary)
print(type(myFavoriteFruitDictionary))

#Acceso al diccionario por nombre
print(myFavoriteFruitDictionary["Akua"])
print(myFavoriteFruitDictionary["Saanvi"])
print(myFavoriteFruitDictionary["Paulo"])