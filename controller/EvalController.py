
class EvaluadorController:
    def __init__(self) -> None:
        super().__init__()
        self._evaluaciones = []

    def agregar_evaluacion(self, evaluacion_obj):
        self._evaluaciones.append(evaluacion_obj)

    def get_evaluaciones(self):
        return self._evaluaciones