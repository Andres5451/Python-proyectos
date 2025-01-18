def suma(a,b):
    return a + b

def resta(a,b):
    return a - b

def multiplicacion(a,b):
    return a * b

def division(a,b):
    if b != 0:
        return a / b
    else: 
        return "Error: Division por cero"
def mostrar_menu():
    print("Clculadora Basica")
    print("1. Suma")
    print("2. resta")
    print("3. multiplicacion")
    print("4. division")
    print("5. Salir")
while True:
    mostrar_menu()
    opcion = input("Elige una opcion: ")
    num1 = float(input("Ingrese el primer numero: "))
    num2 = float(input("Ingrese el segundo numero: "))
    if opcion == "5":
        print("Saliendo del programa")
        break 
    if opcion in ["1", "2", "3", "4"]:
        if opcion == "1":
            print(f'Resultado: {suma(num1, num2)}')
        if opcion == "2":
            print(f'Resultado: {resta(num1, num2)}')
        if opcion == "3":
            print(f'Resultado: {multiplicacion(num1, num2)}')
        if opcion == "4":
            print(f'Resultado: {division(num1, num2)}')
    else:
        print("Opcion no valida intente de nuevo")
