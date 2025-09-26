class Paciente:
    def __init__(self, nombre, id_paciente, fecha_nacimiento):
        self.nombre = nombre
        self.id_paciente = id_paciente
        self.fecha_nacimiento = fecha_nacimiento
        self.historial_medico = []
        self.citas = []
    
    def agregar_historial(self, entrada):
        entrada['fecha'] = datetime.now()
        self.historial_medico.append(entrada)

class Doctor:
    def __init__(self, nombre, especialidad, id_doctor):
        self.nombre = nombre
        self.especialidad = especialidad
        self.id_doctor = id_doctor
        self.horarios_disponibles = []
        self.citas = []
    
    def agregar_horario(self, dia, hora_inicio, hora_fin):
        self.horarios_disponibles.append({
            'dia': dia,
            'hora_inicio': hora_inicio,
            'hora_fin': hora_fin
        })
    
    def esta_disponible(self, fecha, hora):
        # Verificar si tiene cita en esa fecha/hora
        for cita in self.citas:
            if cita.fecha.date() == fecha and cita.hora == hora:
                return False
        return True

class Cita:
    def __init__(self, paciente, doctor, fecha, hora, motivo):
        self.paciente = paciente
        self.doctor = doctor
        self.fecha = fecha
        self.hora = hora
        self.motivo = motivo
        self.estado = "programada"
        self.notas = ""
    
    def completar_cita(self, diagnostico, tratamiento):
        self.estado = "completada"
        self.notas = f"Diagnóstico: {diagnostico}, Tratamiento: {tratamiento}"
        
        # Agregar al historial del paciente
        self.paciente.agregar_historial({
            'tipo': 'consulta',
            'doctor': self.doctor.nombre,
            'diagnostico': diagnostico,
            'tratamiento': tratamiento
        })

class ClinicaMedica:
    def __init__(self):
        self.pacientes = {}
        self.doctores = {}
        self.citas = []
    
    def programar_cita(self, id_paciente, id_doctor, fecha, hora, motivo):
        if id_paciente in self.pacientes and id_doctor in self.doctores:
            paciente = self.pacientes[id_paciente]
            doctor = self.doctores[id_doctor]
            
            if doctor.esta_disponible(fecha, hora):
                cita = Cita(paciente, doctor, fecha, hora, motivo)
                paciente.citas.append(cita)
                doctor.citas.append(cita)
                self.citas.append(cita)
                return cita
        return None
