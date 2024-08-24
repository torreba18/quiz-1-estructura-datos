#Bienvendida 

def recibido():
    print("""
    ***************************

    1. Suma
    2. Resta
    3. Multiplicacion
    4. Division
    5. Potenciacion
    6. Residuo
    7. Apagar calculadora

    ***************************""")

#Operaciones 

def ejecucion():
    opcion = int(input("Definir lo que quiere lograr: ")) 
    while(opcion >0 and opcion <7):
        n1 = int(float(input("Primer numero: ")))
        n2 = int(float(input("Segundo numero: ")))
        if (opcion == 1):
            print("El resultado es: ", n1 + n2)
            opcion = int(input("Definir lo que quiere lograr: "))
        elif (opcion == 2):
            print("El resultado es: ", n1 - n2)
            opcion = int(input("Definir lo que quiere lograr: "))
        elif (opcion == 3):
            print("El resultado es: ", n1 * n2)
            opcion = int(input("Definir lo que quiere lograr: "))
        elif (opcion == 4):
            try:
                print("El resultado es: ", n1 / n2)
                opcion = int(input("Definir lo que quiere lograr: "))
            except ZeroDivisionError:
                print("La division no se puede realizar")
        elif (opcion == 5):
            print("El resultado es: ", n1 ** n2)
            opcion = int(input("Definir lo que quiere lograr: "))
        elif (opcion == 6):
            print("El resultado es: ", n1 % n2)
            opcion = int(input("Definir lo que quiere lograr: "))
        elif (opcion == 0 or 7):
            print("APAGANDO")
print(recibido(), ejecucion())