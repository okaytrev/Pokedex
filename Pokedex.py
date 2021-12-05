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
import webbrowser
import os

#variable creation
path = os.path.dirname(os.path.abspath(__file__)) #path = the current working directory of python script
pokemonlist = []
name = ""

#opens csv containing all data, saves in pokemonlist list
with open(path +"\\pokemon.csv", newline='') as csv_file:
        for index in csv.reader(csv_file):
            pokemonlist.append(index)

############################### INITIAL_FORM_CREATION #####################################
#path to folder that contains pokemon images
form = tk.Tk() #create main form
form.title("Pokedex") #Title form
form.geometry("746x542") #Sets form size
background = PhotoImage(file = path + "\\PokedexImg.png") #sets background image
#Create canvas
canvas1 = Canvas(form,width=746, height=542) 
canvas1.pack(fill = "both", expand = True)
canvas1.create_image( 0, 0,image= background, anchor="nw") #Sets images to background image
canvas1.configure(bg='white') #background color
###########################################################################################

#functions to set pokemon images to a more usable format using PIL
def set_image(picture_number):
    return (ImageTk.PhotoImage(Image.open(path +"\\pokeimages\\" + picture_number+".jpg")))

def set_sprite(sprite_number):
    return (ImageTk.PhotoImage(Image.open(path + "\\pokesprites\\" + sprite_number+".png")))

#Gets the current pokemon input and stores the entire row of pokemon data as list
def current_pokemon_list():
    input_string = inputtxt.get()
    cap_string = input_string.title()
    for row in pokemonlist:
        if row[1] == cap_string:
            single_pokemon_list = row 
    return(single_pokemon_list)
########################################################

#update input box
def update_inputbox(string):
    inputtxt.delete(0,END) 
    inputtxt.insert(0,string)

#Updates labels, accepts the list of desired pokemon
def update_labels(single_pokemon_list):
    canvas1.delete("growth","rank", "type1", "type2","name","num")
    global pokeimage,spriteimage
    name = single_pokemon_list[1]
    num = single_pokemon_list[0]
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
    total = single_pokemon_list[4]
    growth = single_pokemon_list[32]
    rank = single_pokemon_list[35]

    namelabel = tk.Label(form,bg='white',text=name)
    numlabel = tk.Label(form,bg='white',text=num)
    typelabel = tk.Label(form,bg='white',text=type1)
    typelabel2 = tk.Label(form,bg='white',text=type2)
    hplabel = tk.Label(form,bg='white',text=hp)
    attacklabel = tk.Label(form,bg='white',text=attack)
    defenselabel = tk.Label(form,bg='white',text=defense)
    spatklabel = tk.Label(form,bg='white',text=spatk)
    spdeflabel = tk.Label(form,bg='white',text=spdef)
    speedlabel = tk.Label(form,bg='white',text=speed)
    totallabel = tk.Label(form,bg='white',text=total)
    growthlabel = tk.Label(form,bg='white',text=growth)
    ranklabel = tk.Label(form,bg='white',text=rank)
    leglabel = tk.Label(form,bg='white',text=legendary)

    canvas1.create_window(225,167,window=typelabel,tags="type1")
    canvas1.create_window(225,187,window=typelabel2, tags="type2")
    canvas1.create_window(240,150,window=namelabel, tags="name")
    canvas1.create_window(297,150,window=numlabel, tags='num')
    canvas1.create_window(145,167,window=hplabel)
    canvas1.create_window(145,187,window=attacklabel)
    canvas1.create_window(145,227,window=defenselabel)
    canvas1.create_window(145,207,window=spatklabel)
    canvas1.create_window(145,247,window=spdeflabel)
    canvas1.create_window(145,267,window=speedlabel)
    canvas1.create_window(145,287,window=totallabel)
    canvas1.create_window(265,227,window=growthlabel, tags='growth')
    canvas1.create_window(145,307,window=ranklabel, tags="rank")
    canvas1.create_window(235,207,window=leglabel)

    pokeimage = set_image(image) #image function 
    spriteimage = set_sprite(image) #image function
    pokelabel = Label(form,image=pokeimage)  
    canvas1.create_window(573,273,window=pokelabel)
    spritelabel = Label(form,image=spriteimage) 
    canvas1.create_window(235,285,window=spritelabel)
########################################################

#Random button
def button_random():
    rand_int = random.randint(1,151) #gets random number
    single_pokemon_list = pokemonlist[rand_int] #gets all the data of one row randomly and stores in list
    update_labels(single_pokemon_list) #update labels fucntion with that random list
    #updates input box with the current random string
    string = single_pokemon_list[1] 
    #update inputbox function
    update_inputbox(string)
########################################################

