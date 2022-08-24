datos = open('primer_problema.txt', 'r')
archivo_final = open('primer_solucion.txt', 'w')

prendas = []

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


prendas = sorted(prendas,key=lambda x: x[2], reverse=True)
print(prendas)
    
# Busco las compatibles de las prendas mas sucias
todas_prendas = [ i for i in range(1,len(prendas)) ] # Creo las prendas


num = list(filter(lambda x: x not in num_to_remove, num))
    
# Escribo en el archivo final
#archivo_final.write(" ".join(map(str,linea)))
    
datos.close()
archivo_final.close()