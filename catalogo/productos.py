class Producto:
    def __init__(self):
        self.imagen = ""
        self.descripcion = ""
        self.grupo = ""

class Arma(Producto):
    def __init__(self):
        Producto.__init__(self)
        self.mango = ""

class ArmaHumanos(Arma):
    def __init__(self):
        self.grupo = "Humanos"
        self.imagen = "imagenes/humanos/arma.png"
        self.descripcion = "arma de los humanos"
        self.mango = True

class ArmaOrcos(Arma):
    def __init__(self):
        self.grupo = "Orcos"
        self.imagen = "imagenes/orcos/arma.png"
        self.descripcion = "arma de los orcos"

class Escudo(Producto):
    def __init__(self):
        Producto.__init__(self)

class EscudoHumanos(Escudo):
    def __init__(self):
        self.grupo = "Humanos"
        self.imagen = "imagenes/humanos/escudo.png"
        self.descripcion = "escudo de los humanos"

class EscudoOrcos(Escudo):
    def __init__(self):
        self.grupo = "Orcos"
        self.imagen = "imagenes/orcos/escudo.png"
        self.descripcion = "escudo de los orcos"

class Montura(Producto):
    def __init__(self):
        Producto.__init__(self)

class MonturaHumanos(Montura):
    def __init__(self):
        self.grupo = "Humanos"
        self.imagen = "imagenes/humanos/montura.png"
        self.descripcion = "montura humanos"

class MonturaOrcos(Montura):
    def __init__(self):
        self.grupo = "Orcos"
        self.imagen = "imagenes/orcos/montura.jpg"
        self.descripcion = "montura orcos"

# --------------------
# Cuerpos
# --------------------

class Cuerpo:
    def __init__(self):
        self.grupo = ""
        self.descripcion = ""
        self.imagen = ""

class esqueleto(Cuerpo):
    def __init__(self):
        Cuerpo.__init__(self)

class CuerpoHumanos(esqueleto):
    def __init__(self):
        self.grupo = "Humanos"
        self.descripcion = "Cuerpo humanos"
        self.imagen = "imagenes/humanos/cuerpo.png"

class CuerpoOrcos(esqueleto):
    def __init__(self):
        self.grupo = "Orcos"
        self.descripcion = "Cuerpo orcos"
        self.imagen = "imagenes/orcos/cuerpo.png"