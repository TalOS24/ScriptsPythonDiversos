#!/usr/bin/env python
# -*- coding: utf-8 -*-

archivo1 = "GO0315_201708DATOS5D_4.txt"
archivo2 = "GO0315_201709DATOS5D_4.txt"

archi1 = open(archivo1,"r")
cadenaArchivoUno = archi1.read()
l1 = cadenaArchivoUno.splitlines()
archi1.close()

archi2 = open(archivo2,"r")
cadenaArchivoDos = archi2.read()
l2 = cadenaArchivoDos.splitlines()
archi2.close()

c = 0
for lineaArchivoUno in l1:
    for lineaArchivoDos in l2:
        if lineaArchivoUno == lineaArchivoDos:
            c += 1
        else:
            print("en la linea :" + str(c) + " hay diferencias " )
            listaPalabra1 = list(lineaArchivoUno)
            listaPalabra2 = list(lineaArchivoDos)

            caracter = 0
            pares = list(zip(listaPalabra1,listaPalabra2))
            for elemento in pares:
                if elemento[0] != elemento[1]:
                    print("detectada diferencia en: " + str(pares.index(elemento)) + " los elementos son: " + str(elemento))
        break
    break












