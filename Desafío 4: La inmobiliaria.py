#Semana 4: Funciones, Módulos e Introducción a git
'''Desafío 4: La inmobiliaria
Requisitos técnicos:
- Operadores.
- Estructuras de datos.
- Estructuras de control de flujo.
- Funciones
Una inmobiliaria de tu ciudad solicita un sistema para automatizar la gestión de sus inmuebles.
Se te pide construir un programa que permita:
-Agregar, editar y eliminar inmuebles a la lista.
Las funciones deben ajustarse al formato de lista y reglas de validación.
-Cambiar el estado de un inmueble, sin modificar sus demás datos.
Las funciones deben ajustarse al formato de lista y reglas de validación.
-Hacer búsqueda de inmuebles en función de un presupuesto dado.
    La función recibirá como entrada la lista de inmuebles y un precio, y devolverá otra lista con
    los inmuebles cuyo precio sea menor o igual que el dado y el estado sea Disponible o
    Reservado. Los inmuebles de la lista que se devuelva deben incorporar un nuevo par a cada
    diccionario con el precio del inmueble, donde el precio de un inmueble se calcula con las
    reglas de precio en función de la zona.
Formato de lista
[{'año': 2010, 'metros': 150, 'habitaciones': 4, 'garaje': True, 'zona': 'C', 'estado': 'Disponible'},
{'año': 2016, 'metros': 80, 'habitaciones': 2, 'garaje': False, 'zona': 'B', 'estado': 'Reservado'},
{'año': 2000, 'metros': 180, 'habitaciones': 4, 'garaje': True, 'zona': 'A', 'estado': 'Disponible'},
{'año': 2015, 'metros': 95, 'habitaciones': 3, 'garaje': True, 'zona': 'B', 'estado': 'Vendido'},
{'año': 2008, 'metros': 60, 'habitaciones': 2, 'garaje': False, 'zona': 'C', 'estado': 'Disponible'}]
Reglas de validación
-Inmuebles solo de zona: A, B o C.
-Inmuebles con estado: Disponible, Reservado o Vendido.
-No opera con inmuebles:
    -Anteriores al año 2000.
    -Menores de 60 metros cuadrados.
    -Menores de 2 habitaciones.
Reglas de precio
Zona A: precio = (metros x 100 + habitaciones x 500 + garaje x 1500) x (1 - antigüedad / 100)
Zona B: precio = (metros x 100 + habitaciones x 500 + garaje x 1500) x (1 - antigüedad / 100) x 1.5
Zona C: precio = (metros x 100 + habitaciones x 500 + garaje x 1500) x (1 - antigüedad / 100) x 2
'''
import os
import time
import datetime

##### Limpiar Pantalla ######################################

# Para Unix/Linux/MacOS/BSD
if os.name == "posix":
    limpiar = "clear"
# Para DOS/Windows
elif os.name == "ce" or os.name == "nt" or os.name == "dos":
    limpiar = "cls"
#############################################################


anio_actual=2023

inmuebles=[
{'año': 2010, 'metros': 150, 'habitaciones': 4, 'garaje': True, 'zona': 'C', 'estado': 'Disponible'},
{'año': 2016, 'metros': 80, 'habitaciones': 2, 'garaje': False, 'zona': 'B', 'estado': 'Reservado'},
{'año': 2000, 'metros': 180, 'habitaciones': 4, 'garaje': True, 'zona': 'A', 'estado': 'Disponible'},
{'año': 2015, 'metros': 95, 'habitaciones': 3, 'garaje': True, 'zona': 'B', 'estado': 'Vendido'},
{'año': 2008, 'metros': 60, 'habitaciones': 2, 'garaje': False, 'zona': 'C', 'estado': 'Disponible'}
]
reglas_D_validacion={
'zona':['A','B','C'],
'estados' : ['DISPONIBLE', 'RESERVADO', 'SEÑADO', 'PAGADO', 'ENTREGADO'],
'inmueble_condiciones_minimas':{
'anio':2000,
'metros':60,
'habitaciones':2
}
}
def validar_zona(zona):
    if zona in reglas_D_validacion['zona']:
        return True
    else:
        return False