#Next button
def button_next():
    index = -1 #ignores first row
    input_string = inputtxt.get() #saves inputbox as str
    cap_string = input_string.title() #capitalize first letter in string
    #Logic to set last entry to first entry, so user can infinitely click next
    if cap_string == "Mew":
            cap_string = "Name"
    #loops through list and increases the index by 1, updates the inputbox
    for row in pokemonlist:
        index+=1
        if row[1] == cap_string:
            index += 1 
            single_pokemon_list = pokemonlist[index]
            string = single_pokemon_list[1]
    #updates labels
    update_labels(single_pokemon_list)
    update_inputbox(string)
    index = -1
########################################################

#Back button
def button_back():
    index = -1 #ignores first row
    input_string = inputtxt.get()
    cap_string = input_string.title()
    if cap_string == "Bulbasaur":
            cap_string = "Name"
    for row in pokemonlist:
        index+=1
        if row[1] == cap_string:
            index -= 1 
            single_pokemon_list = pokemonlist[index]
            string = single_pokemon_list[1]
    update_labels(single_pokemon_list)
    update_inputbox(string)
    index = -1
########################################################

#Plus twenty button
def button_plustwenty():
    index = -1
    input_string = inputtxt.get()
    cap_string = input_string.title()
    if cap_string == "Mew":
            cap_string = "Name"
    for row in pokemonlist:
        index+=1
        if row[1] == cap_string:
            if index <= 130:
                index += 20 
                single_pokemon_list = pokemonlist[index]
                string = single_pokemon_list[1]
            if index > 130:
                index = random.randint(-1,5)
                index += 20
                single_pokemon_list = pokemonlist[index]
                string = single_pokemon_list[1]
    update_labels(single_pokemon_list)
    update_inputbox(string)
    index = -1
########################################################

#Minus twenty button
def button_minustwenty():
    index = -1
    input_string = inputtxt.get()
    cap_string = input_string.title()
    if cap_string == "Bulbasaur":
        cap_string = "Name"
    for row in pokemonlist:
        index+=1
        if row[1] == cap_string:
            index -= 20 
            single_pokemon_list = pokemonlist[index]
            string = single_pokemon_list[1]
    update_labels(single_pokemon_list)
    update_inputbox(string)
    index = -1
########################################################

#Catch em button
def button_catch():
    #global variable for tkinter images
    global pokeball,greatball,ultraball,masterball 
    single_pokemon_list = current_pokemon_list() #sets curet input box to list
    catchrate = single_pokemon_list[33] #gets the catchrate from column 34
    name =single_pokemon_list[1] #sets name of pokemon
    catchrate = int(catchrate) #converst catchrate to int
    #initiate pokeball images
    pokeball = ImageTk.PhotoImage(Image.open("balls\\pokeball.png"))
    greatball = ImageTk.PhotoImage(Image.open("balls\\greatball.png"))
    ultraball = ImageTk.PhotoImage(Image.open("balls\\ultraball.png"))
    masterball = ImageTk.PhotoImage(Image.open("balls\\masterball.png"))
    #creates new form
    catchform = Toplevel(form) 
    catchform.geometry("300x350")
    catchform.configure(bg='white')
    catchform.title("Catch em all!")
    #based on catch rate populates the new form, higher the catch rate means the easier it is to catch
    if catchrate <= 255 and catchrate >= 190:
        outputstr = name +" has a catch rate of " + str(catchrate) +  ".\n The best way to catch it is with a Pokeball. \n Do some damage and huck some pokeballs at it!"
        Label(catchform,text=outputstr,background='white').place(x='15',y='0')
        Label(catchform,image=pokeball,background='white').place(x='0',y='60')
    elif catchrate < 190 and catchrate >= 45:
        outputstr = name +" has a catch rate of " + str(catchrate) +  ".\n Catch it is with a Greatball or Pokeball. \n You will want to weaken it first. "
        Label(catchform,text=outputstr,background='white').place(x='40',y='0')
        Label(catchform,image=greatball,background='white').place(x='0',y='60')
    elif catchrate < 45 and catchrate >= 25:
        outputstr = name +" has a catch rate of " + str(catchrate) +  ".\n Better bring an Ultraball or Greatball. \n This one is tough. You might want to put it to sleep!"
        Label(catchform,text=outputstr,background='white').place(x='5',y='0')
        Label(catchform,image=ultraball,background='white').place(x='0',y='60')
    else:
        outputstr = name +" has a catch rate of " + str(catchrate) +  ".\n Masterball time! \n Goodluck with the Ultraball..."
        Label(catchform,text=outputstr,background='white').place(x='70',y='0')
        Label(catchform,image=masterball,background='white').place(x='0',y='60')
########################################################

