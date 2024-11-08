
print("----------------------------------\n-Bienvenido al laboratorio de ADN-\n----------------------------------\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("Nos encantaria saber con que cadena de ADN te podemos ayudar, inteoducir dicha cadena como aparese en el siguiente ejemplo:\n *GTACGT CTGATA AGGCAG GCATCG TGAGCG GCTACT*\nCada cadena debe estar compuesta por 6 bases nitrogenadas y separadas por un espacio en blanco al completar las 6.\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

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
    opcion=opcion.upper
    if opcion == "D":
        break
    elif opcion == "M":
        break
    elif opcion == "S":
        break
    else:
        print("Opción inválida")
