  # Toplevel object which will
    # be treated as a new window
    newWindow = Toplevel(form)
    # sets the title of the
    # Toplevel widget
    newWindow.title("Image")
    # sets the geometry of toplevel
    newWindow.geometry("200x200")
    # A Label widget to show in toplevel
    Label(newWindow, text ="This is a new window").pack()




    #pokeimage = Image.open("Test.png")
    #pokeimage = ImageTk.PhotoImage(Image.open("C:\\Users\\TrevarHupf\\Documents\\Scripts\\Pokedex\\PokeImages\\" + image +".jpg"))
    #backimage.paste(pokeimage (20, 40))
    #pokeimage_label = tk.Label(form,image=pokeimage).place(x=300,y=300)
    #canvas1.create_window(145,185,window=pokeimage_label)