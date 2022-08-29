datos = open('primer_problema.txt', 'r')
archivo_final = open('primer_solucion.txt', 'w')

prendas = []

# Leo los datos
for linea_leida in datos:

    linea = linea_leida.split()

    # Leo el problema
    if 'p' == linea[0]:
        prendas = [ [i,[],None] for i in range(1,int(linea[2])+1)] # Creo las prendas
    
    # Agrego las prendas incompatibles
    elif 'e' == linea[0]:
        n_prenda = int(linea[1])
        prendas[n_prenda-1][1].append(int(linea[2]))
    
    # Agrego el peso de cada prenda
    elif 'n'  == linea[0]:
        n_prenda = int(linea[1])
        prendas[n_prenda-1][2] = int(linea[2])


# Ordeno segun el peso de cada prenda
prendas = sorted(prendas,key=lambda x: x[2], reverse=True)
    

# Busco las compatibles de las prendas mas sucias
todas_prendas = set([ i for i in range(1,len(prendas)+1) ]) # Creo las prendas


prendas_incompatibles = {}

for i in prendas:
    prendas_incompatibles[i[0]]=set(i[1])



for i in [ i[0] for i in prendas ]:
    num = i
    compatibles = todas_prendas-prendas_incompatibles[num]
    
    compatibles_final = []
    
    for i in compatibles:

        compatibles_final.append(i)

        for j in compatibles_final.copy():
            if (i in prendas_incompatibles[j]):
                compatibles_final.remove(i)
                break
   

    todas_prendas = todas_prendas - set(compatibles_final)

    # Escribo las prendas finales
    for m in compatibles_final:
        escribir=[m,prendas[i-1][2]]
        archivo_final.write(" ".join(map(str,escribir)))
        archivo_final.write(" ".join(map(str,"\n")))
    
datos.close()
archivo_final.close()