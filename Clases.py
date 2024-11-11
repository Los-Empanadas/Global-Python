#Clases:

#Clase Detector

class Detector:
    def __init__(self, nombre):
        self.nombre = nombre
        
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

class Mutador: 
    def __init__(self,base_nitrogenada):
        pass
    def crear_mutante(self):
        pass
    
#Clase Radiacion    
    
class Radiacion(Mutador):
    def __init__(self, base_nitrogenada):
        super().__init__(base_nitrogenada)
    
    def crear_mutante(self,matriz_ADN,posicion_inicial,orientacion):
        try:
            fila, col = posicion_inicial
            if orientacion == "H":
                for i in range(4):
                    matriz_ADN[fila][col + i] = self.base_nitrogenada
            elif orientacion == "V":
                for i in range(4):
                    matriz_ADN[fila + i][col] = self.base_nitrogenada
            return matriz_ADN
        except (IndexError, TypeError):
            print("Error: Posición fuera de rango o tipo de datos incorrecto.")
            return matriz_ADN
        
#Clase Virus

class Virus(Mutador):
    pass

#Clase Sanador 

class Sanador:
    pass


