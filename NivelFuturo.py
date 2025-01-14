# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 16:15:51 2025

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

def evento():
    global Evento
    global Dados
    criarEvento = str(input("Você quer criar um evento [S/sim - N/não]: ")).upper()
    if (criarEvento=="S"):
        if Evento==True:
            print ("Já existe um evento aberto, finalize para poder criar outro.")
            print ("O evento em questão tem data de inicio em {}".format(Dados["Data"][0]))
        else:
            dataInicial = int(input("Insira o dia de inicio do evento: "))
            mesInicial = int(input("Insira o Mês de inicio do evento: "))
            dataInicial = "{}/{}".format(dataInicial,mesInicial)
            print ("A data inicial do evento será {} as 00:00 horas".format(dataInicial))
            for i in range(0,24):
                Dados["Data"].append(dataInicial)
                Dados["Hora"].append(horas[i])
            Evento = True

def imprimirDados():
    global Dados
    print ("Data - Hora - Blumenau - Apiuna - Timbó")
    for i in range(len(Dados["Blumenau"])):
        print ("{} - {} - {} - {} - {}".format(Dados["Data"][i], Dados["Hora"][i], Dados["Blumenau"][i], Dados["Apiuna"][i], Dados["Timbó"][i]))


def dadosNivel():
    global Dados
    inseriDados = str(input("Inserir dados [S/sim - N/não]: ")).upper()
    if inseriDados == "S":
        posição = len(Dados["Blumenau"])
        
        