from os import error

def menu():
    print(f'''
    1. Sumar
    2. Restar
    3. Multiplicar
    4. Dividir
    5. Salir
    ''')

def get_option():
    response = input('Elija una opción: ')
    return response
