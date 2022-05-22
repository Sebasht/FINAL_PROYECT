from model.EvalAnteproy import EvaluacionAnteproyecto
from model.Criterio import Criterio
from model.Usuario import Usuario
from model.PDF import PDF
from PIL import Image

""" Este archivo contine las funcionalidades de la vista relacionado con la evaluacion de los anteproyectos"""


def agregar_evaluacion(st, controller, criterios_controller, usuario_controller):
    col20, col21 = st.columns([10,1])
    with col20:
        st.text("")
    with col21:
        cerrar_sesion = st.button("logout")
        if cerrar_sesion:
            usuario_controller.set_verificador(0)
            st.success("Has cerrado sesion correctamente")
    st.title( "Trabajo de Grado" )
    st.text("")
    st.text("")
    st.subheader("En el siguiente apartado, debes de llenar los datos requeridos de la evaluación")
    st.text("")
    st.text("")

    col1, col2 = st.columns([4, 3])
    img = Image.open("EVALUA.png")
    with col1:
        # Objecto que modelará el formulario
        evaluacion_obj = EvaluacionAnteproyecto()
        evaluacion_obj.set_nombre_estudiante(st.text_input("Nombre estudiante"))
        evaluacion_obj.set_id_acta(st.text_input("Id del Acta"))
        evaluacion_obj.set_fecha_evaluacion(st.text_input("Fecha de evaluacion"))
        tipo_trabajo = st.radio("Indique que tipo de trabajo es:", ('Aplicado', 'Investigacion'))
        if (tipo_trabajo == 'Aplicado'):
            evaluacion_obj.set_tipo_documento("Aplicado")
        elif (tipo_trabajo == 'Investigacion'):
            evaluacion_obj.set_tipo_documento("Investigacion")
        evaluacion_obj.set_nombre_proyecto(st.text_input("Nombre Proyecto"))
        evaluacion_obj.set_director(st.text_input("Director"))
        evaluacion_obj.set_codirector(st.text_input("Codirector"))
        evaluacion_obj.set_jurado1(st.text_input("Jurado 1"))
        evaluacion_obj.set_jurado2(st.text_input("jurado 2"))
        evaluacion_obj.set_lista_criterios(criterios_controller.get_criterios())
    with col2:
        st.image(img, width=650)
    # TODO
    # Agregar campo para leer el tema y la versión de la evaluación del proyecto
    st.text("")
    st.text("")
    st.text("")
    enviado_btn = st.button("Submit")

    # Cuando se oprime el boton se agrega a la lista
    if enviado_btn:
        controller.agregar_evaluacion(evaluacion_obj)
        st.success("Evaluacion agregada exitosamente")
    # Retorna el controlador pq solo las colecciones se pasan en python por referencia,
    # entonces de esta manera se actualiza el controlador en la vista principal
    return controller



