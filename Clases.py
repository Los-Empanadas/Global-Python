import random
# Clases:

# Clase Detector

class Detector:
    def __init__(self,nombre,deteccion):
        self.nombre = nombre
        self.deteccion = deteccion
    def detectar_mutantes(self, matriz_ADN):
        
        #Detecta mutantes en la matriz de ADN en horizontal, vertical o diagonal#
        if(self._detectar_horizontal(matriz_ADN)):
            return 1
        elif(self._detectar_vertical(matriz_ADN)):
            return 2
        elif(self._detectar_diagonal(matriz_ADN)):
            return 3
        else: return 0

    def _detectar_horizontal(self, matriz_ADN):
        
        ###Detecta mutantes en horizontal de la matriz ADN###
        
        for fila in matriz_ADN:
            for i in range(3):
                if fila[i] == fila[i + 1] == fila[i + 2] == fila[i + 3]:
                    return True
        return False

    def _detectar_vertical(self, matriz_ADN):
        
        ###Detecta mutantes en vertical de la matriz ADN###
        
        for col in range(6):
            for fila in range(3):
                if (matriz_ADN[fila][col] == matriz_ADN[fila + 1][col] ==
                        matriz_ADN[fila + 2][col] == matriz_ADN[fila + 3][col]):
                    return True
        return False

    def _detectar_diagonal(self, matriz_ADN):
        
        ###Detecta mutantes en diagonal de la matriz ADN###
        
        for i in range(3):
            for j in range(3):
                if (matriz_ADN[i][j] == matriz_ADN[i + 1][j + 1] == 
                    matriz_ADN[i + 2][j + 2] == matriz_ADN[i + 3][j + 3]):
                    return True
                if (matriz_ADN[i][j + 3] == matriz_ADN[i + 1][j + 2] ==
                        matriz_ADN[i + 2][j + 1] == matriz_ADN[i + 3][j]):
                    return True
        return False

# Clase Mutador

class Mutador: 
    def __init__(self,nombre,tarea):
        self.nombre=nombre
        self.tarea=tarea
    def crear_mutante(self):
        pass
    
#Clase Radiacion    
    
class Radiacion(Mutador):
    def __init__(self,nombre, base_nitrogenada):
        super().__init__(nombre,"Mutar")
        self.base_nitrogenada=base_nitrogenada
        
        
        
    def crear_mutante(self, matriz_adn, posicion_inicial,orientacion):
        
        fila, columna = posicion_inicial

        try:
            # Verificar la orientacion elegida
            if orientacion=="H":
                fila_mod=list(matriz_adn[fila])
                for i in range(4):
                    fila_mod[columna+i]=self.base_nitrogenada
                matriz_adn[fila]="".join(fila_mod)
                
                return matriz_adn
            elif orientacion=="V":
                
                for i in range(4):
                    fila_actual=list(matriz_adn[fila+i])
                    fila_actual[columna]=self.base_nitrogenada
                    matriz_adn[fila+i]="".join(fila_actual)
                    
                return matriz_adn
        except IndexError as e:
            print(f"Error de índice al intentar crear la mutación: {e}")
            return matriz_adn  # Retorna la matriz sin cambios si ocurre un error

        
# Clase Virus

class Virus(Mutador):
    def __init__(self,nombre,base_nitrogenada,orientacion):
        super().__init__(nombre,"Mutar")
        self.tipo_mutacion = orientacion
        self.base_nitrogenada = base_nitrogenada

    def crear_mutante(self, matriz_adn, posicion_inicial):
        """
        Crea una mutación diagonal en la matriz de ADN, repitiendo la base nitrogenada 4 veces.

        Argumentos:
        matriz_adn -- lista de strings representando la matriz de ADN.
        posicion_inicial -- tupla (fila, columna) indicando dónde empezar la mutación.

        Retorna:
        La matriz de ADN con la mutación diagonal aplicada, o la matriz original si hubo un error.
        """
        fila, columna = posicion_inicial

        try:
            # Verificar que la mutación cabe en una diagonal (requiere espacio de 4 posiciones)
            if fila + 3 < 6 and columna + 3 < 6:
                # Crear la mutación diagonal
                for i in range(4):
                    # Convertir la fila en una lista para modificarla
                    fila_actual = list(matriz_adn[fila + i])
                    fila_actual[columna + i] = self.base_nitrogenada
                    # Volver a unir la fila y actualizar en la matriz
                    matriz_adn[fila + i] = "".join(fila_actual)
                return matriz_adn
            else:
                print("Error: la posición inicial no permite una mutación diagonal completa.")
                return matriz_adn  # Retorna la matriz sin cambios si no cabe la mutación
        except IndexError as e:
            print(f"Error de índice al intentar crear la mutación: {e}")
            return matriz_adn  # Retorna la matriz sin cambios si ocurre un error

# Clase Sanador 

class Sanador:
    def __init__(self,nombre,bases):
        self.nombre = nombre
        self.bases = bases  # Bases nitrogenadas posibles

    def sanar_mutantes(self, matriz_adn, detector):
        """
        Revisa la matriz de ADN para ver si tiene mutaciones.
        Si hay mutaciones, genera una nueva matriz de ADN sin mutaciones.

        Argumentos:
        matriz_adn -- lista de strings representando la matriz de ADN.
        detector -- instancia de la clase Detector para usar su método de detección.

        Retorna:
        Una nueva matriz sin mutaciones si había mutantes, o la matriz original si no los había.
        """
        # Verificar si la matriz de ADN actual tiene mutantes
        if detector.detectar_mutantes(matriz_adn):
            print("Mutaciones detectadas. Generando nueva secuencia de ADN sin mutaciones.")
            # Generar una nueva matriz de ADN sin mutantes
            matriz_adn_nueva = self.generar_adn_sin_mutantes(detector)
            return matriz_adn_nueva
        else:
            print("No se detectaron mutaciones. La matriz de ADN está intacta.")
            return matriz_adn  # No hay mutantes, retornamos la matriz original

    def generar_adn_sin_mutantes(self, detector):
        """
        Genera una nueva matriz de ADN de 6x6 sin mutaciones.

        Argumentos:
        detector -- instancia de la clase Detector para verificar la nueva matriz.

        Retorna:
        Una matriz de ADN sin mutantes.
        """
        self.bases = ["A","T","G","C"]
        while True:
            # Crear una matriz aleatoria de 6x6 sin mutantes
            matriz_adn = ["".join(random.choice(self.bases) for _ in range(6)) for _ in range(6)]
            # Verificar si la nueva matriz tiene mutantes
            if not detector.detectar_mutantes(matriz_adn):
                return matriz_adn