#Function for evolve button click
def button_evolve():
    global original,evolve1, evolve2, evolve3, arrow #set global variables ~ required for multiple images in TKINTER - something about garbage collection
    arrow = ImageTk.PhotoImage(Image.open("arrow.jpg")) #Set arrow images
    string = inputtxt.get()  #Store input of Poke search
    mystring = string.title() #capitalize first letter to match CSV
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
 ###########################################################################

#Button press function 
def button_search():
    single_pokemon_list = current_pokemon_list()
    update_labels(single_pokemon_list)

#opens url based on the current pokemon in inputbox
def button_bulpedia():
    name = inputtxt.get()
    url = "https://bulbapedia.bulbagarden.net/wiki/" + name + "_(Pokémon)"
    webbrowser.open_new(url)

def button_off():
    global blackscreen1,blackscreen2,blackscreen3
    blackscreen1 = tk.Label(form,bg='black')
    canvas1.create_window(573,273,width=296,height=240,window=blackscreen1)
    blackscreen2 = tk.Label(form,bg='black')
    canvas1.create_window(105,238,width=100,height=175,window=blackscreen2)
    blackscreen3 = tk.Label(form,bg='black')
    canvas1.create_window(235,247,width=165,height=225,window=blackscreen3)
    disable_buttons()

def button_on():
    enable_buttons()
    blackscreen1.destroy()
    blackscreen2.destroy()
    blackscreen3.destroy()

def disable_buttons():
    buttonpoweroff["state"] = DISABLED
    buttonback["state"] = DISABLED
    buttonback2["state"] = DISABLED
    buttonrandom["state"] = DISABLED
    buttonrandom2["state"] = DISABLED
    buttonnext["state"] = DISABLED
    buttonnext2["state"] = DISABLED
    buttonminustwenty["state"] = DISABLED
    buttonplustwenty["state"] = DISABLED
    buttonevolve["state"] = DISABLED
    buttonevolve2["state"] = DISABLED
    buttonbulpedia["state"]=DISABLED
    buttoncatch["state"]=DISABLED
    buttonpokesearch["state"]=DISABLED
    randomsix["state"]=DISABLED

def enable_buttons():
    buttonpoweroff["state"] = NORMAL
    buttonback["state"] = NORMAL
    buttonback2["state"] = NORMAL
    buttonrandom["state"] = NORMAL
    buttonrandom2["state"] = NORMAL
    buttonnext["state"] = NORMAL
    buttonnext2["state"] = NORMAL
    buttonminustwenty["state"] = NORMAL
    buttonplustwenty["state"] = NORMAL
    buttonevolve["state"] = NORMAL
    buttonevolve2["state"] = NORMAL
    buttonbulpedia["state"]=NORMAL
    buttoncatch["state"]=NORMAL
    buttonpokesearch["state"]=NORMAL
    randomsix["state"]=NORMAL
    
def random_six():
    global pokeimage1,pokeimage2,pokeimage3,pokeimage4,pokeimage5,pokeimage6
    count = 1
    sixform = Toplevel(form) 
    sixform.geometry("900x480")
    sixform.configure(bg='white')
    sixform.title("Random Team")
    random_list = []
    num_list = []
    for i in range(6):
        rand_int = random.randint(1,151)
        random_list.append(pokemonlist[rand_int])
        i+=1
    for item in random_list:
        num_list.append(item[0])

    print(num_list)
    pokeimage1 = set_image(num_list[0])
    pokeimage2 = set_image(num_list[1])
    pokeimage3 = set_image(num_list[2])
    pokeimage4 = set_image(num_list[3])
    pokeimage5 = set_image(num_list[4])
    pokeimage6 = set_image(num_list[5])
    Label(sixform,image=pokeimage1).place(x='0',y='0') 
    Label(sixform,image=pokeimage2).place(x='300',y='0')
    Label(sixform,image=pokeimage3).place(x='600',y='0')
    Label(sixform,image=pokeimage4).place(x='0',y='240')
    Label(sixform,image=pokeimage5).place(x='300',y='240')
    Label(sixform,image=pokeimage6).place(x='600',y='240')
    
    

