print("--- CALCULADORA ---")
print("1. Suma")
print("2. Resta")
print("3. Multiplicación")
print("4. División")

option = input("Seleccione una opción (1-4): ")

num1 = float(input("Ingrese el primer numero: "))
num2 = float(input("Ingrese el segundo numero: "))

if option == "1":
    resultado = num1 + num2
    print("Resultado: ", resultado)

elif option == "2":
    resultado= num1 - num2
    print("Resultado: ", resultado)

elif option == "3":
        resultado = num1 * num2
        print("Resultado: ", resultado)

elif option == "4":
        resultado = num1 / num2
        print("Resultado: ", resultado)

else:
    print("Opción no válida. Por favor, seleccione una opción del 1 al 4.")
