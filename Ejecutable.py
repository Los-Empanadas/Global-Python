#Importando clases
import time
from Clases import *

detector=Detector("Detector",3)

sanador = Sanador("Sanador",["A","T","G","C"])



### Interfaz Laboratorio ###


print("----------------------------------\n-Bienvenido al laboratorio de ADN-\n----------------------------------\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("Nos encantaria saber con que cadena de ADN te podemos ayudar, introducir dicha cadena como aparece en el siguiente ejemplo:\n *GTACGT CTGATA AGGCAG GCATCG TGAGCG GCTACT*\nCada cadena debe estar compuesta por 6 bases nitrogenadas y separadas por un espacio en blanco al completar las 6.\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

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
      Sanar Cadena de ADN(Debe estar mutado) \"S\"
      Salir \"Q\"
      """)

while True:
    opcion=input().upper()
    if opcion == "D":
        match detector.detectar_mutantes(matriz_ADN):
            case 1:print('Se ha detectado una mutación de tipo "Radiación"(Horizontal).')
            case 2:print('Se ha detectado una mutación de tipo "Radiación"(Vertical).')
            case 3:print('Se ha detectado una mutación de tipo "Virus"(Diagonal).')
            case 0:print("No se ha detectadio ninguna mutación.")
        
    elif opcion == "M":
        # Solicita al usuario si quiere una mutacion tipo Virus o Radiación
        print("""Que tipo de mutación desea ingresar: 
            Virus: \"V\"
            Radiación: \"R\"
            """)
        tipo_mutacion=input().upper()
        if tipo_mutacion == "V":
            # Elige la opción Virus
            
            # Solicitar detalles para realizar una mutación diagonal con Virus
            fila = int(input("Ingrese la fila de inicio para la mutación diagonal (0-2): "))
            col = int(input("Ingrese la columna de inicio para la mutación diagonal (0-2): "))
            base_nitrogenada=""
            while(base_nitrogenada not in ["A", "T", "G", "C"]):
                base_nitrogenada = input("Ingrese la base nitrogenada que se repetirá ('A', 'T', 'G', 'C'): ").upper()
                # Verificar la base nitrogenada
                if base_nitrogenada not in ["A", "T", "G", "C"]:
                    print("Error: Base nitrogenada no válida. Debe ser 'A', 'T', 'G' o 'C'.")

            # Crear un objeto de la clase Virus
            virus = Virus("Virus",base_nitrogenada,"diagonal")
            # Mutar la matriz de ADN con la clase Virus
            matriz_ADN = virus.crear_mutante(matriz_ADN, (fila, col))
            # Mostrar la matriz mutada
            print("Matriz de ADN después de la mutación diagonal con Virus:")
            for fila in matriz_ADN:
                print("\t".join(fila))
                
        elif tipo_mutacion=="R":
            orien=""
            # Elige la opción Radiación
            while(orien not in ["H","V"]):
                orien= input("""Ingrese la orientación de la mutación: 
                Vertical: \"V\"
                Horizontal: \"H\"
                """).upper()
                if(orien not in ["H","V"]):
                    print("Error: Orientación no válida.")
            if orien=="H":
                fila = int(input("Ingrese la fila de inicio para la mutación horizontal (0-5): "))
                col = int(input("Ingrese la columna de inicio para la mutación diagonal (0-2): "))
            elif orien=="V":
                fila = int(input("Ingrese la fila de inicio para la mutación horizontal (0-2): "))
                col = int(input("Ingrese la columna de inicio para la mutación diagonal (0-5): "))
            base_nitrogenada=""
            
            while(base_nitrogenada not in ["A", "T", "G", "C"]):
                base_nitrogenada = input("Ingrese la base nitrogenada que se repetirá ('A', 'T', 'G', 'C'): ").upper()
                # Verificar la base nitrogenada
                if base_nitrogenada not in ["A", "T", "G", "C"]:
                    print("Error: Base nitrogenada no válida. Debe ser 'A', 'T', 'G' o 'C'.")
            # Crear un objeto de la clase radiacion
            radiacion=Radiacion("Radiacion",base_nitrogenada)
           # Mutar la matriz de ADN con la clase Radiación
            matriz_ADN = radiacion.crear_mutante(matriz_ADN, (fila, col),orien)
           # Mostrar la matriz mutada
            print("Matriz de ADN:")
            for fila in matriz_ADN:
                print("\t".join(fila))
            
    elif opcion == "S":
        
        matriz_ADN = sanador.sanar_mutantes(matriz_ADN,detector)
        print("Nueva Matriz de ADN:")
        for i in range(len(matriz_ADN)):
            print("\t".join(matriz_ADN[i]))
    elif opcion == "Q":
        break
        
    else:
        print("Opción inválida")
        
    print("""Que desea hacer con ésta cadena: 
      Detectar Mutacion Escriba \"D\"
      Mutar Cadena de ADN Escriba \"M\"
      Sanar Cadena de ADN(Debe estar mutado) \"S\"
      Salir \"Q\"
      """)
print("Gracias por usar Laboratorio de ADN :)")
time.sleep(1.3)