######################################### Initial Form GUI #####################################################
inputtxt = tk.Entry(form)
pokemon_label = tk.Label(form,bg='white',text="Name: ")
search_label = tk.Label(form,bg='white',text="Search:")
num_label = tk.Label(form,bg='white',text="#")
namelabel = tk.Label(form,bg='white',text=name)
type_label = tk.Label(form,bg='white',text="Type 1: ")
type2_label = tk.Label(form,bg='white',text="Type 2: ")
hp_label = tk.Label(form,bg='white',text="HP: ")
attack_label = tk.Label(form,bg='white',text="Attack: ")
defense_label = tk.Label(form,bg='white',text="Defense: ")
spatk_label = tk.Label(form,bg='white',text="Sp Attack: ")
spdef_label = tk.Label(form,bg='white',text="Sp Defense: ")
speed_label = tk.Label(form,bg='white',text="Speed: ")
total_label = tk.Label(form,bg='white',text="Total stats: ")
growth_label = tk.Label(form,bg='white',text="Growth rate: ")
power_label = tk.Label(form,bg='white',text="Power rank: ")
leg_label = tk.Label(form,bg='white',text="Legendary: ")
buttonpoweroff = tk.Button(form,text="Off",bg='sienna1', command = button_off) #button calls search_button function
buttonpoweron = tk.Button(form,text="On", bg='green yellow', command = button_on) #button calls search_button function
buttonpokesearch = tk.Button(form,text="Find",bg='white', command = button_search) #button calls search_button function
buttoncatch = tk.Button(form,text="Catch it!",bg='yellow', command = button_catch) #button calls search_button function
buttonbulpedia = tk.Button(form,text="Web Search\nBulpedia",bg='lime green', command = button_bulpedia) #button calls search_button function
buttonevolve = tk.Button(form,text="Evolve",bg='skyblue1', command = button_evolve) #button calls button_evolve function
buttonrandom = tk.Button(form,text="Random",bg='maroon1', command = button_random) #button calls search_button function
buttonevolve2 = tk.Button(form,text="Evolve",bg='skyblue1', command = button_evolve) #button calls button_evolve function
buttonrandom2 = tk.Button(form,text="Random",bg='maroon1', command = button_random) #button calls search_button function
buttonnext = tk.Button(form,text=">",bg='grey', command = button_next) #button calls search_button function
buttonback = tk.Button(form,text="<",bg='grey', command = button_back) #button calls search_button function
buttonnext2 = tk.Button(form,text=">>",bg='grey', command = button_next) #button calls search_button function
buttonback2 = tk.Button(form,text="<<",bg='grey', command = button_back) #button calls search_button function
buttonplustwenty = tk.Button(form,text="+",bg='grey', command = button_plustwenty) #button calls search_button function
buttonminustwenty = tk.Button(form,text="-",bg='grey', command = button_minustwenty) #button calls search_button function
randomsix = tk.Button(form,text="Random Team",bg='pink', command = random_six) #button calls search_button function
canvas1.create_window(180,150,window=pokemon_label)
canvas1.create_window(185,345,window=search_label)
canvas1.create_window(280,150,window=num_label)
canvas1.create_window(180,167,window=type_label)
canvas1.create_window(180,187,window=type2_label)
canvas1.create_window(72,167,window=hp_label)
canvas1.create_window(79,187,window=attack_label)
canvas1.create_window(82,227,window=defense_label)
canvas1.create_window(86,207,window=spatk_label)
canvas1.create_window(90,247,window=spdef_label)
canvas1.create_window(77,267,window=speed_label)
canvas1.create_window(87,287,window=total_label)
canvas1.create_window(91,307,window=power_label)
canvas1.create_window(194,227,window=growth_label)
canvas1.create_window(190,207,window=leg_label)
canvas1.create_window(258, 345, window=inputtxt, width=100)
canvas1.create_window(145,165,window=namelabel, tags="name")
canvas1.create_window(60, 397, height=28,width=53, window=buttonpoweroff)
canvas1.create_window(60, 424, height=28,width=53, window=buttonpoweron)
canvas1.create_window(115, 350, height=35,width=70, window=buttonpokesearch)
canvas1.create_window(151, 475, height=50,width=112, window=buttoncatch)
canvas1.create_window(630, 492, height=50,width=112, window=buttonbulpedia)
canvas1.create_window(125, 405, height=25,width=65, window=buttonevolve)
canvas1.create_window(196, 405, height=25,width=65, window=buttonrandom)
canvas1.create_window(583, 408, height=25,width=65, window=buttonevolve2)
canvas1.create_window(653, 408, height=25,width=65, window=buttonrandom2)
canvas1.create_window(315, 438, height=20,width=30, window=buttonnext)
canvas1.create_window(265, 438, height=20,width=30, window=buttonback)
canvas1.create_window(525, 441, height=32,width=31, window=buttonnext2)
canvas1.create_window(489, 441, height=32,width=31, window=buttonback2)
canvas1.create_window(290, 410, height=30,width=20, window=buttonplustwenty)
canvas1.create_window(290, 463, height=30,width=20, window=buttonminustwenty)
canvas1.create_window(505, 492, height=50,width=112, window=randomsix)
###############################################################################################################

#randomly launches a pokemon at launch
button_random()

#initiate main form
form.mainloop()

