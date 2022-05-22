
class UsuarioController:
    def __init__(self) -> None:
        # 0 -> jurado
        # 1 -> asistente
        # 2 -> Directora
        super().__init__()
        self._usuarios = []
        self._index = 0
        self._verificador = 0
        self._tipo = 0

    def agregar_usuario(self, usuario):
        self._usuarios.append(usuario)

    #sets
    def set_tipo(self, x):
        self._tipo = x
    def set_index(self, x):
        self._index = x
    def set_verificador(self, x):
        self._verificador = x

    #gets
    def get_verificador(self):
        return self._verificador
    def get_tipo(self):
        return self._tipo
    def get_usuarios(self):
        return self._usuarios

