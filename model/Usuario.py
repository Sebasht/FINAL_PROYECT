from model.Criterio import Criterio

class Usuario:

    def __init__(self):
        self._contraseña = ""
        self._nombre = ""
        self._verificado_clave = 0
        self._verificado_login = 0

    #sets

    def set_contraseña(self, x):
        self._contraseña = x
    def set_nombre(self, x):
        self._nombre = x
    def set_verificado(self, x):
        self._verificado = x
    def set_verificado_clave(self, x):
        self._verificado_clave = x
    def set_verificado_login(self, x):
        self._verificado_login = x

    #gets

    def get_nombre(self):
        return self._nombre
    def get_contraseña(self):
        return self._contraseña



