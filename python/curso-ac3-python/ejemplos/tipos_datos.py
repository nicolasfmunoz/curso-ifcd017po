
#! TIPOS DE DATOS Y VARIABLES
#? CADENA DE CARACTERES
string = 'Se puede escribir con comillas simples' + " o con comillas dobles" 
print(type(string),string) # Se concatena con ',' el '+' siempre actua de operador
string_format = f'El {string}, con la f delante de la apertura damos formato'
print(string_format)
string_format2 = f'''Hola, 
    ¿Como 
        estas?''' # Con comillas simples*3 podemos escribir con saltos de carro y tabulaciones, respetandonos el formato
print(string_format2)

#? DATOS NUMERICOS 
integer = 12345 # Números enteros reales (Incluye negativos y 0)
print(type(integer),integer)

float = 89.45907 # Número con decimales o punto flotante
print(type(float),float)
print(round(float,2)) # Con el metodo round (redondear) podemos definir el número de decimales (argumento 2)

# Comportamiento de los tipos de datos númericos en divisiones
a = 9.0 #float
b = 2 #integer
print(a/b) # Nos devuelve float porque el resultado tiene decimales (Comportamiento distinto a JAVA)
print(int(a/b)) # Al convertirlo a número entero redondea al número entero más cercano. A la baja si el resultado es n.5

complex = 3 + 2j
print(type(complex),complex)

#? BOOLEAN
bool = True # A diferencia de JAVA, se escribe con la primera letra en mayuscula (True, False) 
print(type(bool),bool)
bool = 5 < 0 # Podemos darle el valor asignando un condicional
print(bool)
print('Hola'=='HOLA') # Si imprimimos en pantalla un condicional, nos dará el resultado

#? VARIABLES DINAMICAS
# La variable cambia de tipo en función de la asignación
variable = 'Hola'
print(type(variable),variable)
variable = 240
print(type(variable),variable)
variable = True
print(type(variable),variable)
variable = 8.7
print(type(variable),variable)

#? COLECCIONES DECLARADAS EN VARIABLES
variable = [] # Definimos una lista
print(type(variable),variable)
variable = () # Definimos una tupla
print(type(variable),variable)
variable = {} # Definimos un diccionario
print(type(variable),variable)
variable = {1,2,3,4} # Definimos un set. Hay que darle algún valor para que se diferencie de Diccionario, prescindiendo de la clave
print(type(variable),variable)



""" 
even = [2,4,6,8,0]
odd = [1,3,5,7,9]
comp = True
while comp:
    num = int(input('Introduzca un número: '))
    if num%2==0:
        print(f'El número {num} es un número par')
    elif num%2!=0:
        print(f'El número {num} es un número impar')
    else:
        print(f'El número {num} es un número negativo')
    resp = input('¿Quiere continuar revisando números?(Y/N)').lower()
    if resp == 'y':      
        comp = True
    elif resp == 'n':
        comp = False
    else:
        print('No entiendo su respuesta. ¡Hasta la proxima!')
        break
"""