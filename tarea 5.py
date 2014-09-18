def non (num):
    if int (num) % 2 == 0:
        return False
    return True
non (4)
print (not non)

# 2 nose le entedí

# 3 no lo pude hacer
def mayus (frase):
    txt = frase.split()
    for palabras in txt:
        framayu= txt.mayus()
    return framayu
print (mayus)

#nose que valor poner
import random
def ruleta ():
    tiros = 0
    vive = True
    while tiros != 8 and vive == True :
        tiros += 1
        tiroya = random.randint(0,8)
        if tiroya == 0 :
            print ("Estas muerto")
            vivo = False
    if vivo == True:
        print  ("te salvaste")

import math
def lado (base, angulo):
    otangulo = 90 - angulo
    ladop = base * (math.sin(math.radians(angulo)))
    otlado = ladop / (math.sin(math.radians(otangulo)))
    return otlado
lado(13,27)

import statistics
def stadev(poblacion):
    return statistics.stdev(poblacion)
print(stadev([1.5, 2.5, 2.5, 3.75, 3.25, 4.75]))

import os
def cpus ():
    if os.cpu_count() < 2:
        print ("Comprese una nueva compu esta chafa")
    else:
        print ( "Tu compu es chida")



        
    
