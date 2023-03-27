# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 16:09:12 2023

@author: Aldo
"""

from tkinter import *
import speedtest 

SpeedtestChafa = Tk()
SpeedtestChafa.title("Speedtest barato")
SpeedtestChafa.geometry("740x480")
SpeedtestChafa.configure(background = "thistle4")

"""
print(round((VelociDescarga.download()) / 1000000))
"""
Titulo = Label(SpeedtestChafa,text = "SPeDTst",font = ("comic sans",65,"bold"), bg = "thistle4", fg = "thistle2")
Titulo.place(relx = 0.5,rely = 0.12, anchor = CENTER)

VeloDescarga = Label(SpeedtestChafa,text = "Velocidad de descarga",font = ("comic sans",15,"bold"), bg = "thistle3", fg = "thistle1")
VeloDescarga.place(relx = 0.25,rely = 0.3, anchor = CENTER)
Descarga = Label(SpeedtestChafa,font = ("comic sans",15,"bold"), bg = "thistle3", fg = "thistle1")
Descarga.place(relx = 0.25,rely = 0.38, anchor = CENTER)

VeloCarga = Label(SpeedtestChafa,text = "Velocidad de carga",font = ("comic sans",15,"bold"), bg = "thistle3", fg = "thistle1")
VeloCarga.place(relx = 0.75,rely = 0.3, anchor = CENTER)
Carga = Label(SpeedtestChafa,font = ("comic sans",15,"bold"), bg = "thistle3", fg = "thistle1")
Carga.place(relx = 0.75,rely = 0.38, anchor = CENTER)


def Correr ():
    VelociDescarga = speedtest.Speedtest()
    Calculadora = round((VelociDescarga.download()) / 1000000)
    Descarga['text'] = str(Calculadora) + "MBps"
    
    CalculadoraCarga = round((VelociDescarga.upload()) / 1000000)
    Carga['text'] = str(CalculadoraCarga) + "MBps"

print("Hooorah! BOTON!")
VeTuFuturo = Button(SpeedtestChafa,text = "Vas A Ganar En tu Juego?",font = ("comic sans",10,"bold"), bg = "thistle3", fg = "thistle1", command = Correr)
VeTuFuturo.place(relx = 0.5,rely = 0.7, anchor = CENTER)


SpeedtestChafa.mainloop()