from productos import *

class Fabrica:
    def crear_arma(self):
        pass

    def crear_escudo(self):
        pass

    def crear_montura(self):
        pass

class FabricaHumanos(Fabrica):
    def crear_arma(self):
        return ArmaHumanos()

    def crear_escudo(self):
        return EscudoHumanos()

    def crear_montura(self):
        return MonturaHumanos()

class FabricaOrcos(Fabrica):
    def crear_arma(self):
        return ArmaOrcos()

    def crear_escudo(self):
        return EscudoOrcos()

    def crear_montura(self):
        return MonturaOrcos()

# --------------------
# Fabrica (V2) de cuerpos
# --------------------

class FabricaCuerpo:
    def crear_cuerpo(self):
        pass

class FabricaHumanos2(FabricaCuerpo):

    def crear_cuerpo(self):
       return CuerpoHumanos()

class FabricaOrcos2(FabricaCuerpo):

    def crear_cuerpo(self):
        return CuerpoOrcos()