def listar_evaluacion(st, controller, usuario_controller):
    col20, col21 = st.columns([10, 1])
    with col20:
        st.text("")
    with col21:
        cerrar_sesion = st.button("logout")
        if cerrar_sesion:
            usuario_controller.set_verificador(0)
            st.success("Has cerrado sesion correctamente")
    st.title("Historico")
    st.text("")
    st.text("")
    st.text("")
    st.text("")
    st.text("")
    st.text("")
    st.text("")
    st.text("A continuación, podrá observar el historial de actas creadas, calificadas o sin calificar")
    st.text("")
    st.text("")
    st.text("")
    st.text("")
    st.text("")
    st.text("")
    st.text("")
    col3, col4, col5, col6, col7, col8, col9, col10, col11, col12 = st.columns([2, 2, 2, 2, 2, 2, 2, 2, 2, 2])
    for evaluacion in controller.get_evaluaciones():
        with col3:
            st.markdown("<h5 style='color: white;'>Identificacion del Acta: </h5>", unsafe_allow_html=True)
            st.write(evaluacion.get_id_acta())
        with col4:
            st.markdown("<h5 style='color: white;'>Nombre del Autor: </h5>", unsafe_allow_html=True)
            st.write(evaluacion.get_nombre_estudiante())
        with col5:
            st.markdown("<h5 style='color: white;'>Nombre del Proyecto: </h5>", unsafe_allow_html=True)
            st.write(evaluacion.get_nombre_proyecto())
        with col6:
            st.markdown("<h5 style='color: white;'>Tipo del Documento: </h5>", unsafe_allow_html=True)
            st.write(evaluacion.get_tipo_documento())
        with col7:
            st.markdown("<h5 style='color: white;'>Fecha de Entrega </h5>", unsafe_allow_html=True)
            st.write(evaluacion.get_fecha_evaluacion())
        with col8:
            st.markdown("<h5 style='color: white;'>Director: </h5>", unsafe_allow_html=True)
            st.write(evaluacion.get_director())
        with col9:
            st.markdown("<h5 style='color: white;'>Codirector: </h5>", unsafe_allow_html=True)
            st.write(evaluacion.get_codirector())
        with col10:
            st.markdown("<h5 style='color: white;'>Jurado 1: </h5>", unsafe_allow_html=True)
            st.write(evaluacion.get_jurado1())
        with col11:
            st.markdown("<h5 style='color: white;'>Jurado 2: </h5>", unsafe_allow_html=True)
            st.write(evaluacion.get_jurado2())
        with col12:
            st.markdown("<h5 style='color: white;'>Nota: </h5>", unsafe_allow_html=True)
            if evaluacion.get_nota() == -1:
                st.text("Sin calificar")
            else:
                st.write(evaluacion.get_nota())
    st.text("")
    st.text("")
    st.text("")
    st.text("")
    st.text("")
    st.text("")
    st.title("Usuarios guardados:")
    st.text("")
    st.text("")
    st.text("")
    st.text("")
    st.text("A continuación, podrá observar la lista de usuarios que han iniciado sesion")
    st.text("")
    st.text("")
    i = 0
    colu,colu1,colu2 = st.columns([1, 4, 4])
    for usuarios in usuario_controller.get_usuarios():
        with colu:
            st.write(i)
        with colu1:
            st.markdown("<h5 style='color: white;'>Nombre del usuario: </h5>", unsafe_allow_html=True)
        with colu2:
            st.write(usuarios.get_nombre())
        i = i + 1

def listar_evaluacion_jurados(st, pdf, controller, usuario_controller):
    col20, col21 = st.columns([10, 1])
    with col20:
        st.text("")
    with col21:
        cerrar_sesion = st.button("logout")
        if cerrar_sesion:
            usuario_controller.set_verificador(0)
            st.success("Has cerrado sesion correctamente")
    st.title("Lista de Actas")
    st.text("")
    st.text("")
    st.text("")
    st.text("")
    st.markdown("<h4 style='text-align: center; color: white;'>Actas Calificadas</h4>", unsafe_allow_html=True)
    st.text(" ")
    st.text(" ")
    st.text(" ")
    st.text(" ")
    col3, col4, col5, col6, col7, col8, col9 = st.columns([1, 4, 3, 3, 3, 2, 2])
    i = 1
    for evaluacion in controller.get_evaluaciones():
        if evaluacion.get_nota() != -1:
            with col3:
                st.markdown("<h5 style='color: white;'>Acta: </h5>", unsafe_allow_html=True)
                st.write(i)
            with col4:
                st.markdown("<h5 style='color: white;'>Identificacion del Acta: </h5>", unsafe_allow_html=True)
                st.write(evaluacion.get_id_acta())
            with col5:
                st.markdown("<h5 style='color: white;'>Nombre del Autor: </h5>", unsafe_allow_html=True)
                st.write(evaluacion.get_nombre_estudiante())
            with col6:
                st.markdown("<h5 style='color: white;'>Nombre del Proyecto: </h5>", unsafe_allow_html=True)
                st.write(evaluacion.get_nombre_proyecto())
            with col7:
                st.markdown("<h5 style='color: white;'>Tipo del Documento: </h5>", unsafe_allow_html=True)
                st.write(evaluacion.get_tipo_documento())
            with col8:
                st.markdown("<h5 style='color: white;'>Nota: </h5>", unsafe_allow_html=True)
                st.write(evaluacion.get_nota())
            with col9:
                st.markdown("<h5 style='color: white;'>Estado: </h5>", unsafe_allow_html=True)
                if evaluacion.get_nota() > 3.5 or evaluacion.get_nota() == 3.5:
                    st.text("Aprobó")
                else:
                    st.text("Reprobó")
            i = i + 1
    st.text(" ")
    st.text(" ")
    st.text(" ")
    st.markdown("<h4 style='color: white;'>¿Desea exportar un acta?: </h4>", unsafe_allow_html=True)
    indice = st.text_input("Acta a calificar")
    exportar = st.button("Exportar")
    if exportar:
        try:
            acta_a_exportar = controller.get_evaluaciones()[int(indice)-1]
            exportar_acta(acta_a_exportar)
            st.success("Acta exportada a pdf correctamente")
        except ValueError as e:
            st.error("Digita un valor valido")

