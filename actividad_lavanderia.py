datos = open('/home/luis/Documents/UBA_Drive/UBA/C5/modelos_optimizacion/actividades/semana_1/primer_problema.txt', 'r')
archivo_final = open('/home/luis/Documents/UBA_Drive/UBA/C5/modelos_optimizacion/actividades/semana_1/primer_solucion.txt', 'w')

for linea_leida in datos:

    linea = linea_leida.split()

    # Leo el problema
    if 'p' == linea[0]:
        
        print(linea)


    


datos.close()
archivo_final.close()