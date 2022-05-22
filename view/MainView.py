import streamlit as st
import fpdf as pdf
from streamlit_option_menu import option_menu
from controller.EvalController import EvaluadorController
from view.AboutPartial import consultar_instrucciones
from view.EvalPartial import listar_evaluacion, agregar_evaluacion, listar_criterios, crear_criterio, crear_usuario, evaluar_acta, listar_evaluacion_jurados
from controller.CriteriosController import CriteriosController
from controller.UsuarioController import UsuarioController
from model.Criterio import Criterio

class MainView:
    def __init__(self) -> None:
        super().__init__()

        # Estretagia para manejar el "estado" del controllador y del modelo entre cada cambio de ventana
        if 'main_view' not in st.session_state:
            self.menu_actual = "Inicio"
            # Conexión con el controlador
            self.controller = EvaluadorController()
            self.criterio_controller = CriteriosController()
            self.usuario_controller = UsuarioController()


            criterio1 = Criterio()
            criterio1.set_categoria("Desarrollo y profundidad en el tratamiento del tema")
            criterio1.set_ponderacion(20)
            criterio1.set_descripcion("Primer Criterio Creado")
            criterio2 = Criterio()
            criterio2.set_categoria("Desafío académico y científico del tema")
            criterio2.set_ponderacion(15)
            criterio2.set_descripcion("Segundo Criterio Creado")
            criterio3 = Criterio()
            criterio3.set_categoria("Cumplimiento de los objetivos propuestos")
            criterio3.set_ponderacion(10)
            criterio3.set_descripcion("Tercero Criterio Creado")
            criterio4 = Criterio()
            criterio4.set_categoria("Creatividad e innovación de las soluciones y desarrollos propuestos")
            criterio4.set_ponderacion(10)
            criterio4.set_descripcion("Cuarto Criterio Creado")
            criterio5 = Criterio()
            criterio5.set_categoria("Validez de los resultados y conclusiones")
            criterio5.set_ponderacion(20)
            criterio5.set_descripcion("Quinto Criterio Creado")
            criterio6 = Criterio()
            criterio6.set_categoria("Manejo y procesamiento de la información y bibliografía")
            criterio6.set_ponderacion(10)
            criterio6.set_descripcion("sexto Criterio Creado")
            criterio7 = Criterio()
            criterio7.set_categoria("Calidad y presentación del documento escrito")
            criterio7.set_ponderacion(7.5)
            criterio7.set_descripcion("septimo Criterio Creado")
            criterio8 = Criterio()
            criterio8.set_categoria("Presentación oral")
            criterio8.set_ponderacion(7.5)
            criterio8.set_descripcion("octavo Criterio Creado")

            self.criterio_controller.agregar_criterios(criterio1)
            self.criterio_controller.agregar_criterios(criterio2)
            self.criterio_controller.agregar_criterios(criterio3)
            self.criterio_controller.agregar_criterios(criterio4)
            self.criterio_controller.agregar_criterios(criterio5)
            self.criterio_controller.agregar_criterios(criterio6)
            self.criterio_controller.agregar_criterios(criterio7)
            self.criterio_controller.agregar_criterios(criterio8)
            st.session_state['main_view'] = self
        else:

            # Al exisir en la sesión entonces se actualizan los valores
            self.menu_actual = st.session_state.main_view.menu_actual
            self.controller = st.session_state.main_view.controller
            self.criterio_controller = st.session_state.main_view.criterio_controller
            self.usuario_controller = st.session_state.main_view.usuario_controller

        #criterio1 = Criterio("Introduce gradualmente al lector en el escenario donde se presenta el problema y describe características específicas que sean interesantes para entender la problemática (ejm geográficas, culturales, económicas)", "Titulo", 2, 0, " ")
        #criterio2 = Criterio( "Presenta los involucrados en el proyecto (stakeholders) y la  información relevante para entender los stakeholders. Por ejemplo sus condiciones económicas, características culturales, étnicas, su forma de trabajo, etc .", "Interes", 4, 0, " ")
        self._dibujar_layout()

    def _dibujar_layout(self):
        # Set page title, icon, layout wide (more used space in central area) and sidebar initial state
        st.set_page_config(page_title="Trabajo de Grado", page_icon='', layout="wide",
                           initial_sidebar_state="expanded")
        # Defines the number of available columns del area principal
        self.col1, self.col2, self.col3 = st.columns([1, 1, 1])

        # Define lo que abrá en la barra de menu
        with st.sidebar:
            self.menu_actual = option_menu("Menu", ["Inicio", 'Idefintificate', 'Crear Evaluacion', 'Crear Criterios', 'Histórico', 'Editar o Borrar Criterios', 'Calificar Acta', 'Listar Actas'],
                                           icons=['house', 'person', 'plus', 'plus', 'list', 'trash', 'pencil', 'list'], menu_icon="cast", default_index=1)

    def controlar_menu(self):
        """TODO poner aqui su codigo de interaccion"""
        if self.menu_actual == "Inicio":
            texto = consultar_instrucciones()
            st.write(texto)
        elif self.menu_actual == "Idefintificate":
            crear_usuario(st, self.usuario_controller)
        elif self.menu_actual == "Crear Evaluacion":
            if self.usuario_controller.get_verificador() == 1:
                if self.usuario_controller.get_tipo() == 1:
                    agregar_evaluacion(st, self.controller, self.criterio_controller, self.usuario_controller)
                else:
                    st.error("No tienes permiso")
            else:
                st.error("No has iniciado sesión!")
        elif self.menu_actual == "Crear Criterios":
            if self.usuario_controller.get_verificador() == 1:
                if self.usuario_controller.get_tipo() == 2:
                    crear_criterio(st, self.criterio_controller, self.usuario_controller)
                else:
                    st.error("No tienes permiso")
            else:
                st.error("No has iniciado sesión!")
        elif self.menu_actual == "Histórico":
            if self.usuario_controller.get_verificador() == 1:
                if self.usuario_controller.get_tipo() == 2 or self.usuario_controller.get_tipo() == 1:
                    listar_evaluacion(st, self.controller, self.usuario_controller)
                else:
                    st.error("No tienes permiso")
            else:
                st.error("No has iniciado sesión!")
        elif self.menu_actual == "Editar o Borrar Criterios":
            if self.usuario_controller.get_verificador() == 1:
                if self.usuario_controller.get_tipo() == 2:
                    listar_criterios(st, self.criterio_controller, self.usuario_controller)
                else:
                    st.error("No tienes permiso")
            else:
                st.error("No has iniciado sesión!")
        elif self.menu_actual == "Calificar Acta":
            if self.usuario_controller.get_verificador() == 1:
                if self.usuario_controller.get_tipo() == 0:
                    evaluar_acta(st, self.controller, self.usuario_controller)
                else:
                    st.error("No tienes permiso")
            else:
                st.error("No has iniciado sesión!")
        elif self.menu_actual == "Listar Actas":
            if self.usuario_controller.get_verificador() == 1:
                if self.usuario_controller.get_tipo() == 0:
                    listar_evaluacion_jurados(st, pdf, self.controller, self.usuario_controller)
                else:
                    st.error("No tienes permiso")
            else:
                st.error("No has iniciado sesión!")

# Main call
if __name__ == "__main__":
    main = MainView()
    main.controlar_menu()
