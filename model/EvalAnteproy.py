import json

#Clase de Acta
class EvaluacionAnteproyecto:
    #Atributos
    def __init__(self) -> None:
        super().__init__()
        self._criterios = []    #Lista con los criterios usados para esta evaluacion
        self._nota = -1         #Inicia en -1 para indicar que aún no ha sido calificada, no en 0 ya que 0 puede ser una nota
        self._jurado1 = ""
        self._jurado2 = ""
        self._fecha_evaluacion = ""
        self._nombre_estudiante = ""
        self._id_acta = ""
        self._nombre_proyecto = ""
        self._codirector = ""
        self._director = ""
        self._tipo_doc = " "  # Identifica el tipo del documento
        self._observacion_final = " "

    def __str__(self) -> str:
        return json.dumps(self.__dict__)


    #Gets
    def get_observacion_final(self):
        return self._observacion_final
    def get_nota(self):
        return self._nota
    def get_criterios(self):
        return self._criterios
    def get_director(self):
        return self._director
    def get_codirector(self):
        return self._codirector
    def get_fecha_evaluacion(self):
        return self._fecha_evaluacion
    def get_id_acta(self):
        return self._id_acta
    def get_nombre_estudiante(self):
        return self._nombre_estudiante
    def get_jurado1(self):
        return self._jurado1
    def get_jurado2(self):
        return self._jurado2
    def get_nombre_proyecto(self):
        return self._nombre_proyecto
    def get_tipo_documento(self):
        return self._tipo_doc

    #Sets
    def set_observacion_final(self, x):
        self._observacion_final = x
    def set_nota(self, x):
        self._nota = x
    def set_director(self, x):
        self._director = x
    def set_codirector(self, x):
        self._codirector = x
    def set_jurado1(self, x):
        self._jurado1 = x
    def set_jurado2(self, x):
        self._jurado2 = x
    def set_nombre_proyecto(self, x):
        self._nombre_proyecto = x
    def set_nombre_estudiante(self, x):
        self._nombre_estudiante = x
    def set_tipo_documento(self, x):
        self._tipo_doc = x
    def set_id_acta(self, x):
        self._id_acta = x
    def set_fecha_evaluacion(self, x):
        self._fecha_evaluacion = x
    def set_lista_criterios(self, x):
        self._criterios = x