def exportar_acta(acta):
    pdf = PDF()
    pdf.add_page()
    pdf.set_margenes()
    pdf.set_auto_page_break
    pdf.encabezado(acta.get_fecha_evaluacion(), acta.get_id_acta())
    pdf.tittles("ACTA DE EVALUACIÓN DE TRABAJO DE GRADO")
    pdf.texts_proyect_name(acta.get_nombre_proyecto())
    pdf.text_info(acta.get_nombre_estudiante(), acta.get_fecha_evaluacion(), acta.get_director(), acta.get_codirector(), acta.get_tipo_documento(), acta.get_jurado1(), acta.get_jurado2())
    pdf.textss("En atención al desarrollo de este Trabajo de Grado y al documento y sustentación que presentó el(la) autor(a), los Jurados damos las siguientes calificaciones parciales y observaciones (los criterios a evaluar y sus ponderaciones se estipulan en el artículo 7.1 de las Directrices para Trabajo de Grado de Maestría):")
    for i in range(len(acta.get_criterios())):
        pdf.criterios_info(str(i), str(acta.get_criterios()[i].get_ponderacion()), acta.get_criterios()[i].get_observacion_criterio(), acta.get_criterios()[i].get_categoria(), str(acta.get_criterios()[i].get_nota()))
    pdf.espacios()
    pdf.nota_final_info(str(acta.get_nota()))
    pdf.espacios()
    pdf.observaciones_adicionales(acta.get_observacion_final())
    pdf.rayitas_observaciones()
    pdf.espacios()
    pdf.rayitas_firmas()
    pdf.espacios()
    if acta.get_nota() > 4.5 or acta.get_nota == 4.5:
        pdf.tittles("RECOMENDACIÓN DE MENCIÓN DE HONOR AL TRABAJO DE GRADO")
        pdf.texts_proyect_name(acta.get_nombre_proyecto())
        pdf.text_info(acta.get_nombre_estudiante(), acta.get_fecha_evaluacion(), acta.get_director(), acta.get_codirector(), acta.get_tipo_documento(), acta.get_jurado1(), acta.get_jurado2())
        pdf.espacios()
        pdf.textss2("En atención a que el Trabajo de Grado se distingue porque la calificación del trabajo es superior a 4,50 y sedestaca por dos condiciones (que indicamos) de las siguientes tres como se estipula en el artículo 7.6 de las Directrices para Trabajo de Grado de Maestría:")
        pdf.espacios()
        pdf.supero()
    pdf.output('proyecto.pdf', 'F')


