#--------------- POKEDEX PROJECT ----------------#
#--------------- BY: TREVAR HUPF ----------------#
#--------------- PURELY FOR FUN -----------------#
#---------------- AND LEARNING ------------------#
#--------------- LEARNING IS FUN ----------------#


# IF I WANTED TO USE THE API INSTEAD OF LOCAL CSV
# import requests
# import json
# response = requests.get('https://pokeapi.co/api/v2/pokemon/' + mystring)
# pokemon = response.json()
# type = pokemon['types'][0]['type']['name']

#imports
from random import randint
from tkinter import *
import tkinter as tk
import csv
from PIL import ImageTk, Image
import random


pokemonlist = []
name = ""
with open("pokemon.csv", newline='') as csv_file:
        for index in csv.reader(csv_file):
            pokemonlist.append(index)

############################### INITIAL_FORM_CREATION #####################################
#path to folder that contains pokemon images
path = "C:\\Users\\TrevarHupf\\Documents\\Scripts\\Pokedex\\PokeImages\\"
form = tk.Tk() #create main form
form.title("Pokedex") #Title form
form.geometry("746x542") #Sets form size
background = PhotoImage(file = "PokedexImg.png") #sets background image
#Create canvas
canvas1 = Canvas(form,width=746, height=542) 
canvas1.pack(fill = "both", expand = True)
canvas1.create_image( 0, 0,image= background, anchor="nw") #Sets images to background image
canvas1.configure(bg='white') #background color
###########################################################################################

#function to set pokemon images to a more usable format using PIL
def set_image(picture_number):
    return (ImageTk.PhotoImage(Image.open(path + picture_number+".jpg")))


#Gets the current pokemon input and stores the entire row of pokemon data as list
def current_pokemon_list():
    input_string = inputtxt.get()
    cap_string = input_string.capitalize()
    for row in pokemonlist:
        if row[1] == cap_string:
            single_pokemon_list = row 
    return(single_pokemon_list)
########################################################

#Updates labels, accepts the list of desired pokemon
def update_labels(single_pokemon_list):
    canvas1.delete("type1")
    canvas1.delete("type2")
    canvas1.delete("name")
    global pokeimage
    name = single_pokemon_list[1]
    type1 = single_pokemon_list[2]
    type2 = single_pokemon_list[3]
    hp = single_pokemon_list[5]
    attack = single_pokemon_list[6]
    defense = single_pokemon_list[7] 
    spatk = single_pokemon_list[8]
    spdef = single_pokemon_list[9]
    speed = single_pokemon_list[10]
    legendary = single_pokemon_list[12]
    image = single_pokemon_list[0] 

    namelabel = tk.Label(form,bg='white',text=name)
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
    canvas1.create_window(145,165,window=namelabel, tags="name")
    canvas1.create_window(145,225,window=hplabel)
    canvas1.create_window(145,245,window=attacklabel)
    canvas1.create_window(145,265,window=defenselabel)
    canvas1.create_window(145,285,window=spatklabel)
    canvas1.create_window(145,305,window=spdeflabel)
    canvas1.create_window(255,185,window=speedlabel)
    canvas1.create_window(255,205,window=leglabel)

    pokeimage = set_image(image)
    #pokeimage = PhotoImage(file = pokeimage1)
    pokelabel = Label(form,image=pokeimage) #calls image function 
    canvas1.create_window(573,273,window=pokelabel)
########################################################

#Random button
def button_random():
    rand_int = random.randint(1,151)
    single_pokemon_list = pokemonlist[rand_int]
    update_labels(single_pokemon_list)
    string = single_pokemon_list[1]
    inputtxt.delete(0,END)
    inputtxt.insert(0,string)
########################################################

#Next button
def next_button():
    index = -1
    input_string = inputtxt.get()
    cap_string = input_string.capitalize()
    for row in pokemonlist:
        index+=1
        if row[1] == cap_string:
            index += 1 
            single_pokemon_list = pokemonlist[index]
            string = single_pokemon_list[1]
    update_labels(single_pokemon_list)
    inputtxt.delete(0,END)
    inputtxt.insert(0,string)
    index = -1
########################################################

