import tkinter as tk
from tkinter import ttk
from tkinter.ttk import Label
from tkinter import * 
from math import *
from tkinter import Tk, Text
root = tk.Tk()
root.title('Convertisseur de monnaies')
root.geometry('600x400+50+50')
tk.Label(root, text='Bienvenue sur le convertisseur de monnaies').pack()

euro=1
dollar=1.08
#--Titre Convertir--#
label= Label(root, text='Valeur à convertir')
label.pack(ipadx=10, ipady=5)
#--Fin Titre Convertir--#

#--Valeur à convertir--#
v = float()
V1=ttk.Entry(root, textvariable=v)
V1.pack(padx=200, pady=2, fill='x')
V1.focus()
#--Fin Valeur à convertir--#

#--Conversion--#
def conversion_euros():
    Integral= V1.get()
    Val1=float(Integral)
    V2=Val1/dollar
    print(V2)
    return V2
    
def conversion_dollars():
    Integral= V1.get()
    Val1=float(Integral)
    V2=Val1*dollar
    print(V2)
    return V2
#--Fin de Conversion--#

#--Bouton1--#
def get_dollars():
    e_text=str(conversion_dollars())+" $ "
    res=Label(root, text=e_text, font= ('Century 15 bold')).pack(pady=20)
    return res
bouton=ttk.Button(root, text='Euros vers Dollars', command=get_dollars)
bouton.pack()
#--Fin Bouton1--#

#--Bouton2--#
def get_euros():
    e_text=str(conversion_euros())+" € "
    res=Label(root, text=e_text, font= ('Century 15 bold')).pack(pady=20)
    return res
bouton=ttk.Button(root, text='Dollars vers Euros', command=get_euros)
bouton.pack()
#--Fin Bouton2--#

#--Titre Convertie--#
label=Label(root, text='Valeur convertie')
label.pack(ipadx=10, ipady=5)
#--Fin Titre Convertie--#



#----------------------------------------------------------------#
#Impossible de trouver la solution pour la partie de l'historique#
#----------------------------------------------------------------#
#--Historique--#
#def open_text():
   #text_file=open("test.txt", "r")
   #content=text_file.read()
   #text.insert(END, content)
   #text_file.close()

#def save_text():
   #text_file=open("test.txt", "w")
   #text_file.write(text.get(1.0, END))
   #text_file.close()

#-texte box-#
#e_text=str(conversion_dollars())+" $ "
#e_text=str(conversion_euros())+" € "
#text=Label(root, text=e_text, font= ('Century 15 bold'))
#text.pack()

#-Ouvrir-#
#bouton=Button(root, text="Ouvrir", command=open_text)
#bouton.pack()

#-sauvegarde-#
#save=Button(root, text="Sauvegarde", command=save_text)
#save.pack()
#--Fin Historique--#


#---------------------------------------------------#
#Impossible de trouver la solution pour la partie du bouton reset#
#---------------------------------------------------#

#e_text=str(conversion_dollars())+" $ "
#e =Label(root, text=e_text, font= ('Century 15 bold')).pack(pady=20)

#--Bouton Reset--#
#def delete():
#    global e
#    e.after(1, e.destroy())

#bouton=ttk.Button(root, text='Reset', command=delete)
#bouton.pack()

root.mainloop()