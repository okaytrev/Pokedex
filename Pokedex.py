# IF I WANTED TO USE THE API INSTEAD OF LOCAL CSV
# import requests
# import json
# response = requests.get('https://pokeapi.co/api/v2/pokemon/' + mystring)
# pokemon = response.json()
# type = pokemon['types'][0]['type']['name']

#imports
from tkinter import *
import tkinter as tk
import csv
from PIL import ImageTk, Image


path = "C:\\Users\\TrevarHupf\\Documents\\Scripts\\Pokedex\\PokeImages\\"
#Create form
form = tk.Tk()
form.title("Pokedex")
#Set size of form
form.geometry("746x542")
#Sets background of form
background = PhotoImage(file = "PokedexImg.png")
#Create canvas
canvas1 = Canvas(form,width=746, height=542)
canvas1.pack(fill = "both", expand = True)
canvas1.create_image( 0, 0,image= background, anchor="nw")
canvas1.configure(bg='white')

def button_evolve():
    global original,evolve1, evolve2, arrow1, arrow2
    evolveform = Toplevel(form)
    evolveform.geometry("800x650")
    evolveform.configure(bg='white')
    string = inputtxt.get()
    mystring = string.capitalize()
    evolveform.title("Evolution of " + string)
    with open ("pokemon.csv", "r", encoding='utf-8') as csv_file: #utf-8 to avoid strange symbols, reads the CSV
        reader = csv.reader(csv_file, delimiter=',') 
        for lines in reader:
            if lines[1] == mystring:
                first_evolution = lines[0]
                a,b = lines[13].split(',')
                original = ImageTk.PhotoImage(Image.open(path + first_evolution+".jpg"))
                Label(evolveform,image=original).place(x='250',y='0')
                evolve1 = ImageTk.PhotoImage(Image.open(path + a +".jpg"))
                Label(evolveform,image=evolve1).place(x='500',y='400')
                evolve2 = ImageTk.PhotoImage(Image.open(path + b +".jpg"))
                Label(evolveform,image=evolve2).place(x='0',y='400')
                


#Button press function 
def button_search():
    global pokeimage
    canvas1.delete("type1")
    canvas1.delete("type2")
    string = inputtxt.get()
    mystring = string.capitalize()
    with open ("pokemon.csv", "r", encoding='utf-8') as csv_file: #utf-8 to avoid strange symbols, reads the CSV
        reader = csv.reader(csv_file, delimiter=',') 
        for lines in reader:
            if lines[1] == mystring:
                type1 = lines[2]
                type2 = lines[3] 
                hp = lines[5]
                attack = lines[6]
                defense = lines[7]
                spatk = lines[8]
                spdef = lines[9]
                speed = lines[10]
                legendary = lines[12]
                image = lines[0]
        pokeimage = ImageTk.PhotoImage(Image.open(path + image +".jpg"))
        #pokeimage = PhotoImage(file = pokeimage1)
        pokelabel = Label(form,image=pokeimage)
        canvas1.create_window(573,273,window=pokelabel)
 
    #Edit form
    typelabel = tk.Label(form,bg='white',text=type1)
    typelabel2 = tk.Label(form,bg='white',text=type2)
    hplabel = tk.Label(form,bg='white',text=hp)
    attacklabel = tk.Label(form,bg='white',text=attack)
    defenselabel = tk.Label(form,bg='white',text=defense)
    spatklabel = tk.Label(form,bg='white',text=spatk)
    spdeflabel = tk.Label(form,bg='white',text=spdef)
    speedlabel = tk.Label(form,bg='white',text=speed)
    leglabel = tk.Label(form,bg='white',text=legendary)

    canvas1.create_window(145,185,window=typelabel,tags="type1")
    canvas1.create_window(145,205,window=typelabel2, tags="type2")
    canvas1.create_window(145,225,window=hplabel)
    canvas1.create_window(145,245,window=attacklabel)
    canvas1.create_window(145,265,window=defenselabel)
    canvas1.create_window(145,285,window=spatklabel)
    canvas1.create_window(145,305,window=spdeflabel)
    canvas1.create_window(255,185,window=speedlabel)
    canvas1.create_window(255,205,window=leglabel)


# TextBox Creation
inputtxt = tk.Entry(form)
pokelabel = tk.Label(form,bg='white',text="Pokemon: ")
type_label = tk.Label(form,bg='white',text="Type 1: ")
type2_label = tk.Label(form,bg='white',text="Type 2: ")
hp_label = tk.Label(form,bg='white',text="HP: ")
attack_label = tk.Label(form,bg='white',text="Attack: ")
defense_label = tk.Label(form,bg='white',text="Defense: ")
spatk_label = tk.Label(form,bg='white',text="Sp Attack: ")
spdef_label = tk.Label(form,bg='white',text="Sp Defense: ")
speed_label = tk.Label(form,bg='white',text="Speed: ")
leg_label = tk.Label(form,bg='white',text="Legendary: ")
button_pokesearch = tk.Button(form,text="Pokemon Search",bg='orange', command = button_search)
button_evolve = tk.Button(form,text="Evolve",bg='orange', command = button_evolve)
canvas1.create_window(90,165,window=pokelabel)
canvas1.create_window(79,185,window=type_label)
canvas1.create_window(79,205,window=type2_label)
canvas1.create_window(72,225,window=hp_label)
canvas1.create_window(79,245,window=attack_label)
canvas1.create_window(82,265,window=defense_label)
canvas1.create_window(86,285,window=spatk_label)
canvas1.create_window(90,305,window=spdef_label)
canvas1.create_window(205,185,window=speed_label)
canvas1.create_window(215,205,window=leg_label)
canvas1.create_window(195, 165, window=inputtxt)
canvas1.create_window(150, 480, height=70,width=130, window=button_pokesearch)
canvas1.create_window(510, 490, height=55,width=130, window=button_evolve)

form.mainloop()

