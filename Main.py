from Manejador import Manejador
import os

if __name__ == "__main__":
    m = Manejador()
    m.Carga()
    m.Listar()

    continuar = True

    while continuar:
        print("MENU".center(20,"-"))
        print("[1] Actualizar el valor de vehículo de cada plan de ahorro")
        print("[2] Dado un valor, mostrar código del plan, modelo y versión del vehículo cuyo valor de la cuota sea inferior al valor dado.")
        print("[3] Mostrar el monto que se debe haber pagado para licitar el vehículo de código dado.")
        print("[4] Dado el código de un plan, modificar la cantidad cuotas que debe tener pagas para licitar")
        print("[0] Para SALIR del menu")

        op = int( input("INGRESE OPCION POR TECLADO\n"))
        os.system("cls")
        if ( op == 1):
            print("".center(20,"-"))
            print("Valores de vehículos actualizados.\n")
            print(m.opcion1())
        elif(op == 2):
            print("Ingrese valor de vehículo: ")
            valor = int(input())
            print(m.opcion2(valor))
        elif(op == 3):
            print("Ingrese codigo de plan para mostrar monto que se debe haber pagado para licitar el vehículo: ")
            print(m.opcion3(codigo))
        elif(op == 4):
            print("Ingrese el código del plan a modificar: ")
            codigo = int(input())
            print("Ingrese la cantidad de cuotas que debe tener pagas para licitar: ")
            cantCuotas = int(input())
            m.opcion4(codigo, cantCuotas)
        elif(op == 0):
            continuar = not continuar