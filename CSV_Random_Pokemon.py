import csv, operator
import random


spatklist = []
pokemonlist = []
with open("pokemon.csv", newline='') as csv_file:
        for index in csv.reader(csv_file):
            pokemonlist.append(index)

with open("pokemon.csv") as csv_file:
    reader=csv.reader(csv_file, delimiter=',')
    
        


mylist = []

count = 1
for i in range(6):
    rand_int = random.randint(1,151)
    mylist.append(pokemonlist[rand_int])
    i+=1


for item in mylist:
    print(item[0])
# count =1 
# while count < 6:
#     for item in pokemonlist:
#         randint = random.randint(1,151)
#         for i in mylist:
#             if mylist[2] != pokemonlist[2]:
#                 mylist.append(pokemonlist[randint])
#                 count+=1

#print(mylist)
        
        



data = csv.reader(open("pokemon.csv"), delimiter=',')
data = sorted(data, key=operator.itemgetter(4))








    