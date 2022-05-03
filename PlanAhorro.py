class PlanAhorro:
    __codigo = 0
    __modelo = ""
    __version = ""
    __valor = 0
    __cantCuotas = 0
    __cantCuotaspag = 0

    def __init__(self, codigo, modelo, version, valor, cantCuotas, cantCuotaspag):
        self.__codigo = codigo
        self.__modelo = modelo
        self.__version = version
        self.__valor = valor
        self.__cantCuotas = cantCuotas
        self.__cantCuotaspag = cantCuotaspag
    
    def __str__(self):
        print("Codigo: {}\nModelo: {}\nVersion: {}\nValor: {}\nCantidad de cuotas: {}\nCantidad de cuotas pagadas: {}".format(self.__codigo, self.__modelo, self.__version, self.__valor, self.__cantCuotas, self.__cantCuotaspag))
    
    def getCodigo(self):
        return self.__codigo
    
    def getModelo(self):
        return self.__modelo
    
    