
#! COLECCIONES
dash ='-'*120  # Para visualizar mejor los datos en los print
sep = f'{dash}\n' # Para visualizar mejor los datos en los print
despedida = "Adios" # Variable para usarla de ejemplo

#? LISTA = LIST
# Las listas son mutables y nos permiten almacenar diversos tipos de datos
print(sep*2,'LISTAS') # Separamos para mayor legibilidad

#DECLARACION DE LISTAS
new_list = [] # Declaración de lista sin asignación de valores. Usamos corchetes []
print(sep,'Tipo:',type(new_list))
new_list = [1,"Hola",6,6,despedida,128.4] # Declaración de Lista con asignación de valores
print(sep,'Lista:',new_list)

# POSIBILIDADES PARA QUITAR LOS COCRCHETES EN LA IMPRESION POR PANTALLA
print(sep,'Lista sin corchetes usando (*):',*new_list) # El * delante de la variable de tipo list nos muestra los datos sin corchetes y comas.

list1 = str(new_list)[1:-1] # Lista convertida a string. Definimos el rango (Valores entre corchetes) de las posiciones que queremos que nos muestre, para quitar los corchetes
print(sep,'Lista convertida a string quitando corchetes con rango de posiciones:',list1)

list2 = str(new_list).replace('[','').replace(']','') # Lista convertida a string. Usamos los metodos replace() (propios del string) para remplazar los corchetes por nada
print(sep,'lista convertida a string quitando corchetes con metodo replace():',list2)

# ALGUNOS METODOS DE LAS LISTAS
# append()
num = 7
new_list.append(num) # Agrega un elemento al final de la lista
print(sep,f'Agregamos {num} al final de la lista {new_list}')

# count()
recuento_list = new_list.count(6) # Nos devuelve el número de veces que se repite el valor que pasamos como argumento
print(sep,'El número de datos con valor 6 que hay en la lista es: ',recuento_list)

# pop()
variable_pop = new_list.pop(2) # Remueve de la lista el valor de la posición indicada y nos lo devuelve
print(sep,'Variable obtenida y removida de la lista:',variable_pop,'Lista actual:',new_list) 

# remove()
new_list.remove(num) # Removemos la variable con valor 7 que añadimos anteriormente
print(sep,'Eliminamos el número 7 de la lista',new_list)

# ASIGNAR VALORES POR POSICION
new_list[2] = 88 # Usamos el uso de corchetes para asignar un valor en la posición indicada que sustituye al anterior
print(sep,'Añadimos el 88 a la lista que sustituye al 6',new_list)


#? TUPLA = TUPLE
print(sep*2,'TUPLAS') # Separamos para mayor legibilidad
# Las tuplas son similares a las listas pero sus valores son inmutables

# DECLARACION DE TUPLAS
tupla = () # Declaración de una tupla sin asignación de valores. Usamos parentesis ()
print(sep,'Tipo:',type(tupla))
tupla = (1,'Hola',8,8,8,9.3) # Declaracion de una tupla con asignación de valores
print(sep,'Tupla:',tupla)

try: # Ponemos a prueba su inmutabilidad intentando asignar un nuevo valor a la posición 2
    tupla[2] = 88
except:
    print(sep,'No podemos sustituir valores de la tupla ya existentes.') # Como no nos lo permite entre en el bloque "except"

# METODOS PROPIOS DE LA TUPLA (UNICAMENTE HAY DOS)
# count()
recuento_tupla = tupla.count(8)
print(sep,f'El número de datos con valor 8 que hay en la tupla es: {recuento_tupla}')

# index()
num = 8 # Variable que vamos a buscar con index()
ele_tuple = tupla.index(num,0,-1) # Recibimos la posicion donde se encuentra el valor definido en el primer argumento ( valor, inicio_busqueda, final_busqueda )
print(sep,f'La posición donde aparece el primer {num} en la lista es ',ele_tuple)



#? FUNCIONES QUE AFECTAN A LISTAS Y TUPLAS
print(sep*2,'FUNCIONES QUE AFECTAN A LISTAS Y TUPLAS') # Separamos para mayor legibilidad

