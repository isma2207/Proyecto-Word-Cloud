class Vueloa:
    def __init__(self, aerolinea, Salida, Llegada, Tiempo, costo, fechaIda, fechVuelta, numPersona, Val):
        self.__aerolinea = aerolinea
        self.__Salida = Salida
        self.__Llegada = Llegada
        self.__Tiempo = Tiempo
        self.__fechIda= fechaIda
        self.__fechVuelta=fechVuelta
        self.__numPersona=numPersona
        self.__costo=costo
        self.__Val=Val


# /get
    @property
    def aerolinea(self):
        return self.__aerolinea
# /set
    @aerolinea.setter
    def aerolinea(self, valor):
        self.__aerolinea = valor


# /get
    @property
    def origen(self):
        return self.__Salida
# /set
    @origen.setter
    def origen(self, valor):
        self.__Salida = valor


# /get
    @property
    def destino(self):
        return self.__Llegada
# /set
    @destino.setter
    def destino(self, valor):
        self.__Llegada= valor


# /get
    @property
    def duracion(self):
        return self.__Tiempo
# /set
    @duracion.setter
    def duracion(self, valor):
        self.__Tiempo = valor

    @property
    def fechIda(self):
        return self.__fechIda

    # /set
    @fechIda.setter
    def fechIda(self, valor):
        self.__fechIda = valor

    @property
    def fechVuelta(self):
        return self.__fechVuelta

    # /set
    @fechVuelta.setter
    def fechVuelta(self, valor):
        self.__fechVuelta = valor

    @property
    def precio(self):
        return self.__costo
     # /set
    @precio.setter
    def precio(self, valor):
        self.__costo = valor

        # /get

    @property
    def npersona(self):
        return self.__numPersona

    # /set
    @npersona.setter
    def npersona(self, valor):
        self.__numPersona = valor

    # /get
    @property
    def cod(self):
            return self.__Val

    # /set
    @cod.setter
    def cod(self, valor):
            self.__Val = valor

    #/def __str__(self):
       #/ cadena=
     #/   return cadena

   # def __str__(self) :
    #    return self.__aerolinea,self.__Salida,self.__Llegada,self.__Tiempo,self.__escala,self.__clase,s