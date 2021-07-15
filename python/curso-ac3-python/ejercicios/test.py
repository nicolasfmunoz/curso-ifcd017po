def function_sample(*args, **kwargs):
    print('Printing args "args" (tuple):\n')
    for item in args:
        print(f'    item: {item}')

    print('\n')

    print('Printing args with keywords "kwargs" (dict):\n')
    for k, v in kwargs.items():
        print(f'    key: {k}    value: {v}')


def function_2():
    pass

# solo funciona si se ejecuta desde el mismo archivo, y no desde otro archivo
if __name__ == "__main__":
    lista = [1, 2, 'hello']

    print(*lista) # imprime la listal impia, separando items por espacios y sin los corchetes
    print(str(lista[1:-1])) # convierte lista a string, y devuelve sub-lista desde posicion 1 hasta el penultimo
    print(lista) # imprime la lista a secas, con corchetes y el separador, que es la coma
    print('\n'.join(str(x) for x in lista)) # itera con un lambda, y a cada item lo convierte en un string y luego hace un join de todos los items recibidos

    function_sample(*lista, key1='hello', key2='bye')

    tupla = (1, 2, 3)
    tupla2 = (5, 6)
    tupla3 = tupla.__add__(tupla2)
    print(tupla3)

    dict1 = {
        'key1': 'test1',
        'key2': 'test2',
        'key3': 'test3'
    }

    for item in dict1.items():
        print(item)

    print('\n ITERATORS Y MAP \n'.center(53, '='))

    listtita = [1, 2, 3, 4, 5]

    iterator = map(lambda num: num**2, listtita)

    #filter(dict.find()) ...

    print(iterator.__next__())
    print(next(iterator))
    print(next(iterator))
    print(next(iterator))
    print(next(iterator))

#! Comprehension list
    """[summary]
    """

#? Modo simple con comprehension list
data = [1, 2, 3, 4, 5]
result_list = [num**2 for num in data]
print(type(result_list))
print(result_list)

#? Modo generator
generador = (num**2 for num in data)
print(type(generador))
print(next(generador))

#? Comprehension list con operador ternario
result_ternario = [num for num in data if num % 2 == 0] # sin 'else', el if va a la derecha/al final
print(result_ternario)

result_ternario_2 = [num**2 if num % 2 == 0 else num for num in data] # Con 'else', el if/else se pone antes (al principio))
print(result_ternario_2)

#? Map y op ternario
result_map_ternario = list(map(lambda num: num**2 if num % 2 == 0 else None, data))
print(result_map_ternario)