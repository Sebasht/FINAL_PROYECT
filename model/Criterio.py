import json


class Criterio:
    #atributos

    def __int__(self):
        self._descripcion = " "
        self._categoria = " "
        self._ponderacion = 0
        self._nota = 0
        self._nota_jurado1 = 0
        self._nota_jurado2 = 0
        self._observacion = " "

    def __str__(self) -> str:
        return json.dump(self.__dict__)

    #sets

    def set_descripcion(self, x):
        self._descripcion = x
    def set_categoria(self, x):
        self._categoria = x
    def set_nota_criterio(self, x):
        self._nota = x
    def set_ponderacion(self, x):
        self._ponderacion = x
    def set_observacion_criterio(self, x):
        self._observacion = x
    def set_nota_jurado1(self, x):
        self._nota_jurado1 = x
    def set_nota_jurado2(self, x):
        self._nota_jurado2 = x
    def set_nota(self, x):
        self._nota = x
    #gets

    def get_descripcion(self):
        return self._descripcion
    def get_categoria(self):
        return self._categoria
    def get_nota_criterio(self):
        return self._nota
    def get_ponderacion(self):
        return self._ponderacion
    def get_observacion_criterio(self):
        return self._observacion
    def get_nota_jurado1(self):
        return self._nota_jurado1
    def get_nota_jurado2(self):
        return self._nota_jurado2
    def get_nota(self):
        return self._nota
