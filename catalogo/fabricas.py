from productos import *

# ---------------------------
# -- Fabrica (V1)
# ---------------------------

class Fabrica:
    def crear_arma(self):
        pass

    def crear_escudo(self):
        pass

class FabricaHumanos(Fabrica):
    def crear_arma(self):
        return ArmaHumanos()

    def crear_escudo(self):
        return EscudoHumanos()

class FabricaOrcos(Fabrica):
    def crear_arma(self):
        return ArmaOrcos()

    def crear_escudo(self):
        return EscudoOrcos()

# ---------------------------
# -- Fabrica (V2)
# ---------------------------

class FabricaV2:
    def crear_montura(self):
        pass

    def crear_cuerpo(self):
        pass

class FabricaHumanosV2(FabricaV2):
    def crear_montura(self):
        return MonturaHumanos()

    def crear_cuerpo(self):
        return CuerpoHumanos()

class FabricaOrcosV2(FabricaV2):
    def crear_montura(self):
        return MonturaOrcos()

    def crear_cuerpo(self):
        return CuerpoOrcos()