
#! OPERADORES
# Variables declaradas para los ejemplos
num1 = 5
num2 = 2

#? OPERADORES ARITMETICOS
print(f'Suma de {num1}+{num2} = {num1+num2}') # Operador '+'
print(f'Resta de {num1}-{num2} = {num1-num2}') # Operador '-'
print(f'Multiplicación de {num1}*{num2} = {num1*num2}') # Operador '*'
print(f'Division de {num1}/{num2} = {num1/num2}') # Operador '/'
print(f'Division entera de {num1}//{num2} = {num1/num2}') # Operador '//', nos devuelve un número entero aunque el resultado sea decimal
print(f'Potencia de {num1} elevado a {num2} = {num1**num2}') # Operador '**'
print(f'Resto o modulo de {num1} entre {num2} = {num1%num2}') # Operador '**'

#? OPERADORES ARITMETICOS SIMPLIFICADOS
num1 += 3 # Equivalente a num1 = num1 + 3
print('Sumamos tres',num1)
num1 -= 2 # Equivalente a num1 = num1 - 2
print('Restamos dos',num1)
num1 *= 6 # Equivalente a num1 = num1 * 6
print('Multiplicamos por seis',num1)
num1 /= 5 # Equivalente a num1 = num1 / 5
print('Dividimos entre cinco',num1)
num1 //= 3 # Equivalente a num1 = num1 // 3
print('Division con resultado entero entre tres',num1)
num1 **= 9 # Equivalente a num1 = num1 ** 9
print('Elevamos el número a potencia 9',num1)
num1 %=7 # Equivalente a num1 = num1 % 7
print('Obtenemos el resto de dividir entre 7',num1)
num1 = 5 # Asignamos a la variable su valor original para seguir con los ejemplos

#? OPERADORES RELACIONALES
print(f'Comprobar igualdad entre {num1} y {num2}: {num1==num2}') # Operador '=='
print(f'Comprobar desigualdad entre {num1} y {num2}: {num1!=num2}') # Operador '!='
print(f'Comprobar si {num1} es mayor que {num2}: {num1>num2}') # Operador '>'
print(f'Comprobar si {num1} es menor que {num2}: {num1<num2}') # Operador '<'
print(f'Comprobar si {num1} es mayor o igual que {num2}: {num1>=num2}') # Operador '>='
print(f'Comprobar si {num1} es menor o igual que {num2}: {num1<=num2}') # Operador '<='


#? OPERADORES LÓGICOS
# RECOMENDACIÓN: Vaya modificando las condiciones y ejecutando para ver los distintos comportamientos

# AND
if num2 < num1 and num2%2==0:
    print('Cumple las dos condiciones')
else:
    print('No cumple, al menos, una de las dos condiciones')

# OR
if num2 > num1 or num2%2==0:
    print('Cumple, al menos, una de las dos condiciones')
else:
    print('No cumple ninguna de las dos condiciones')

# NOT
if not num1%2==0:
    print('Cumple la negación a la condición')
else:
    print('No cumple la negación a la condición')

# IN & NOT IN
lista = [1,2,'Python']
if num2 in lista:
    print('Se cumple la condición porque la variable se encuentra en la lista')
else:
    print('La variable no se encuentra en la lista')

if num2 not in lista:
    print('Cumple la condición porque la variable no se encuentra en la lista')
else:
    print('La variable se encuentra en la lista')

#? OPERADORES BINARIOS
# Usaremos el metodo bin() que convierte decimales a binario para ver el comportamiento
print(f'Realiza bit a bit la operación AND en los operandos {num1} {num2}: {num1&num2} Binario:{bin(num1&num2)}') # Operador '&'
print(f'Realiza bit a bit la operación OR en los operandos {num1} {num2}: {num1|num2} Binario:{bin(num1|num2)}') # Operador '|'
print(f'Realiza bit a bit la operación XOR  en los operandos {num1} {num2}: {num1^num2} Binario:{bin(num1^num2)}') # Operador '^'
print(f'Realiza bit a bit la operación NOT bit a bit. Invierte cada bit en el operando {num1}: {~num1} Binario:{bin(~num1)}') # Operador '~'
print(f'Realiza un desplazamiento a la derecha bit a bit. Desplaza los bits del operador de la izquierda a la derecha tantos bits como indica el operador de la derecha entre {num1} {num2}: {num1>>num2} Binario:{bin(num1>>num2)}') # Operador '>>'
print(f'Realiza un desplazamiento a la izquierda bit a bit. Desplaza los bits del operador de la derecha a la izquierda tantos bits como indica el operador de la derecha entre {num1} {num2}: {num1<<num2} Binario:{bin(num1<<num2)}') # Operador '<<'


