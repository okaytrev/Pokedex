import random
import csv

pokemonlist = []
rand_int = random.randint(1,151)

with open("pokemon.csv", newline='') as csv_file:
        for index in csv.reader(csv_file):
            pokemonlist.append(index)



def current_pokemon_list():

    input_string = inputtxt.get()

    for row in pokemonlist:
        if row[1] == input_string:
            single_pokemon_list = row 

    return(single_pokemon_list)



#single_pokemon_list = pokemonlist[150][1]       

#print(single_pokemon_list)

# def update_labels(single_pokemon_list):
#     global pokeimage
#     type1 = single_pokemon_list[2]
#     type2 = single_pokemon_list[3]
#     hp = single_pokemon_list[5]
#     attack = single_pokemon_list[6]
#     defense = single_pokemon_list[7] 
#     spatk = single_pokemon_list[8]
#     spdef = single_pokemon_list[9]
#     speed = single_pokemon_list[10]
#     legendary = single_pokemon_list[12]
#     image = single_pokemon_list[0] 

#     typelabel = tk.Label(form,bg='white',text=type1)
#     typelabel2 = tk.Label(form,bg='white',text=type2)
#     hplabel = tk.Label(form,bg='white',text=hp)
#     attacklabel = tk.Label(form,bg='white',text=attack)
#     defenselabel = tk.Label(form,bg='white',text=defense)
#     spatklabel = tk.Label(form,bg='white',text=spatk)
#     spdeflabel = tk.Label(form,bg='white',text=spdef)
#     speedlabel = tk.Label(form,bg='white',text=speed)
#     leglabel = tk.Label(form,bg='white',text=legendary)

#     canvas1.create_window(145,185,window=typelabel,tags="type1")
#     canvas1.create_window(145,205,window=typelabel2, tags="type2")
#     canvas1.create_window(145,225,window=hplabel)
#     canvas1.create_window(145,245,window=attacklabel)
#     canvas1.create_window(145,265,window=defenselabel)
#     canvas1.create_window(145,285,window=spatklabel)
#     canvas1.create_window(145,305,window=spdeflabel)
#     canvas1.create_window(255,185,window=speedlabel)
#     canvas1.create_window(255,205,window=leglabel)

#     pokeimage = set_image(image)
#     #pokeimage = PhotoImage(file = pokeimage1)
#     pokelabel = Label(form,image=pokeimage) #calls image function 
#     canvas1.create_window(573,273,window=pokelabel)