#Clases:

class Detector:
    def __init__(self, nombre):
        self.nombre = nombre
        
    def detectar_mutantes(self, matriz_ADN):
        
        ###Detecta mutantes en la matriz de ADN en horizontal, vertical o diagonal###
        
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

detector=Detector("Detector")


### Interfaz Laboratorio ###


print("----------------------------------\n-Bienvenido al laboratorio de ADN-\n----------------------------------\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("Nos encantaria saber con que cadena de ADN te podemos ayudar, inteoducir dicha cadena como aparese en el siguiente ejemplo:\n *GTACGT CTGATA AGGCAG GCATCG TGAGCG GCTACT*\nCada cadena debe estar compuesta por 6 bases nitrogenadas y separadas por un espacio en blanco al completar las 6.\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

#Ingresar Cadena de ADN

while True:
    Cad_ADN=input("Ingrese su Cadena de ADN:")
    Cad_ADN=Cad_ADN.upper()
    bases_nit_ADN = list(Cad_ADN.replace(" ", ""))
    matriz_ADN = Cad_ADN.split()
    if len(Cad_ADN.replace(" ", "")) == 36 and all(base in 'CATG' for base in bases_nit_ADN) and all(len(parte) == 6 for parte in matriz_ADN):   
        break
    else:
        print("*********************************************\nError: Su cadena esta mal formulada revise el ejemplo proporcionado y compruebe si no tiene uno de los siguientes errores:\n  * Caracteres permitidos C, A, T y G.\n  * Son 6 cadenas de 6 caracteres separadas por un espacio\n*********************************************")

print("Matriz de ADN válida:")
for i in range(len(matriz_ADN)):
    print("\t".join(matriz_ADN[i]))
print("""Que desea hacer con la cadena armada: 
      Detectar Mutacion Escriba \"D\"
      Mutar Cadena de ADN Escriba \"M\"
      Sanar Cadena de ADN(aclaracion tiene que estar mutado) \"S\"
      """)

while True:
    opcion=input()
    opcion=opcion.upper()
    if opcion == "D":
        match detector.detectar_mutantes(matriz_ADN):
            case 1:print('Se ha detectado una mutación de tipo "Radiación"(Horizontal).')
            case 2:print('Se ha detectado una mutación de tipo "Radiación"(Vertical).')
            case 3:print('Se ha detectado una mutación de tipo "Virus".')
            case 0:print("No se ha detectadio ninguna mutación.")
        break
    elif opcion == "M":
        
        break
    elif opcion == "S":
        break
    else:
        print("Opción inválida")
