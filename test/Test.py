import unittest
from controller.CriteriosController import CriteriosController
from controller.EvalController import EvaluadorController
from model.Criterio import Criterio
from model.EvalAnteproy import EvaluacionAnteproyecto
from controller.UsuarioController import UsuarioController
from model.Usuario import Usuario


class MyTestCase(unittest.TestCase):

    def test_agregar_Evaluacion(self):
        Econtroller = EvaluadorController()
        evaluacion = EvaluacionAnteproyecto()
        Econtroller.agregar_evaluacion(evaluacion)
        self.assertIn(evaluacion, Econtroller.evaluaciones)

    def test_agregar_Criterios(self):
        Ccontroller = CriteriosController()
        criterio = Criterio()
        Ccontroller.agregar_criterios(criterio)
        self.assertIn(criterio, Ccontroller.criterios)

    def test_agregar_Usuario(self):
        usuario1 = Usuario()
        usuario1.set_nombre("Juan")
        self.assertEqual("Juan", usuario1.get_nombre())

    def test_Usuario_Tipo(self):
        Ucontroller = UsuarioController()
        Ucontroller.set_tipo(0)
        self.assertEqual(0, Ucontroller.get_tipo())
        Ucontroller.set_tipo(1)
        self.assertEqual(1, Ucontroller.get_tipo())
        Ucontroller.set_tipo(2)
        self.assertEqual(2, Ucontroller.get_tipo())


if __name__ == '__main__':
    unittest.main()
