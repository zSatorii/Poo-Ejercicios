import math

class SerVivo:
    def __init__(self, especie, energia_inicial, posicion):
        self.id = str(uuid.uuid4())
        self.especie = especie
        self.energia = energia_inicial
        self.energia_maxima = energia_inicial
        self.posicion = posicion  # {"x": float, "y": float}
        self.edad = 0
        self.vivo = True
        self.nivel_trofico = 0  # 1=productor, 2=herbívoro, 3=carnívoro
        self.radio_vision = 10.0
        self.velocidad = 1.0
        self.tasa_reproduccion = 0.1
        
    def mover(self, nueva_posicion):
        distancia = self.calcular_distancia(self.posicion, nueva_posicion)
        energia_consumida = distancia * 0.1
        
        if self.energia > energia_consumida:
            self.posicion = nueva_posicion
            self.energia -= energia_consumida
    
    def calcular_distancia(self, pos1, pos2):
        return math.sqrt((pos1["x"] - pos2["x"])**2 + (pos1["y"] - pos2["y"])**2)
    
    def envejecer(self):
        self.edad += 1
        self.energia -= 1  # Metabolismo básico
        if self.energia <= 0:
            self.morir()
    
    def morir(self):
        self.vivo = False
        self.energia = 0
    
    def puede_reproducirse(self):
        return self.vivo and self.energia > self.energia_maxima * 0.7 and self.edad > 5

class Planta(SerVivo):
    def __init__(self, especie, energia_inicial, posicion, tasa_fotosintesis):
        super().__init__(especie, energia_inicial, posicion)
        self.nivel_trofico = 1
        self.tasa_fotosintesis = tasa_fotosintesis
        self.velocidad = 0  # Las plantas no se mueven
        self.radio_vision = 0
    
    def realizar_fotosintesis(self, luz_disponible):
        energia_producida = self.tasa_fotosintesis * luz_disponible
        self.energia = min(self.energia_maxima, self.energia + energia_producida)
    
    def ser_consumida(self, cantidad):
        energia_perdida = min(self.energia, cantidad)
        self.energia -= energia_perdida
        if self.energia <= 0:
            self.morir()
        return energia_perdida

class Animal(SerVivo):
    def __init__(self, especie, energia_inicial, posicion, dieta):
        super().__init__(especie, energia_inicial, posicion)
        self.dieta = dieta  # "herbivoro", "carnivoro", "omnivoro"
        self.nivel_trofico = 2 if dieta == "herbivoro" else 3
        self.presas_preferidas = []
        self.depredadores = []
        self.hambre = 0
    
    def buscar_alimento(self, ecosistema):
        alimentos_cercanos = []
        
        for ser in ecosistema.seres_vivos:
            if ser.vivo and ser != self:
                distancia = self.calcular_distancia(self.posicion, ser.posicion)
                if distancia <= self.radio_vision:
                    if self.puede_comer(ser):
                        alimentos_cercanos.append((ser, distancia))
        
        if alimentos_cercanos:
            # Ir hacia el alimento más cercano
            objetivo, _ = min(alimentos_cercanos, key=lambda x: x[1])
            return objetivo
        return None
    
    def puede_comer(self, ser):
        if self.dieta == "herbivoro":
            return isinstance(ser, Planta)
        elif self.dieta == "carnivoro":
            return isinstance(ser, Animal) and ser.nivel_trofico < self.nivel_trofico
        else:  # omnívoro
            return isinstance(ser, (Planta, Animal))
    
    def cazar(self, presa):
        if self.puede_comer(presa):
            distancia = self.calcular_distancia(self.posicion, presa.posicion)
            if distancia <= 2.0:  # Distancia de ataque
                if isinstance(presa, Planta):
                    energia_obtenida = presa.ser_consumida(20)
                else:  # Animal
                    energia_obtenida = presa.energia * 0.3  # Eficiencia trófica
                    presa.energia -= energia_obtenida
                    if presa.energia <= 0:
                        presa.morir()
                
                self.energia += energia_obtenida * 0.1  # Solo 10% se aprovecha
                self.hambre = 0
                return True
        return False
    
    def reproducirse(self, pareja=None):
        if self.puede_reproducirse():
            energia_cria = self.energia * 0.3
            self.energia -= energia_cria
            
            # Crear nueva cría cerca de los padres
            nueva_posicion = {
                "x": self.posicion["x"] + random.uniform(-5, 5),
                "y": self.posicion["y"] + random.uniform(-5, 5)
            }
            
            cria = Animal(self.especie, energia_cria, nueva_posicion, self.dieta)
            return cria
        return None

