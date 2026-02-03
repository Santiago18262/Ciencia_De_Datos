num1 = 0
num2 = 0
resultado = 0

# Pidiendo números por consola
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

# Switch para elegir el operador
operador = input("\nIngrese el operador (+, -, *, /): ")

match operador:
    case '+':
        resultado = num1 + num2
    case '-':
        resultado = num1 - num2
    case '*':
        resultado = num1 * num2
    case '/':
        if num2 != 0:
            resultado = num1 / num2
        else:
            print("Error: División por cero.")
            resultado = None
        
# Mostrando el resultado
print("\nEl resultado de la operación es:", resultado) 