def listar_criterios(st, criterio_controller, usuario_controller):
    col20, col21 = st.columns([10, 1])
    with col20:
        st.text("")
    with col21:
        cerrar_sesion = st.button("logout")
        if cerrar_sesion:
            usuario_controller.set_verificador(0)
            st.success("Has cerrado sesion correctamente")
    st.title("Lista criterios")
    st.text("")
    st.text("")
    st.text("")
    st.text("")
    col3, col4, col5, col6 = st.columns([1, 2, 2, 2])
    i = 1
    for criterio in criterio_controller.get_criterios():
        with col3:
            st.markdown("<h5 style='color: white;'>Numero: </h5>", unsafe_allow_html=True)
            st.write(str(i))
        with col4:
            st.markdown("<h5 style='color: white;'>Categoria: </h5>", unsafe_allow_html=True)
            st.write(criterio.get_categoria())
        with col5:
            st.markdown("<h5 style='color: white;'>Descripcion: </h5>", unsafe_allow_html=True)
            st.write(criterio.get_descripcion())
        with col6:
            st.markdown("<h5 style='color: white;'>Porcentaje: </h5>", unsafe_allow_html=True)
            st.write(str(criterio.get_ponderacion()))
        i = i+1
    st.text("")
    st.text("")
    st.text("")
    st.text("")
    st.markdown("<h5 style='color: white;'>¿Desea borrar un Criterio?: </h5>", unsafe_allow_html=True)
    indice = st.text_input("Numero de Criterio")
    delete = st.button("Borrar")
    if delete:
        try:
            del criterio_controller.get_criterios()[int(indice)-1]
            st.success("Se ha borrado el criterio exitosamente")
        except ValueError as e:
            st.error("Digita un valor valido")

    st.markdown("<h5 style='color: white;'>Editar Criterio: </h5>", unsafe_allow_html=True)
    indice2 = st.text_input("Criterio a modificar")
    n_ponderacion = st.text_input("Ponderacion")
    n_descripcion = st.text_input("Descripcion")
    n_categoria = st.text_input("categoria")
    edit = st.button("Edit")
    if edit:
        try:
            criterio_controller.get_criterios()[int(indice2)-1].set_ponderacion(int(n_ponderacion))
            criterio_controller.get_criterios()[int(indice2)-1].set_descripcion(n_descripcion)
            criterio_controller.get_criterios()[int(indice2)-1].set_categoria(n_categoria)
            st.success("Se ha editado el criterio exitosamente")
        except ValueError as e:
            st.error("Digita un valor valido")

