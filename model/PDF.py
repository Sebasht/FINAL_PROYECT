from fpdf import FPDF

class PDF(FPDF):

    pass
    PDF = FPDF(orientation='p', unit='mm', format='Letter')
    def set_margenes(self):
        self.set_margins(5,5,5)

    def texts_proyect_name(self, proyect_name):
        self.set_text_color(0,0,0)
        self.set_font('Arial', '', 14)
        self.cell(10, 10, txt='Trabajo de grado denominado: "' + proyect_name + '"', ln=1, align='L')

    def textss(self, text):
        self.set_xy(10.0, 160.0)
        self.set_text_color(0,0,0)
        self.set_font('Arial', '', 14)
        self.multi_cell(200, 5, text, ln=1, align='L')

    def textss2(self, text):
        self.set_text_color(0,0,0)
        self.set_font('Arial', '', 14)
        self.multi_cell(200, 5, text, ln=1, align='L')

    def supero(self):
        self.set_text_color(0, 0, 0)
        self.set_font('Arial', '', 14)
        self.multi_cell(200, 10, txt='El estudiante superó los objetivos propuestos: __________', ln=1, align='L')
        self.multi_cell(200, 10, txt='El estudiante demostró una profundidad destacable en el conocimiento y tratamiento del tema: __________', ln=1, align='L')
        self.cell(100, 10, txt='El tema ofrecía una dificultad superior a lo ordinario: __________', ln=1, align='L')
        self.multi_cell(200, 10, txt='Los Jurados recomendamos que el Consejo de la Facultad otorgue Mención de Honor a este Trabajo de Grado, y motivamos esta recomendación con base en las siguientes apreciaciones:', ln=1, align='L')
        self.cell(100, 10, txt='____________________________________________________________________________________________', ln=1, align='L')
        self.cell(190, 10, txt='                      ', ln=1, align='C')
        self.cell(190, 10, txt='                      ', ln=1, align='C')
        self.cell(190, 10, txt='                      ', ln=1, align='C')
        self.cell(190, 10, txt='                      ', ln=1, align='C')
        self.cell(200, 10, txt='         -----------------------------------------                 ------------------------------------------', ln=1, align='L')
        self.cell(200, 10, txt='                      Firma Jurado1                                               Firma Jurado2', ln=1, align='L')

    def criterios_info(self, index, ponderacion, observacion, titulo_criterio, nota):
        self.set_text_color(0, 0, 0)
        self.set_font('Arial', '', 14)
        self.cell(20, 10, txt='' + index + '.', ln=0, align='L', border=0)
        self.set_font('Arial', 'B', 14)
        self.cell(100, 10, titulo_criterio, ln=1, align='L', border=0)
        self.set_font('Arial', '', 14)
        self.cell(170, 10, txt='Calificación parcial: ' + nota, ln=0, align='L', border=0)
        self.cell(10, 10, txt='ponderación: ' + ponderacion, ln=1, align='R', border=0)
        self.multi_cell(200, 10, observacion, 'B', ln=1, align='L')

    def espacios(self):
        self.cell(200,5, txt='                 ', ln=1, align='L', border=0)
        self.cell(200, 5, txt='                 ', ln=1, align='L', border=0)

    def nota_final_info(self, nota):
        self.set_font('Arial', 'B', 14)
        self.multi_cell(200, 5, txt='Como resultado de estas calificaciones parciales y sus ponderaciones, la calificación del Trabajo de grado es: ' + nota, ln=2, align='L', border=0)

    def observaciones_adicionales(self, observacion):
        self.set_font('Arial', '', 14)
        self.multi_cell(200, 5, txt='Observaciones adicionales: ' + observacion, ln=1, align='L', border=0)

    def rayitas_observaciones(self):
        self.set_font('Arial', '', 14)
        self.multi_cell(200, 10, txt='------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------', ln=1, align='L', border=0)

    def text_info(self, autor,fecha,director, codirector, tipo_doc, jurado1, jurado2):
        self.set_text_color(0, 0, 0)
        self.set_font('Arial', '', 14)
        self.cell(40, 10, txt='Autor:     ' + autor, ln=1, align='L', border=0)
        self.cell(50, 10, txt='Fecha:     ' + fecha, ln=1, align='L')
        self.cell(100, 10, txt='Director:     ' + director, ln=1, align='L')
        self.cell(40, 10, txt='Codirector:     ' + codirector, ln=1, align='L')
        self.cell(50, 10, txt='Modalidad:     ' + tipo_doc, ln=1, align='L')
        self.cell(100, 10, txt='Jurado 1:     ' + jurado1, ln=1, align='L')
        self.cell(40, 10, txt='Jurado 2:     ' + jurado2, ln=1, align='L')

    def tittles(self, tittle):

        self.set_font('Arial','B', 16)
        self.set_text_color(0, 0, 0)
        self.cell(w=200.0, h=10.0, align='C', txt=tittle, ln=1, border=0)

    def tittles2(self, tittle):
        self.set_font('Arial','B', 16)
        self.set_text_color(0, 0, 0)
        self.cell(w=200.0, h=20.0, align='C', txt=tittle,ln=1, border=0)

    def rayitas_firmas(self):

        self.cell(200, 10, txt='         -----------------------------------------                 ------------------------------------------', ln=1, align='L')
        self.cell(200, 10, txt='                      Firma Jurado1                                               Firma Jurado2', ln=1, align='L')

    def encabezado(self, fecha, num_acta):
        self.image('PUJ-Logo-vertical.png', 5,5,35,35)
        self.set_xy(5,5)
        self.set_text_color(0, 0, 0)
        self.set_font('Arial', 'B', 16)
        self.cell(190, 10, txt='Facultad de Ingeniería', ln=1, align='C')
        self.cell(190, 10, txt='Maestría en Ingeniería', ln=2, align='C')
        self.cell(190, 10, txt='                      ', ln=1, align='C')
        self.cell(190, 10, txt='                      ', ln=1, align='C')
        self.set_font('Arial', 'B', 11)
        self.cell(150, 10, txt='ACTA:'+ num_acta, ln=0, align='L')
        self.cell(16, 10, txt='Fecha:' + fecha, ln=1, align='L')