def validar_estado(estado):
    if estado in reglas_D_validacion['estados']:
        return True
    else:
        return False

def validar_anio(anio):
    if anio >= reglas_D_validacion['inmueble_condiciones_minimas']['anio']:
        return True
    else:
        return False
    
def validar_metros(metros):
    if metros >= reglas_D_validacion['inmueble_condiciones_minimas']['metros']:
        return True
    else:
        return False

def validar_habitaciones(habitaciones):
    if habitaciones >= reglas_D_validacion['inmueble_condiciones_minimas']['habitaciones']:
        return True
    else:
        return False
def ingreso_datos_inmueble():
    inmueble={}
    anio=input('ingrese el año del inmueble formato aaaa ')
    anio=int(anio)
    metros=input('ingrese los metros del inmueble ')
    metros=int(metros)
    habitaciones=input('ingrese cantidad de habitaciones del inmueble ')
    habitaciones=int(habitaciones)
    garage_in=input('¿tiene garage? ingrese S o N ')
    garage_in=garage_in.upper()
    if garage_in == 'S':
        garage=True
    else:
        garage=False
    zona=input('ingrese zona ')
    zona=zona.upper()
    estado=input('ingrese estado: DISPONIBLE, RESERVADO, SEÑADO, PAGADO, ENTREGADO ')
    estado=estado.upper()
    inmueble={'año': anio, 'metros': metros, 'habitaciones': habitaciones, 'garaje': garage, 'zona': zona, 'estado': estado}
    return (inmueble)

def carga_inmueble(*args):
    inmueble={}
    anio=input('ingrese el año del inmueble formato aaaa ')
    anio=int(anio)
    metros=input('ingrese los metros del inmueble ')
    metros=int(metros)
    habitaciones=input('ingrese cantidad de habitaciones del inmueble ')
    habitaciones=int(habitaciones)
    garage_in=input('¿tiene garage? ingrese S o N ')
    garage_in=garage_in.upper()
    if garage_in == 'S':
        garage=True
    else:
        garage=False
    zona=input('ingrese zona ')
    zona=zona.upper()
    estado=input('ingrese estado: DISPONIBLE, RESERVADO, SEÑADO, PAGADO, ENTREGADO ')
    estado=estado.upper()
    if (validar_anio('anio'))and(validar_habitaciones('habitaciones'))and(validar_metros('metros')):
        inmueble={'año': anio, 'metros': metros, 'habitaciones': habitaciones, 'garaje': garage, 'zona': zona, 'estado': estado}
        agregar_inmueble(inmueble)
        listar_inmueble()
        return print('Inmueble agregado')
    else:
        return print('inmueble no cumple requisitos para ser agregado')
    
def precio(**kwargs):
    precio=(kwargs['metros'] * 100 + kwargs['habitaciones'] * 500 + kwargs['garaje']*1500) * (1-((anio_actual-kwargs['anio']))/100)
    if kwargs['zona']=='A':
        return precio
    elif kwargs['zona']=='B':
        return precio *1.5
    elif kwargs['zona']=='C':
        return precio*2
    

def listar_inmueble():
    for inmueble in inmuebles:
        print(f'{inmuebles.index(inmueble)+1} - {inmueble}\n')
         
def agregar_inmueble(*args):
    inmuebles.append(args)
    return True
def editar_inmueble(*args):
    if  menu_edicion=='1':
        #dato_a_modificar=int(dato_a_modificar)
        inmuebles['anio':int(dato_a_modificar)]
    elif menu_edicion=='2':
        #dato_a_modificar=int(dato_a_modificar)
        args['metros':int(dato_a_modificar)]
    elif menu_edicion=='3':
        #dato_a_modificar=int(dato_a_modificar)
        args['habitaciones':int(dato_a_modificar)]
    elif menu_edicion=='4':
        #dato_a_modificar=bool(dato_a_modificar)
        args['garage':bool(dato_a_modificar)]
    elif menu_edicion=='5':
        #dato_a_modificar=dato_a_modificar.upper()
        args['zona':dato_a_modificar.upper()]
    elif menu_edicion=='6':
        #dato_a_modificar=dato_a_modificar.upper()
        args['estado':dato_a_modificar.upper()]
        return True
    else:
        return False