def evaluar_acta(st, controller, usuario_controller):
    col20, col21 = st.columns([10, 1])
    with col20:
        st.text("")
    with col21:
        cerrar_sesion = st.button("logout")
        if cerrar_sesion:
            usuario_controller.set_verificador(0)
            st.success("Has cerrado sesion correctamente")
    st.title("Evaluar Acta")
    st.text("")
    st.text("")
    st.text("")
    st.text("")
    st.markdown("<h4 style='text-align: center; color: white;'>Actas sin calificación</h4>", unsafe_allow_html=True)
    col3, col4, col5, col6, col7 = st.columns([2, 2, 2, 2, 2])
    i = 1
    for evaluacion in controller.get_evaluaciones():
        if evaluacion.get_nota() == -1:
            with col3:
                st.markdown("<h5 style='color: white;'>Acta: </h5>", unsafe_allow_html=True)
                st.write(i)
            with col4:
                st.markdown("<h5 style='color: white;'>Identificacion del Acta: </h5>", unsafe_allow_html=True)
                st.write(evaluacion.get_id_acta())
            with col5:
                st.markdown("<h5 style='color: white;'>Nombre del Autor: </h5>", unsafe_allow_html=True)
                st.write(evaluacion.get_nombre_estudiante())
            with col6:
                st.markdown("<h5 style='color: white;'>Nombre del Proyecto: </h5>", unsafe_allow_html=True)
                st.write(evaluacion.get_nombre_proyecto())
            with col7:
                st.markdown("<h5 style='color: white;'>Tipo del Documento: </h5>", unsafe_allow_html=True)
                st.write(evaluacion.get_tipo_documento())
        i = i + 1
    index = st.text_input("Acta a calificar:")

    #index = st.number_input("Acta a calificar", key=1, max_value=len(controller.evaluaciones), min_value=1)
    total_ponderacion = 0
    nota_total = 0

    #calificar = st.button("Calificar")
    #if calificar:
    try:
        for j in range(len(controller.get_evaluaciones()[int(index)-1].get_criterios())):
            st.write(controller.get_evaluaciones()[int(index) - 1].get_criterios()[j].get_categoria())
            st.write(controller.get_evaluaciones()[int(index) - 1].get_criterios()[j].get_ponderacion())
            st.write(controller.get_evaluaciones()[int(index) - 1].get_criterios()[j].get_descripcion())

            controller.get_evaluaciones()[int(index)-1].get_criterios()[j].set_nota_jurado1(st.number_input("Nota Jurado 1: ", key=(j+1)*10,
                                                                                           min_value=0, max_value=5))

            controller.get_evaluaciones()[int(index)-1].get_criterios()[j].set_nota_jurado2(st.number_input("Nota Jurado 2: ", key=(j + 1) * 10,
                                                                                           min_value=0, max_value=5))

            nota_por_criterio = (int(controller.get_evaluaciones()[int(index)-1].get_criterios()[j].get_nota_jurado1()) + int(controller.get_evaluaciones()[int(index)-1].get_criterios()[j].get_nota_jurado2()))/2
            controller.get_evaluaciones()[int(index) - 1].get_criterios()[j].set_nota(nota_por_criterio)

            controller.get_evaluaciones()[int(index)-1].get_criterios()[j].set_observacion_criterio(st.text_input("Observacion:", key=(j + 1)))
            total_ponderacion = total_ponderacion + int(controller.get_evaluaciones()[int(index)-1].get_criterios()[j].get_ponderacion())
            st.write(total_ponderacion)

        for e in range(len(controller.get_evaluaciones()[int(index)-1].get_criterios())):

            nota_promedio = (int(controller.get_evaluaciones()[int(index)-1].get_criterios()[e].get_nota_jurado1()) + int(controller.get_evaluaciones()[int(index)-1].get_criterios()[e].get_nota_jurado2()))/2
            ponderacion_criterio = (int(controller.get_evaluaciones()[int(index)-1].get_criterios()[e].get_ponderacion())/total_ponderacion)
            nota_total = nota_total + (nota_promedio * ponderacion_criterio)

        controller.get_evaluaciones()[int(index) - 1].set_observacion_final(st.text_input("Observacion final del proyecto:"))
        my_round_nota_final = round(nota_total, 2)
        controller.get_evaluaciones()[int(index)-1].set_nota(my_round_nota_final)
        st.text("")
        st.text("")
        st.text("")
        st.text("")
    except ValueError as e:
        if(len(controller.get_evaluaciones()) == 0 ):
            st.error("No hay evaluaciones")
        else:
            st.error("Digita un valor valido")

def crear_criterio(st, criterio_controller, usuario_controller):
    st.title("Crea un criterio")
    st.text("")
    st.text("")
    st.text("")
    st.markdown("<h7 style='color: white;'>En el siguiente apartado, puedes crear un nuevo criterio para la evaluación del estudiante</h7>", unsafe_allow_html=True)
    col20, col21 = st.columns([10, 1])
    with col20:
        st.text("")
    with col21:
        cerrar_sesion = st.button("logout")
        if cerrar_sesion:
            usuario_controller.set_verificador(0)
            st.success("Has cerrado sesion correctamente")
    new_criterio = Criterio()
    new_criterio.set_descripcion(st.text_input("descripcion"))
    new_criterio.set_categoria(st.text_input("categoria"))
    new_criterio.set_ponderacion(st.text_input("ponderacion"))

    st.text("")
    st.text("")
    st.text("")

    enviado_btn = st.button("Submit")
    if enviado_btn:
        criterio_controller.agregar_criterios(new_criterio)
        st.success("Criterio agregado exitosamente")