# Declaramos nuevas listas y tuplas con valores númericos para hacer uso de las funciones
num_list = [5,10,20,30]
num_tuple = (40,50,60)

# len()
list_size = len(num_list) # Nos devuelve la dimensión de la lista
print(sep,f'La dimensión de la lista es = {list_size}')
tuple_size = len(num_tuple) # Nos devuelve la dimensión de la tupla
print(sep,f'La dimensión de la tupla es = {tuple_size}')

# sum()
suma_list = sum(num_list) # Suma los valores de la lista
print(sep,f'La suma de los valores de la lista {num_list} es = {suma_list}')
suma_tuple = sum(num_tuple) # Suma los valores de las tupla
print(sep,f'La suma de los valores de la tupla {num_tuple} es = {suma_tuple}')

# max()
max_value_list = max(num_list) # Retorna el elemento de mayor valor en la lista
print(sep,f'El elemento de mayor valor en la lista {num_list} es = {max_value_list}')
max_value_tuple = max(num_tuple) # Retorna el elemento de mayor valor en la tupla
print(sep,f'El elemento de mayor valor en la tupla {num_tuple} es = {max_value_tuple}')


# min()
min_value_list = min(num_list) # Retorna el elemento de menor valor en la lista
print(sep,f'El elemento de menor valor en la lista {num_list} es = {min_value_list}')
min_value_tuple = min(num_tuple) # Retorna el elemento de menor valor en la tupla
print(sep,f'El elemento de menor valor en la tupla {num_tuple} es = {min_value_tuple}')


#? DICCIONARIO = DICT
# Estructura que almacena un conjunto de datos, agrupados en pares (clave-valor). Son de tipo mutable. Las claves deben ser únicas.
print(sep*2,'DICIONARIOS') # Separamos para mayor legibilidad

# DECLARACION DE DICCIONARIOS
dict = {} # Declaracion sin asignación de valores. Usamos llaves {}
print(sep,'Tipo:',type(dict))
dict = {'Valor1': 149,'Valor2': 233} # Declaración con asignación de valores (clave-valor)
print(sep,'Diccionario:',dict)

dict['Valor1'] = 333 # Asignamos valores inroduciendo el nombre de la clave
print(sep,'Diccionario con el valor de "Valor1" modificado:',dict)

# Diccionario complejo (con otros diccionarios como valor)
new_dict ={
    'Lavadora':{
        'Precio': 600, 
        'Modelo': 'Balay 20IJ'},
    'Televisor':{
        'Precio': 1500, 
        'Modelo': 'Samsumg FF9002'},
    'Microondas':{
        'Precio': 200, 
        'Modelo': 'Balay 300L'},
    'Nevera':{
        'Precio': 870, 
        'Modelo': 'Fagor 20IJ'},
} # Ordenamos para mejor lectura sin errores por indentación gracias a las {}
print(sep,'Diccionario complejo:',new_dict)

# METODOS UTILES PARA BUCLES E ITERACIONES
total= 0 # Declaramos variables para los ejemplos
articulos = '' # Declaramos variables para los ejemplos

# keys()
print(sep,'Imprimimos las claves de nuestro diccionario usando keys():')
for key in new_dict.keys(): # Nos devuelve las claves del diccionario
    print('\t',key)

# values()
print(sep,'Imprimimos los valores de nuestro diccionario usando values():')
for value in new_dict.values(): # Nos devuelve los valores del diccionario
    print('\t',value)

print(sep,'Obtenemos una "factura" usando items():')
# items()
for key, value in new_dict.items(): # Nos devuelve dos elementos, la clave (primer elemento declarado) y el valor (segundo elemento declarado)
    total += value['Precio'] # Hacemos referencia a la clave "Precio" del segundo diccionario para obtener el valor
    articulos += '\t- ' + key + ' ' + value['Modelo'] + '\n' # Hacemos referencia a la clave "Modelo" del segundo diccionario para obtener el modelo
print(sep,f'ARTICULOS: \n{articulos} PRECIO TOTAL:\n\t- {total} €')

#TODO Metodos adicionales de las colecciones




