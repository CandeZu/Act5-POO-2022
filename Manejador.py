from PlanAhorro import PlanAhorro
import csv

class Manejador:
    __lista = []

    def __init__(self):
        self.__lista = []
    
    def Carga(self):
        archivo = open("PlanAhorro.csv")
        lector = csv.reader(archivo, delimiter=";")
        for fila in lector:
            codigo = int(fila[0])
            modelo = fila[1]
            version = fila[2]
            valor = int(fila[3])
            cantCuotas = int(fila[4])
            cantCuotaspag = int(fila[5])
            nuevoplan = PlanAhorro(codigo, modelo, version, valor, cantCuotas, cantCuotaspag)
            self.__lista.append(nuevoplan)
        archivo.close()
    
    def Listar(self):
        for plan in self.__lista:
            print(plan)
    
    def opcion1(self):
        for plan in self.__lista:
            
