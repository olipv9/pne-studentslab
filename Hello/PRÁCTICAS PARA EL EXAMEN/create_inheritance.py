class Padre():  # Creamos la clase Padre
    def __init__(self, ojos, cejas):  # Definimos los Atributos
        self.ojos = ojos
        self.cejas = cejas


class Hijo(Padre):  # Creamos clase hija que hereda de Padre
    def __init__(self, ojos, cejas, cara):  # creamos el constructor de la clase especificando atributos
        super().__init__(ojos, cejas)  # Especificamos la clase y llamamos a su constructor + Atributos
        self.cara = cara  # Especificamos el nuevo atributo para Hijo

Tomas = Hijo('Azules', 'Marrones', 'Larga')
print(Tomas.ojos, Tomas.cejas, Tomas.cara)