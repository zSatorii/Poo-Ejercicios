class Curso:
    def __init__(self, titulo, descripcion, instructor, precio):
        self.id = str(uuid.uuid4())
        self.titulo = titulo
        self.descripcion = descripcion
        self.instructor = instructor
        self.precio = precio
        self.modulos = []
        self.estudiantes_inscritos = []
        self.calificaciones = []
    
    def agregar_modulo(self, modulo):
        self.modulos.append(modulo)
    
    def inscribir_estudiante(self, estudiante):
        if estudiante not in self.estudiantes_inscritos:
            self.estudiantes_inscritos.append(estudiante)
            estudiante.cursos_inscritos.append(self)

class Modulo:
    def __init__(self, titulo, descripcion, orden):
        self.titulo = titulo
        self.descripcion = descripcion
        self.orden = orden
        self.lecciones = []
    
    def agregar_leccion(self, leccion):
        self.lecciones.append(leccion)

class Leccion:
    def __init__(self, titulo, contenido, tipo, duracion):
        self.titulo = titulo
        self.contenido = contenido
        self.tipo = tipo  # video, texto, quiz
        self.duracion = duracion  # en minutos
        self.completada_por = set()
    
    def marcar_completada(self, estudiante):
        self.completada_por.add(estudiante.id)

class EstudianteCurso:
    def __init__(self, nombre, email):
        self.id = str(uuid.uuid4())
        self.nombre = nombre
        self.email = email
        self.cursos_inscritos = []
        self.progreso = {}  # curso_id: porcentaje_completado
        self.certificados = []
    
    def calcular_progreso(self, curso):
        total_lecciones = sum(len(modulo.lecciones) for modulo in curso.modulos)
        lecciones_completadas = sum(
            1 for modulo in curso.modulos 
            for leccion in modulo.lecciones 
            if self.id in leccion.completada_por
        )
        return (lecciones_completadas / total_lecciones * 100) if total_lecciones > 0 else 0
    
    def obtener_certificado(self, curso):
        progreso = self.calcular_progreso(curso)
        if progreso >= 80:  # 80% para certificado
            certificado = {
                'curso': curso.titulo,
                'estudiante': self.nombre,
                'fecha': datetime.now(),
                'id_certificado': str(uuid.uuid4())
            }
            self.certificados.append(certificado)
            return certificado
        return None
