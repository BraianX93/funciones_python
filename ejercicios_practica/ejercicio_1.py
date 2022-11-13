# Funciones [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 3.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios con funciones

# Objetivo:
# Completar el funcionamiento de la función "imprimir_mayor"

def imprimir_mayor(numero_1, numero_2):
    print("Funcion imprimir mayor")
    # Alumno:
    # En esta función debe determinar cual de los dos
    # números ingresados por parámetro es mayor
    
    # Crear una variable llamada mayor en donde
    # almacenará el número mayor ingresado
    # Si ambos números son iguales, almacenar
    # cualquier de los datos en la variable mayor

    # Imprimir en pantalla la variable mayor
if numero_1 > numero_2:
        print(f'el número {numero_1} es mayor que el número {numero_2}')
    elif numero_2 > numero_1:
        print(f'el número {numero_2} es mayor a el número {numero_1}')
    else:
        print('Ambos son iguales')

if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    
    imprimir_mayor(2, 10)

    print("terminamos")
