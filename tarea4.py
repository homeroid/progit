def cuad(num):
    x = float(num) ** 2
    print("El cuadrado de " + str(num) + "es " + str(x))
    return x
cuad ("60.5")

import datetime
def edad(date):
    ndia = datetime.datetime.strptime(date, "%d-%m-%Y")
    hoy = datetime.datetime.today()
    edadtotal = hoy - ndia
    edadfinal = (edadtotal.days/ 365, 0)
    print("Usted tiene " + str(edadfinal) + " años.")
    return edadfinal
edad("26-09-1995")

def esvier(date):
    fecha = datetime.datetime.strptime(date, "%d-%m-%Y")
    diasem = fecha.weekday()
    if diasem == 4:
        print(True)
        return True #no se porque agarra a viernes como 4#
    else:
        print(False)
        return False
esvier ("26-08-2014")

def futuro(date):
    fecha = datetime.datetime.strptime(date, "%d-%m-%Y") 
    fecha2 = datetime.date(fecha.year + 10, fecha.month, fecha.day)
    nuevaf = "{0:%d (%A) %B %Y}".format(fecha2)
    print(nuevaf)
futuro("29-08-2004")

def imc(peso, altura):
    imc2 = peso / (altura**2)
    print("Tu imc es " + str(round(imc2)))
    return imc2
imc(83,1.8)

def areacir(radio):
    PI = 3.1416
    area = PI * (radio**2)
    print("El area del circulo con radio " + str(radio) + " es " + str(area))
    return area
areacir(10)

def div2(num):
    divi = int(num) % 2
    if div2 == 0:
        print(True)
        return True
    else:
        print(False)
        return False # es tambien la primera función creo#
div2(24)

def div3(num):
    divis = int(num) % 3
    if div3 == 0:
        print(True)
        return True
    else:
        print(False)
        return False
div2(7)

def div23(num):
    divi2 = int(num) % 2
    divi3 = int(num) % 3
    if divi2 == 0:
        if divi3 ==0:
            print(True)
            return True
        else:
            print(False)
            return False
    else:
        print(False)      
div23(66)

def prom10(num1,num2,num3,num4,num5,num6,num7,num8,num9,num10):
    prome = (num1+num2+num3+num4+num5+num6+num7+num8+num9+num10)/10
    print(prome)
    return(prome)
prom10(12,6,5,16,78,45,33,22,10,59)
