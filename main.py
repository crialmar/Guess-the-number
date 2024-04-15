'''PRIMERO: input para preguntar al usuario el nombre y dar la respuesta 
SEGUNDO: usar librería Random y usar randint()
TERCERO: plantear el match con los cuatro casos
CUARTO: cálculo de los intentos'''

from random import randint

name_user = input("¿Cuál es tu nombre?: ")

print(f'Bueno, {name_user}, he pensado un número entre 1 y 100, y tienes solo ocho intentos para adivinar cuál crees que es el número')

number_python = randint(1,100)

try_user = 0
number_user = 0
while try_user < 8:
    number_user = int(input("Dime un número: "))
    
    if number_user < 1 and number_user > 100:
        try_user += 1
        print("No es un valor válido 😡")
    elif number_user < number_python:
        try_user += 1
        print("Tu número es menor al mio 😄")
    elif number_user > number_python:
        try_user += 1
        print("Tu número es mayor al mío 😁")
    else:
        print(f"Muy bien, has ganado!!!🎉🪅 Te ha llevado {try_user} intentos" )
        break 


if try_user < 8:
    print(input(number_user))
if try_user == 8:
    print(f"He ganado jejej 😈 El número era: {number_python}")