class Ambiente:
    def __init__(self, tamaño_x, tamaño_y, temperatura, humedad):
        self.tamaño_x = tamaño_x
        self.tamaño_y = tamaño_y
        self.temperatura = temperatura  # Celsius
        self.humedad = humedad  # Porcentaje
        self.luz_solar = 100  # Porcentaje
        self.estacion = "primavera"
        self.clima = "templado"
        
    def cambiar_estacion(self):
        estaciones = ["primavera", "verano", "otoño", "invierno"]
        indice_actual = estaciones.index(self.estacion)
        self.estacion = estaciones[(indice_actual + 1) % 4]
        
        # Ajustar parámetros según la estación
        if self.estacion == "invierno":
            self.temperatura -= 10
            self.luz_solar = 60
        elif self.estacion == "verano":
            self.temperatura += 10
            self.luz_solar = 120
        else:
            self.temperatura = 20
            self.luz_solar = 100
    
    def evento_climatico(self, tipo):
        if tipo == "sequía":
            self.humedad *= 0.5
            self.luz_solar *= 1.2
        elif tipo == "lluvia":
            self.humedad = min(100, self.humedad * 1.5)
        elif tipo == "tormenta":
            self.temperatura -= 5
            self.humedad = 100

class CadenaAlimenticia:
    def __init__(self):
        self.relaciones = {}  # {especie_depredador: [especies_presa]}
        self.flujos_energia = {}
        
    def agregar_relacion(self, depredador, presa):
        if depredador not in self.relaciones:
            self.relaciones[depredador] = []
        if presa not in self.relaciones[depredador]:
            self.relaciones[depredador].append(presa)
    
    def calcular_flujo_energia(self, ecosistema):
        # Calcular transferencia de energía entre niveles tróficos
        niveles = {1: 0, 2: 0, 3: 0}  # productores, herbívoros, carnívoros
        
        for ser in ecosistema.seres_vivos:
            if ser.vivo:
                niveles[ser.nivel_trofico] += ser.energia
        
        return niveles

class EcosistemaSimulador:
    def __init__(self, ambiente):
        self.ambiente = ambiente
        self.seres_vivos = []
        self.cadena_alimenticia = CadenaAlimenticia()
        self.tiempo = 0
        self.estadisticas = {"poblaciones": {}, "energia_total": 0}
        self.eventos_programados = []
    
    def agregar_ser_vivo(self, ser):
        self.seres_vivos.append(ser)
    
    def simular_paso_tiempo(self):
        self.tiempo += 1
        
        # Envejecer todos los seres
        for ser in self.seres_vivos:
            if ser.vivo:
                ser.envejecer()
        
        # Fotosíntesis para plantas
        for ser in self.seres_vivos:
            if isinstance(ser, Planta) and ser.vivo:
                ser.realizar_fotosintesis(self.ambiente.luz_solar / 100)
        
        # Comportamiento animal
        for ser in self.seres_vivos:
            if isinstance(ser, Animal) and ser.vivo:
                # Buscar alimento
                alimento = ser.buscar_alimento(self)
                if alimento:
                    # Moverse hacia el alimento
                    nueva_pos = {
                        "x": ser.posicion["x"] + (alimento.posicion["x"] - ser.posicion["x"]) * 0.1,
                        "y": ser.posicion["y"] + (alimento.posicion["y"] - ser.posicion["y"]) * 0.1
                    }
                    ser.mover(nueva_pos)
                    
                    # Intentar cazar
                    ser.cazar(alimento)
                else:
                    # Movimiento aleatorio
                    nueva_pos = {
                        "x": ser.posicion["x"] + random.uniform(-ser.velocidad, ser.velocidad),
                        "y": ser.posicion["y"] + random.uniform(-ser.velocidad, ser.velocidad)
                    }
                    ser.mover(nueva_pos)
                
                # Reproducción
                if random.random() < ser.tasa_reproduccion:
                    cria = ser.reproducirse()
                    if cria:
                        self.agregar_ser_vivo(cria)
        
        # Remover seres muertos
        self.seres_vivos = [ser for ser in self.seres_vivos if ser.vivo]
        
        # Cambios ambientales
        if self.tiempo % 365 == 0:  # Cada año
            self.ambiente.cambiar_estacion()
        
        # Actualizar estadísticas
        self.actualizar_estadisticas()
    
    def actualizar_estadisticas(self):
        poblaciones = {}
        energia_total = 0
        
        for ser in self.seres_vivos:
            if ser.vivo:
                if ser.especie not in poblaciones:
                    poblaciones[ser.especie] = 0
                poblaciones[ser.especie] += 1
                energia_total += ser.energia
        
        self.estadisticas = {
            "poblaciones": poblaciones,
            "energia_total": energia_total,
            "tiempo": self.tiempo,
            "temperatura": self.ambiente.temperatura
        }
    
    def ejecutar_simulacion(self, pasos):
        resultados = []
        for _ in range(pasos):
            self.simular_paso_tiempo()
            resultados.append(dict(self.estadisticas))
        return resultados