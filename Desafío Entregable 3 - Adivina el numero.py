import random
num=0
text=''
cont=1
valor_a_adivinar=random.randint(1,101)

print(''' *************************************
* Juego Adivina el numero *
*************************************
''')
while (text =='') or (text==' '):
    text=input(f' Ingrese su nombre por favor ')

print('¡', text ,' Vamos a adivinar el número! \n debe ser entre 1 y 100, \ny tiene 8 intentos para adivinarlo.')

while True:
    print(cont,'° intento')
    num=(input('Ingrese su número '))
    if (cont == 8):
        break
    if (num=='') or (num==' '):
        cont-=1
        print('No ha ingresado un número, le quedan',(8-cont),' intentos')
    if not (num.isdigit()):
        cont-=1
        print('El numero ingresado no es un número entero, le quedan',(8-cont),' intentos')
    else:
        num=int(num)
        if (num < 1) or (num > 101):
            print('El numero ingresado no esta entre 1 y 100, le quedan',(8-cont),' intentos')
        elif num < valor_a_adivinar:
            print('El numero ingresado es menor al valor a adivinar, le quedan',(8-cont),' intentos')
        elif num > valor_a_adivinar:
            print('El numero ingresado es mayor al valor a adivinar, le quedan',(8-cont),' intentos')
        elif (num == valor_a_adivinar): 
            break
    cont+=1
if (num == valor_a_adivinar) and (cont <= 8):
    print('Excelente has adivinado el numero en el ',cont,'° intento, el valor era el ',valor_a_adivinar)
elif (num != valor_a_adivinar) or (cont == 8):
    print('Lo siento no has podido adivinar \nEl valor era el ',valor_a_adivinar)