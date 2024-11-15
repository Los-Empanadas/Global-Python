#Importando clases
from Clases import *
import time
detector=Detector("Detector")

mutador=Radiacion("Mutador")

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
    opcion=input()
    opcion=opcion.upper()
    if opcion == "D":
        match detector.detectar_mutantes(matriz_ADN):
            case 1:print('Se ha detectado una mutación de tipo "Radiación"(Horizontal).')
            case 2:print('Se ha detectado una mutación de tipo "Radiación"(Vertical).')
            case 3:print('Se ha detectado una mutación de tipo "Virus".')
            case 0:print("No se ha detectadio ninguna mutación.")
        
    elif opcion == "M":
        pass
        
    elif opcion == "S":
        sanador = Sanador()
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
time.sleep(1.2)