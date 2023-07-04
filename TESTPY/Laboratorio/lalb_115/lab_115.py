import random

# -*- coding: utf-8 -*-
"""
Bucles

"""
#Ejercicio 1: Trabajo con un bucle while

#Impresión de las reglas del juego

print("Welcome to Guess the Number!")
print("The rules are simple. I will think of a number, and you will try to guess it.")

#generará un número aleatorio entre 1 y 10 mediante el uso de la función randint() del módulo random.
number = random.randint(1,10)

#Monitoree si el usuario adivinó su número con la creación de una variable llamada isGuessRight
isGuessRight = False

#Para gestionar la lógica del juego, cree un bucle while:
while isGuessRight != True:
    guess = input("Guess a number between 1 and 10: ")
    if int(guess) == number:
        print("You guessed {}. That is correct! You win!".format(guess))
        isGuessRight = True
    else:
        print("You guessed {}. Sorry, that isn’t it. Try again.".format(guess))

