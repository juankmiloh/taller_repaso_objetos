class Producto:
    def __init__(self):
        self.imagen = ""
        self.descripcion = ""
        self.grupo = ""

# ---------------------------
# -- Armas
# ---------------------------

class Arma(Producto):
    def __init__(self):
        Producto.__init__(self)

class ArmaHumanos(Arma):
    def __init__(self):
        self.grupo = "Humanos"
        self.imagen = "imagenes/humanos/arma.png"
        self.descripcion = "Arma de los humanos"

class ArmaOrcos(Arma):
    def __init__(self):
        self.grupo = "Orcos"
        self.imagen = "imagenes/orcos/arma.png"
        self.descripcion = "Arma de los orcos"

# ---------------------------
# -- Escudos
# ---------------------------

class Escudo(Producto):
    def __init__(self):
        Producto.__init__(self)

class EscudoHumanos(Escudo):
    def __init__(self):
        self.grupo = "Humanos"
        self.imagen = "imagenes/humanos/escudo.png"
        self.descripcion = "Escudo de los humanos"

class EscudoOrcos(Escudo):
    def __init__(self):
        self.grupo = "Orcos"
        self.imagen = "imagenes/orcos/escudo.png"
        self.descripcion = "Escudo de los orcos"

# ---------------------------
# -- Monturas
# ---------------------------

class Montura(Producto):
    def __init__(self):
        Producto.__init__(self)

class MonturaHumanos(Montura):
    def __init__(self):
        self.grupo = "Humanos"
        self.imagen = "imagenes/humanos/montura.png"
        self.descripcion = "Montura de los humanos"

class MonturaOrcos(Montura):
    def __init__(self):
        self.grupo = "Orcos"
        self.imagen = "imagenes/orcos/montura.jpg"
        self.descripcion = "Montura de los orcos"

# ---------------------------
# -- Cuerpos
# ---------------------------

class Cuerpo(Producto):
    def __init__(self):
        Producto.__init__(self)

class CuerpoHumanos(Cuerpo):
    def __init__(self):
        self.grupo = "Humanos"
        self.descripcion = "Cuerpo de los humanos"
        self.imagen = "imagenes/humanos/cuerpo.png"

class CuerpoOrcos(Cuerpo):
    def __init__(self):
        self.grupo = "Orcos"
        self.descripcion = "Cuerpo de los orcos"
        self.imagen = "imagenes/orcos/cuerpo.png"

