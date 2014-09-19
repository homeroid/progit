def non (num):
    if int (num) % 2 == 0:
        return False
    return True
non (4)
print (not non)

def oddbit(num):
    x = 1
    y = int(num) & a
    if b == 1:
        return True
    return False

# 3 no lo pude hacer
def mayus (frase):
    txt = frase.split()
    for palabras in txt:
        framayu= txt.mayus()
    return framayu
print (mayus)

import random
def ruleta ():
    tiros = 0
    vive = True
    while tiros != 7 and vive == True :
        tiros += 1
        tiroya = random.randint(0,7)
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


#En este problema en particular me ayudaron porque no me sali y me pasaron el un link y me ayudaron
import smtplib
import socket
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def sendmail():
    dedir = "omegonza26@gmail.com"
    adir = "rontiveros@itesm.mx"
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "Tarea 5 ejercicio 6"
    texto = "Mensaje enviado desde " + os.environ['COMPUTERNAME']
    msg.attach(MIMEText(body, 'plain'))
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login("omegonza26@gmail.com", "escuela") 
    text = msg.as_string()
    server.sendmail(dedir, adir, texto)
sendmail()
print ("Enviado)

#A veces falla nose porque
import tkinter
def selectfile():
    tkinter.Tk().withdraw()
    return (tkinter.filedialog.askopenfilename())

print(eval(input("Escribe una operación")))

    