#Function for evolve button click
def button_evolve():
    global original,evolve1, evolve2, evolve3, arrow #set global variables ~ required for multiple images in TKINTER - something about garbage collection
    arrow = ImageTk.PhotoImage(Image.open("arrow.jpg")) #Set arrow images
    string = inputtxt.get()  #Store input of Poke search
    mystring = string.capitalize() #capitalize first letter to match CSV
    with open ("pokemon.csv", "r", encoding='utf-8') as csv_file: #utf-8 to avoid strange symbols, reads the CSV
        reader = csv.reader(csv_file, delimiter=',') #Sets reader variable, dlimiter is comma
        for lines in reader: #loop through columns of CSV
            if lines[1] == mystring: #if column [1] (the second column that contains pokemon names) equals the string the user searches
                ##########Create Second FORM####################
                evolveform = Toplevel(form) 
                evolveform.geometry("1200x245")
                evolveform.configure(bg='white')
                evolveform.title("Evolution of " + string.capitalize()) #Set title and includes the pokemon that evolves 
                #################################################
                first_evolution = lines[0] #Set first evolution as the pokemon that was searched
                original = set_image(first_evolution) #Sets original variable to the searched pokemon's image
                if mystring == "Eevee": # if statement purely for eevee because of the three eveolutions
                    evolveform.geometry("1200x600")
                    a,b,c = lines[13].split(',') #splits the 14th column into 3 variable strings that correlate to the correct image
                    Label(evolveform,image=original).place(x='450',y='0') #GUI image placement, logic repeats
                    evolve1 = set_image(a) #sets first image to the image that correctly correlates - see CSV for logic, logic repeats
                    Label(evolveform,image=evolve1).place(x='0',y='300') 
                    evolve2 = set_image(b) 
                    Label(evolveform,image=evolve2).place(x='450',y='300') 
                    evolve3 = set_image(c)
                    Label(evolveform,image=evolve3).place(x='898',y='300') 
                    Label(evolveform,image=arrow).place(x='350',y='100')
                elif ',' in lines[13]: #searches for comma in csv, this identifies that pokemon evolves twice
                    a,b = lines[13].split(',')
                    Label(evolveform,image=original).place(x='3',y='0') 
                    evolve1 = set_image(a)
                    Label(evolveform,image=evolve1).place(x='450',y='0')
                    evolve2 = set_image(b)
                    Label(evolveform,image=evolve2).place(x='898',y='0') 
                    Label(evolveform,image=arrow).place(x='350',y='100') 
                    Label(evolveform,image=arrow).place(x='800',y='100') 
                elif lines[13] != "0": #if the evolution column does not equal zero, this assumes that pokemon only evolve once
                    evolveform.geometry("800x245")
                    Label(evolveform,image=original).place(x='3',y='0') 
                    evolve1 = set_image(lines[13])
                    Label(evolveform,image=evolve1).place(x='500',y='0') 
                    Label(evolveform,image=arrow).place(x='370',y='100') 
                else: #assumes that the pokemon does not evolve
                    evolveform.title(string + " is fully evolved")
                    evolveform.geometry("300x245")
                    Label(evolveform,image=original).place(x='0',y='0') 
                    
                                    
#Button press function 
def button_search():
    single_pokemon_list = current_pokemon_list()
    update_labels(single_pokemon_list)

######################################### Initial Form GUI #####################################################
inputtxt = tk.Entry(form)
pokemon_label = tk.Label(form,bg='white',text="Pokemon: ")
namelabel = tk.Label(form,bg='white',text=name)
type_label = tk.Label(form,bg='white',text="Type 1: ")
type2_label = tk.Label(form,bg='white',text="Type 2: ")
hp_label = tk.Label(form,bg='white',text="HP: ")
attack_label = tk.Label(form,bg='white',text="Attack: ")
defense_label = tk.Label(form,bg='white',text="Defense: ")
spatk_label = tk.Label(form,bg='white',text="Sp Attack: ")
spdef_label = tk.Label(form,bg='white',text="Sp Defense: ")
speed_label = tk.Label(form,bg='white',text="Speed: ")
leg_label = tk.Label(form,bg='white',text="Legendary: ")
button_pokesearch = tk.Button(form,text="Pokemon Search",bg='orange', command = button_search) #button calls search_button function
buttonevolve = tk.Button(form,text="Evolve",bg='orange', command = button_evolve) #button calls button_evolve function
buttonrandom = tk.Button(form,text="Random",bg='orange', command = button_random) #button calls search_button function
canvas1.create_window(90,165,window=pokemon_label)
canvas1.create_window(79,185,window=type_label)
canvas1.create_window(79,205,window=type2_label)
canvas1.create_window(72,225,window=hp_label)
canvas1.create_window(79,245,window=attack_label)
canvas1.create_window(82,265,window=defense_label)
canvas1.create_window(86,285,window=spatk_label)
canvas1.create_window(90,305,window=spdef_label)
canvas1.create_window(205,185,window=speed_label)
canvas1.create_window(215,205,window=leg_label)
canvas1.create_window(148, 430, window=inputtxt)
canvas1.create_window(145,165,window=namelabel, tags="name")
canvas1.create_window(150, 480, height=70,width=130, window=button_pokesearch)
canvas1.create_window(510, 490, height=55,width=130, window=buttonevolve)
canvas1.create_window(640, 490, height=55,width=130, window=buttonrandom)
###############################################################################################################


#initiate main form
form.mainloop()

