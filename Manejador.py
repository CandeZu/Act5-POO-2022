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
    
    def opcion1(self, ValorNuevo):

        for i in range(len(self.__lista)):
            print("COD. PLAN: {}".format(self.__lista[i].getCodigo()))
            print("MODELO: {}".format(self.__lista[i].getModelo()))
            print("VERSION: {}".format(self.__lista[i].getVersion()))
            self.__lista[i].modificarValor(ValorNuevo)
            print("Valor actualizado")
            print("".center(20,"-"))
        return    
    
    def opcion2(self, valorAComparar):
        print("Vehiculos de cuota menor o igual a: {}".format(valorAComparar))
        for i in range (len(self.__lista)):
            valorCuotaPlan = (self.__lista[i].getValor() / self.__lista[i].getCantCuotas()) + self.__lista[i].getValor()*0.1
            if(valorCuotaPlan <= valorAComparar):
                print("Codigo del plan: {}".format(self.__lista[i].getCodigo()))
                print("Modelo: {}".format(self.__lista[i].getModelo()))
                print("Version: {}".format(self.__lista[i].getVersion()))
                print("Valor de cuota: ${}".format(round(valorCuotaPlan,2)))
        return

    def opcion3(self):
        print("Cantidad de cuotas que se deben pagar: {}".format(PlanAhorro.retornarCuotasLicitar()))
        return

    def opcion4(self, codigo):
        plan = self.buscar(codigo)
        if (plan != None):
            print("Ingrese nueva cantidad de cuotas que debe tener pagas para licitar un vehiculo: ")
            cantCuotas = int(input())
            plan.modificarCuotasLicitar(cantCuotas)
            print("Cambio realizado con exito")
            print(plan.mostrarCuotasLicitar())

    def buscar(self,codigo):
        i = 0

        while (self.__lista[i].getCodigo() != codigo):
            i += 1
        if(self.__lista[i].getCodigo() == codigo):
            plan = self.__lista[i]
            print("Plan encontrado")
            print(plan)
        else:
            print("Plan no existente")
        return plan