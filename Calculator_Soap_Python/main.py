from calculator.operations import add, subtract, multiply, divide

def main():
    print("Bienvenido a la Calculadora SOAP")
    print("Seleccione una operación:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")

    choice = input("Ingrese su elección (1/2/3/4): ")

    if choice not in ["1", "2", "3", "4"]:
        print("Opción inválida. Por favor intente de nuevo.")
        return

    try:
        num1 = int(input("Ingrese el primer número: "))
        num2 = int(input("Ingrese el segundo número: "))

        if choice == "1":
            result = add(num1, num2)
            operation = "Suma"
        elif choice == "2":
            result = subtract(num1, num2)
            operation = "Resta"
        elif choice == "3":
            result = multiply(num1, num2)
            operation = "Multiplicación"
        elif choice == "4":
            result = divide(num1, num2)
            operation = "División"

        print(f"Resultado de la {operation}: {result}")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

if __name__ == "__main__":
    main()
