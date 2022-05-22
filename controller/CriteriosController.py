from model.Criterio import Criterio

class CriteriosController:
    def __init__(self) -> None:
        super().__init__()
        self._criterios = []

    def get_criterios(self):
        return self._criterios

    def agregar_criterios(self, criterio):
        self._criterios.append(criterio)