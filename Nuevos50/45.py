class PacienteHospital:
    def __init__(self, nombre, cedula, fecha_nacimiento, tipo_sangre):
        self.id = str(uuid.uuid4())
        self.nombre = nombre
        self.cedula = cedula
        self.fecha_nacimiento = fecha_nacimiento
        self.tipo_sangre = tipo_sangre
        self.historial_medico = []
        self.internaciones = []
        self.tratamientos_activos = []
        self.alergias = []
        self.contacto_emergencia = {}

class DoctorHospital:
    def __init__(self, nombre, especialidad, numero_licencia):
        self.id = str(uuid.uuid4())
        self.nombre = nombre
        self.especialidad = especialidad
        self.numero_licencia = numero_licencia
        self.pacientes_asignados = []
        self.turnos = []
        self.disponible = True

class Departamento:
    def __init__(self, nombre, jefe_departamento):
        self.nombre = nombre
        self.jefe_departamento = jefe_departamento
        self.doctores = [jefe_departamento]
        self.camas = []
        self.equipos_medicos = []
        self.presupuesto = 0

class Tratamiento:
    def __init__(self, paciente, doctor, diagnostico, medicamentos, duracion_dias):
        self.id = str(uuid.uuid4())
        self.paciente = paciente
        self.doctor = doctor
        self.diagnostico = diagnostico
        self.medicamentos = medicamentos
        self.duracion_dias = duracion_dias
        self.fecha_inicio = datetime.now()
        self.fecha_fin = datetime.now() + timedelta(days=duracion_dias)
        self.estado = "activo"
        self.notas_seguimiento = []
    
    def agregar_seguimiento(self, nota):
        self.notas_seguimiento.append({
            'fecha': datetime.now(),
            'nota': nota,
            'doctor': self.doctor.nombre
        })

class HistorialMedico:
    def __init__(self, paciente):
        self.paciente = paciente
        self.entradas = []
    
    def agregar_entrada(self, tipo, descripcion, doctor, fecha=None):
        entrada = {
            'id': str(uuid.uuid4()),
            'tipo': tipo,  # consulta, tratamiento, cirugia, emergencia
            'descripcion': descripcion,
            'doctor': doctor,
            'fecha': fecha or datetime.now()
        }
        self.entradas.append(entrada)
        return entrada
    
    def buscar_por_tipo(self, tipo):
        return [e for e in self.entradas if e['tipo'] == tipo]

class SistemaHospitalario:
    def __init__(self, nombre_hospital):
        self.nombre_hospital = nombre_hospital
        self.pacientes = {}
        self.doctores = {}
        self.departamentos = {}
        self.citas_programadas = []
        self.emergencias_activas = []
    
    def admitir_paciente(self, paciente, departamento, tipo_admision="consulta"):
        admision = {
            'paciente': paciente,
            'departamento': departamento,
            'tipo': tipo_admision,
            'fecha_admision': datetime.now(),
            'estado': 'activo'
        }
        
        if tipo_admision == "emergencia":
            self.emergencias_activas.append(admision)
        
        return admision
    
    def asignar_cama(self, paciente, departamento):
        camas_disponibles = [c for c in departamento.camas if c['disponible']]
        if camas_disponibles:
            cama = camas_disponibles[0]
            cama['disponible'] = False
            cama['paciente'] = paciente
            return cama
        return None
