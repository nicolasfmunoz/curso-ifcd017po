from models import Calculadora
from utils import *

if __name__ == '__main__':
    print(f'''
--------------------------------------
Bienvenido a la calculadora en Python!
--------------------------------------
    ''')

    user = ''
    while user != 'q':
        try:
            num1 = int(input('Escoja el operando 1: '))
            num2 = int(input('Escoja el operando 2: '))
        except ValueError:
            print('Los datos son inválidos. Ingrese datos correctos por favor. No sea idiota.')
            continue

        calc = Calculadora(num1, num2)

        menu()
        option = get_option()

        operation_type = ''

        if option == '1':
            operation_type = 'suma'
            calc.sumar()
        elif option == '2':
            operation_type = 'resta'
            calc.restar()
        elif option == '3':
            operation_type = 'división'
            calc.dividir()
        elif option == '4':
            operation_type = 'multiplicación'
            calc.multiplicar()
        elif option == '5':
            user = 'q'
            continue
        else:
            print('Opción inválida. Inténtelo otra vez.')
            continue

        print(str(calc))
        print(f'Resultado de la {operation_type}: {calc.result}')

    print('Adiós!')
    print('\033[91m', '''
───▄▄▄▄▄▄─────▄▄▄▄▄▄
─▄█▓▓▓▓▓▓█▄─▄█▓▓▓▓▓▓█▄
▐█▓▓▒▒▒▒▒▓▓█▓▓▒▒▒▒▒▓▓█▌
█▓▓▒▒░╔╗╔═╦═╦═╦═╗░▒▒▓▓█
█▓▓▒▒░║╠╣╬╠╗║╔╣╩╣░▒▒▓▓█
▐█▓▓▒▒╚═╩═╝╚═╝╚═╝▒▒▓▓█▌
─▀█▓▓▒▒░░░░░░░░░▒▒▓▓█▀
───▀█▓▓▒▒░░░░░▒▒▓▓█▀
─────▀█▓▓▒▒░▒▒▓▓█▀
──────▀█▓▓▒▓▓█▀
────────▀█▓█▀
──────────▀
    ''')
