import numpy as np

class Neurona:
    def __init__(self, num_entradas):
        self.pesos = [random.uniform(-1, 1) for _ in range(num_entradas)]
        self.bias = random.uniform(-1, 1)
        self.salida = 0
        self.delta = 0  # Para backpropagation
    
    def funcion_activacion(self, x):
        # Función sigmoide
        return 1 / (1 + math.exp(-max(-500, min(500, x))))  # Limitar para evitar overflow
    
    def derivada_activacion(self, x):
        # Derivada de la sigmoide
        s = self.funcion_activacion(x)
        return s * (1 - s)
    
    def propagar_adelante(self, entradas):
        suma_ponderada = sum(w * e for w, e in zip(self.pesos, entradas)) + self.bias
        self.salida = self.funcion_activacion(suma_ponderada)
        return self.salida

class CapaNeuronal:
    def __init__(self, num_neuronas, num_entradas_por_neurona):
        self.neuronas = [Neurona(num_entradas_por_neurona) for _ in range(num_neuronas)]
    
    def propagar_adelante(self, entradas):
        salidas = []
        for neurona in self.neuronas:
            salida = neurona.propagar_adelante(entradas)
            salidas.append(salida)
        return salidas

class RedNeuronal:
    def __init__(self, arquitectura):
        """
        arquitectura: lista con el número de neuronas por capa
        Ejemplo: [3, 5, 2] = 3 entradas, 5 neuronas ocultas, 2 salidas
        """
        self.capas = []
        for i in range(1, len(arquitectura)):
            num_neuronas = arquitectura[i]
            num_entradas = arquitectura[i-1]
            capa = CapaNeuronal(num_neuronas, num_entradas)
            self.capas.append(capa)
        
        self.tasa_aprendizaje = 0.1
        self.historial_error = []
    
    def propagar_adelante(self, entradas):
        salidas = entradas
        for capa in self.capas:
            salidas = capa.propagar_adelante(salidas)
        return salidas
    
    def calcular_error(self, salidas_esperadas, salidas_obtenidas):
        error = sum((esperada - obtenida) ** 2 
                   for esperada, obtenida in zip(salidas_esperadas, salidas_obtenidas))
        return error / len(salidas_esperadas)
    
    def backpropagation(self, entradas, salidas_esperadas):
        # Propagación hacia adelante
        activaciones = [entradas]
        for capa in self.capas:
            salidas = capa.propagar_adelante(activaciones[-1])
            activaciones.append(salidas)
        
        # Calcular error en capa de salida
        salidas_finales = activaciones[-1]
        for i, neurona in enumerate(self.capas[-1].neuronas):
            error = salidas_esperadas[i] - salidas_finales[i]
            neurona.delta = error * neurona.derivada_activacion(salidas_finales[i])
        
        # Propagar error hacia atrás
        for i in range(len(self.capas) - 2, -1, -1):
            for j, neurona in enumerate(self.capas[i].neuronas):
                error = sum(self.capas[i+1].neuronas[k].delta * self.capas[i+1].neuronas[k].pesos[j]
                           for k in range(len(self.capas[i+1].neuronas)))
                neurona.delta = error * neurona.derivada_activacion(activaciones[i+1][j])
        
        # Actualizar pesos y bias
        for i, capa in enumerate(self.capas):
            for neurona in capa.neuronas:
                for j in range(len(neurona.pesos)):
                    neurona.pesos[j] += self.tasa_aprendizaje * neurona.delta * activaciones[i][j]
                neurona.bias += self.tasa_aprendizaje * neurona.delta
    
    def entrenar(self, datos_entrenamiento, epocas):
        for epoca in range(epocas):
            error_total = 0
            
            for entradas, salidas_esperadas in datos_entrenamiento:
                # Entrenar con un ejemplo
                salidas_obtenidas = self.propagar_adelante(entradas)
                error = self.calcular_error(salidas_esperadas, salidas_obtenidas)
                error_total += error
                
                self.backpropagation(entradas, salidas_esperadas)
            
            error_promedio = error_total / len(datos_entrenamiento)
            self.historial_error.append(error_promedio)
            
            if epoca % 100 == 0:
                print(f"Época {epoca}: Error promedio = {error_promedio:.4f}")
    
    def predecir(self, entradas):
        return self.propagar_adelante(entradas)

class ConjuntoDatos:
    def __init__(self):
        self.datos_entrenamiento = []
        self.datos_prueba = []
    
    def agregar_ejemplo(self, entradas, salidas):
        self.datos_entrenamiento.append((entradas, salidas))
    
    def generar_datos_xor(self, num_ejemplos=1000):
        """Genera datos para el problema XOR"""
        for _ in range(num_ejemplos):
            a = random.choice([0, 1])
            b = random.choice([0, 1])
            resultado = [a ^ b]  # XOR
            self.datos_entrenamiento.append([a, b], resultado)
    
    def normalizar_datos(self):
        """Normaliza los datos de entrada"""
        if not self.datos_entrenamiento:
            return
        
        # Encontrar min y max de cada característica
        num_caracteristicas = len(self.datos_entrenamiento[0][0])
        mins = [float('inf')] * num_caracteristicas
        maxs = [float('-inf')] * num_caracteristicas
        
        for entradas, _ in self.datos_entrenamiento:
            for i, valor in enumerate(entradas):
                mins[i] = min(mins[i], valor)
                maxs[i] = max(maxs[i], valor)
        
        # Normalizar
        datos_normalizados = []
        for entradas, salidas in self.datos_entrenamiento:
            entradas_norm = [(entradas[i] - mins[i]) / (maxs[i] - mins[i]) if maxs[i] != mins[i] else 0
                           for i in range(len(entradas))]
            datos_normalizados.append((entradas_norm, salidas))
        
        self.datos_entrenamiento = datos_normalizados

class ValidadorModelo:
    @staticmethod
    def validacion_cruzada(modelo, datos, k_folds=5):
        """Validación cruzada k-fold"""
        tamaño_fold = len(datos) // k_folds
        errores = []
        
        for i in range(k_folds):
            inicio = i * tamaño_fold
            fin = inicio + tamaño_fold
            
            datos_prueba = datos[inicio:fin]
            datos_entrenamiento = datos[:inicio] + datos[fin:]
            
            # Crear nueva instancia del modelo
            modelo_temp = RedNeuronal([2, 4, 1])  # Ejemplo para XOR
            modelo_temp.entrenar(datos_entrenamiento, 500)
            
            # Evaluar
            error_total = 0
            for entradas, salidas_esperadas in datos_prueba:
                salidas_obtenidas = modelo_temp.predecir(entradas)
                error = modelo_temp.calcular_error(salidas_esperadas, salidas_obtenidas)
                error_total += error
            
            error_promedio = error_total / len(datos_prueba)
            errores.append(error_promedio)
        
        return {
            'errores_por_fold': errores,
            'error_promedio': sum(errores) / len(errores),
            'desviacion_estandar': (sum((e - sum(errores)/len(errores))**2 for e in errores) / len(errores))**0.5
        }