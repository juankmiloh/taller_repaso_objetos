from fabricas import *

class Componente():
    def crear_arma(self):
        pass

    def crear_escudo(self):
        pass
    
    def crear_cuerpo(self):
        pass

    def crear_montura(self):
        pass

class ComponenteConcreto(Componente):
    def crear_arma(self):
        print("Crear arma del personaje");

    def crear_escudo(self):
        print("Crear escudo del personaje");
    
    def crear_cuerpo(self):
        print("Crear cuerpo del personaje");

    def crear_montura(self):
        print("Crear montura del personaje");

class Decorador(Componente):
    def __init__(self, componente):
        self.__comp__ = componente

    def crear_arma(self):
        pass

    def crear_escudo(self):
        pass
    
    def crear_cuerpo(self):
        pass

    def crear_montura(self):
        pass

# ---------------------------
# -- Decorador Humanos
# ---------------------------
class DecoradorConcretoHumanos(Decorador):
    def crear_arma(self):
        return FabricaHumanos.crear_arma(self)
    
    def crear_escudo(self):
        return FabricaHumanos.crear_escudo(self)
    
    def crear_cuerpo(self):
        return FabricaHumanosV2.crear_cuerpo(self)

    def crear_montura(self):
        return FabricaHumanosV2.crear_montura(self)

# ---------------------------
# -- Decorador Orcos
# ---------------------------
class DecoradorConcretoOrcos(Decorador):
    def crear_arma(self):
        return FabricaOrcos.crear_arma(self)

    def crear_escudo(self):
        return FabricaOrcos.crear_escudo(self)
    
    def crear_cuerpo(self):
        return FabricaOrcosV2.crear_cuerpo(self)

    def crear_montura(self):
        return FabricaOrcosV2.crear_montura(self)