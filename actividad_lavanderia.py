datos = open('segundo_problema.txt', 'r')
archivo_final = open('segunda_solucion.txt', 'w')

prendas = []
lavados = 1

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


# Ordeno segun el tiempo de lavado de cada prenda
prendas = sorted(prendas,key=lambda x: x[2], reverse=True)  

# Creo las prendas
todas_prendas = set([ i for i in range(1,len(prendas)+1) ]) 


# Creo un diccionario para las prendas incompatibles
prendas_incompatibles = {}

for i in prendas:
    prendas_incompatibles[i[0]]=set(i[1])


tiempo_prendas_incompatibles = {}

for i in prendas:
    tiempo_prendas_incompatibles[i[0]]=i[2]



for i in [ i[0] for i in prendas ]:

    if(i not in todas_prendas):
        continue

    # Hago la diferencia de conjuntos A-B para obtener aquellos elementos del total 
    # de prendas a lavar que son compatibles para el numero i 
    compatibles = todas_prendas - prendas_incompatibles[i]


    # Ordeno los compatibles en orden decreciente del tiempo que tardan 
    # en lavarse para ir agregando siempre las prendas que duran mas tiempo
    compatibles = sorted(compatibles, key=lambda x: (tiempo_prendas_incompatibles[x] ), reverse=True)

    compatibles_final = []
    
    for j in compatibles:

        compatibles_final.append(j)

        # Si la prenda es incompatible con alguna de las prendas en el lavado, la saco
        for k in compatibles_final.copy():
            if (k in prendas_incompatibles[j] or j in prendas_incompatibles[k]):
                compatibles_final.remove(j)
                break
   
    # Escribo las prendas finales en el archivo final
    for m in compatibles_final:
        escribir=[m,lavados]
        archivo_final.write(" ".join(map(str,escribir)))
        archivo_final.write(" ".join(map(str,"\n")))

    todas_prendas = todas_prendas - set(compatibles_final)
    lavados = lavados+1
        
    
datos.close()
archivo_final.close()