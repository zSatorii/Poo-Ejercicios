class Candidato:
    def __init__(self, nombre, partido, propuestas):
        self.nombre = nombre
        self.partido = partido
        self.propuestas = propuestas
        self.votos = 0
    
    def obtener_votos(self):
        return self.votos
    
    def agregar_voto(self):
        self.votos += 1

class Votante:
    def __init__(self, nombre, cedula, edad):
        self.nombre = nombre
        self.cedula = cedula
        self.edad = edad
        self.ha_votado = False
        self.elegible = self.edad >= 18
    
    def puede_votar(self):
        return self.elegible and not self.ha_votado
    
    def votar(self, candidato):
        if self.puede_votar():
            candidato.agregar_voto()
            self.ha_votado = True
            return True
        return False

class Eleccion:
    def __init__(self, nombre, fecha):
        self.nombre = nombre
        self.fecha = fecha
        self.candidatos = []
        self.votantes_registrados = {}
        self.votos_emitidos = 0
        self.activa = False
    
    def agregar_candidato(self, candidato):
        self.candidatos.append(candidato)
    
    def registrar_votante(self, votante):
        if votante.elegible:
            self.votantes_registrados[votante.cedula] = votante
            return True
        return False
    
    def procesar_voto(self, cedula_votante, nombre_candidato):
        if cedula_votante in self.votantes_registrados and self.activa:
            votante = self.votantes_registrados[cedula_votante]
            candidato = next((c for c in self.candidatos if c.nombre == nombre_candidato), None)
            
            if candidato and votante.votar(candidato):
                self.votos_emitidos += 1
                return f"Voto registrado para {nombre_candidato}"
        return "Voto no válido"
    
    def obtener_resultados(self):
        resultados = []
        for candidato in self.candidatos:
            porcentaje = (candidato.votos / self.votos_emitidos * 100) if self.votos_emitidos > 0 else 0
            resultados.append({
                'candidato': candidato.nombre,
                'partido': candidato.partido,
                'votos': candidato.votos,
                'porcentaje': porcentaje
            })
        
        return sorted(resultados, key=lambda x: x['votos'], reverse=True)

class SistemaVotacion:
    def __init__(self):
        self.elecciones = {}
        self.votantes = {}
    
    def crear_eleccion(self, eleccion):
        self.elecciones[eleccion.nombre] = eleccion
    
    def iniciar_votacion(self, nombre_eleccion):
        if nombre_eleccion in self.elecciones:
            self.elecciones[nombre_eleccion].activa = True
            return f"Votación '{nombre_eleccion}' iniciada"
        return "Elección no encontrada"
    
    def cerrar_votacion(self, nombre_eleccion):
        if nombre_eleccion in self.elecciones:
            self.elecciones[nombre_eleccion].activa = False
            return self.elecciones[nombre_eleccion].obtener_resultados()
        return "Elección no encontrada"