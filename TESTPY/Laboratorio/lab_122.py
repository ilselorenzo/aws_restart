# -*- coding: utf-8 -*-
"""
Lab - Cálculo de la carga neta de la insulina mediante listas y bucles de Python
"""

#Cálculo de la carga neta de la insulina mediante listas y bucles de Python

## **Ejercicio 1: Asignación de variables, listas y diccionarios**

# Python3.6
# Coding: utf-8
# Store the human preproinsulin sequence in a variable called preproinsulin:
preproInsulin = "malwmrllpllallalwgpdpaaafvnqhlcgshlvealylvcgergffytpktrreaedlqvgqvelgggpgagslqplalegslqkrgiveqcctsicslyqlenycn"
# Store the remaining sequence elements of human insulin in variables:
lsInsulin = "malwmrllpllallalwgpdpaaa"
bInsulin = "fvnqhlcgshlvealylvcgergffytpkt"
aInsulin = "giveqcctsicslyqlenycn"
cInsulin = "rreaedlqvgqvelgggpgagslqplalegslqkr"
insulin = bInsulin + aInsulin

pKR = {
    'y': 10.07,
    'c': 8.18,
    'k': 10.53,
    'h': 6.00,
    'r': 12.48,
    'd': 3.65,
    'e': 4.25
}

# Ejercicio 2: Uso de count() para contar los números de cada aminoácido
insulin.count("Y")
float(insulin.count("Y"))
seqCount = ({x: float(insulin.count(x)) for x in ['y','c','k','h','r','d','e']})

# ## **Ejercicio 3: Escritura de la fórmula de la carga neta**
pH = 0
while (pH <= 14):
    netCharge = (
    +(sum({x: ((seqCount[x]*(10**pKR[x]))/((10**pH)+(10**pKR[x]))) \
    for x in ['k','h','r']}.values()))
    -(sum({x: ((seqCount[x]*(10**pH))/((10**pH)+(10**pKR[x]))) \
    for x in ['y','c','d','e']}.values())))
    
    print('{0:.2f}'.format(pH), netCharge)
    
    pH +=1
