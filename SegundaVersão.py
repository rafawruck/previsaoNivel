# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 16:02:17 2025

@author: 215511
"""

horas = ["00:00", "01:00", "02:00", "03:00", "04:00", "05:00", "06:00", "07:00", "08:00", "09:00", "10:00", "11:00", "12:00", "13:00", "14:00", "15:00", "16:00", "17:00", "18:00", "19:00", "20:00", "21:00", "22:00", "23:00"]
Cabeçalho = ["Data","Hora","Blumenau","Apiuna","Timbó"]
Dados = {"Data": [],
         "Hora":[],
         "Blumenau":[],
         "Apiuna":[],
         "Timbó":[]
         }

Evento = False


def registraLeitura():
    global Dados
    if len(Dados["Data"]) == 0:
        print ("Não existe dados sobre o evento.")
        start = str(input("Você quer iniciar um evento [S/sim - N/não]: ")).upper()
        if start == "S":
            diaI = int(input("Insira o dia de inicio: "))
            mesI = int(input("Insira o mês de inicio: "))
            dataI = ("{}/{}".format(diaI,mesI))
            print ("Data de inicio do evento será {} e horário as 00:00 horas".format(dataI))
            
    while True:
        posição = len(Dados["Data"])
        Dados["Data"].append(dataI)
        Dados["Hora"].append(horas[posição])
        Dados["Blumenau"].append(float(input("Insira a leitura de Blumenau para o dia {} as {}: ".format(Dados["Data"][posição], Dados["Hora"][posição]))))
        Dados["Apiuna"].append(float(input("Insira a leitura de Apiuna para o dia {} as {}: ".format(Dados["Data"][posição], Dados["Hora"][posição]))))
        Dados["Timbó"].append(float(input("Insira a leitura de Timbó para o dia {} as {}: ".format(Dados["Data"][posição], Dados["Hora"][posição]))))
        
        if Dados["Hora"][posição]=="23:00":
            diaI+=1
            
        
        end = str(input("Quer inserir mais dados [S/sim - N/não]: ")).upper()
        if end == "N":
            break

def imprimirDados():
    global Dados
    print ("Data - Hora - Blumenau - Apiuna - Timbó")
    for i in range(len(Dados["Data"])):
        print ("{} - {} - {} - {} - {}".format(Dados["Data"][i], Dados["Hora"][i], Dados["Blumenau"][i], Dados["Apiuna"][i], Dados["Timbó"][i]))