def eliminar_inmueble(*args):
     inmuebles.pop(args)
     return True
################################################################################################################
while True:

            menu_principal = input('''
                *************************************
                *   1 - Inmuebles                   *
                *   2 - Cambiar estado del inmueble *
                *   3 - Buscar Inmuebles            *
                *   4 - Salir                       *
                *************************************
                        Ingrese una opción: ''')
            os.system(limpiar)    
            if menu_principal == '1':
                 while True:

                    menu_inmuebles = input('''
                    *************************************
                    *           Inmuebles               *
                    *************************************
                    *       1 - Agregar                 *
                    *       2 - Editar                  *
                    *       3 - Eliminar                *
                    *       4 - Listar Inmuebles         *
                    *       5 - Volver                  *
                    *************************************
                        Ingrese una opción: ''')
                    os.system(limpiar)    
                    if menu_inmuebles == '1':
                        carga_inmueble()
                    elif menu_inmuebles == '2':
                        while True:
                            listar_inmueble()
                            inmueble_a_modificar = input('Ingrese inmueble que desea modificar \n')
                            menu_edicion=input('''
                                ¿Que dato desea modificar?
                                1-año
                                2-metros
                                3-habitaciones
                                4-garaje
                                5-zona 
                                6-estado
                                7-Cancelar \n
                                 ''')
                            if menu_edicion=='7':
                                break
                            else:
                                dato_a_modificar=input('Ingrese el valor que desea cambiar \n')
                                dato_a_modificar=int(dato_a_modificar)
                                menu_edicion=int(menu_edicion)
                                editar_inmueble(inmueble_a_modificar,menu_edicion,dato_a_modificar)
                                if editar_inmueble==True:
                                    print('Modificado')
                                    listar_inmueble()
                                    break
                        print('')
                    elif menu_inmuebles=='2':
                        while True:
                            listar_inmueble()
                            inmueble_a_modificar = input('Ingrese inmueble que desea modificar \n')
                            menu_estado=input('''¿En que estado se encuentra actualmente el inmueble?
                            1-DISPONIBLE
                            2-RESERVADO
                            3-SEÑADO
                            4-PAGADO
                            5-ENTREGADO''')
                            
                            if menu_estado=='1':
                                editar_inmueble(inmueble_a_modificar,menu_edicion, menu_estado='DISPONIBLE')
                            elif menu_estado=='2':
                                editar_inmueble(inmueble_a_modificar,menu_edicion,enu_estado='RESERVADO')
                            elif menu_estado=='3':
                                editar_inmueble(inmueble_a_modificar,menu_edicion,enu_estado='SEÑADO')
                            elif menu_estado=='4':
                                editar_inmueble(inmueble_a_modificar,menu_edicion,enu_estado='PAGADO')
                            elif menu_estado=='5':
                                editar_inmueble(inmueble_a_modificar,menu_edicion,enu_estado='ENTREGADO')

                    elif menu_inmuebles == '3':
                        pass
                    elif menu_inmuebles == '4':
                        listar_inmueble()
                        time.sleep(2)
                        break
                    elif menu_inmuebles == '5':
                        break
            
            elif menu_principal == '3':
                 while True:   
                    listar_inmueble()
                    inmueble= input('Ingrese los datos del  artículo o N para salir: ')
                    ingreso_datos_inmueble()
                    if inmueble in inmuebles:
                        eliminar_inmueble(inmueble)
                        print('El inmueble fue eliminado')
                        break
                    elif inmueble=='N':
                        break
                    else:
                        print('El inmueble no se encuentra')
                    time.sleep(2)
                
            elif menu_principal == '4':
                break
                time.sleep(2)