def verificar_usuario( usuario_controller, name ):
    index = 0
    for usuario in usuario_controller.get_usuarios():
        if usuario.get_nombre() == name:
            usuario_controller.set_index(index-1)
            return 1
        index += 1

def verificar_contraseña( usuario_controller, clave ):
    for usuario in usuario_controller.get_usuarios():
        if usuario.get_contraseña() == clave:
            return 1

def crear_usuario(st, usuario_controller):
    img = Image.open("usuarioimage.png")
    st.markdown("<h2 style='text-align: center; color: white;'>Bienvenido!</h2>", unsafe_allow_html=True)
    st.markdown("<h4 style='text-align: center; color: white;'>Antes de empezar a navegar, porfavor indica quien eres</h4>", unsafe_allow_html=True)
    new_usuario = Usuario()
    col1, col2, col3 = st.columns([7,5,6])
    index = 0
    with col2:
        st.image(img, width=300)
        st.text("")
        st.text("")
        st.text("")
        st.text("")
        st.text("")
        st.text("")
        st.text("")
        st.text("")
    col4, col5, col6 = st.columns([6, 5, 6])
    with col5:
        tipo_usuario = st.radio("Indique que tipo de usuario es:", ('Jurado', 'Asistente', 'Director'))
        if ( tipo_usuario == 'Jurado' ):
            usuario_controller.set_tipo(0)
            st.success("Bienvenido Jurado!")
        elif ( tipo_usuario == 'Asistente'):
            usuario_controller.set_tipo(1)
            st.success("Bienvenido Asistente!")
        else:
            usuario_controller.set_tipo(2)
            st.success("Bienvenido Director!")
        nombre_usuario = st.text_input("Escriba su nombre de Usuario:")
        new_usuario.set_nombre(nombre_usuario)
        new_usuario.set_verificado(verificar_usuario(usuario_controller, nombre_usuario))
        clave_usuario = st.text_input("Escriba su contraseña:")
        new_usuario.set_contraseña(clave_usuario)
        new_usuario.set_verificado_clave(verificar_contraseña(usuario_controller, clave_usuario))
        enviado_usuario = st.button("Submit")
        if enviado_usuario:
            if new_usuario._verificado != 1:
                usuario_controller.agregar_usuario(new_usuario)
                st.success("Usuario Creado exitosamente")
                new_usuario.set_verificado_login(1)
                usuario_controller.set_verificador(1)
            else:
                if new_usuario._verificado_clave != 1:
                    st.error( "Contraseña Incorrecta" )
                    usuario_controller.set_verificador(0)
                else:
                    st.success("Has iniciado sesión!")
                    new_usuario.set_verificado_login(1)
            usuario_controller.set_index(index-1)


#Esta parte de código comentada, tiene la funcionalidad de ver si los datos agregados están siendo guardados (Ya se verficó que es correcto por lo tanto ya no se usará)
#    st.markdown("<h5 style='color: white;'>Usuario: </h5>", unsafe_allow_html=True)
#    st.write(new_usuario._nombre)
#    st.markdown("<h5 style='color: white;'>contraseña: </h5>", unsafe_allow_html=True)
#    st.write(new_usuario._contraseña)
#    st.markdown("<h5 style='color: white;'>Tipo de Usuario: </h5>", unsafe_allow_html=True)
#    st.write(usuario_controller.get_tipo())
#    st.markdown("<h5 style='color: white;'Verificado: </h5>", unsafe_allow_html=True)
#    st.write(new_usuario._verificado)
#    st.markdown("<h5 style='color: white;'login: </h5>", unsafe_allow_html=True)
#    st.write(new_usuario._verificado_login)
