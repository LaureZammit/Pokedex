from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

fenetre = Tk()
fenetre.title("Pokedex")
fenetre.geometry("1000x700")
fenetre.resizable(False, False)

fenetre.config(bg='red')

ttk.Separator(fenetre, orient=VERTICAL).grid(row=0, columnspan=1, ipadx=272)

# Déclaration de la taille de ma fenêtre de gauche avec les infos affichés
left_frame = Frame(fenetre, width=450, height=650, bg='white')
left_frame.grid(row=0, column=0, padx=1, pady=1)

rigth_frame = Frame(fenetre, width=400, height=650, bg='white')
rigth_frame.grid(row=0, column=1, padx=1, pady=1)


# Déclaration de mes Label sur left_frame
pok_name = Label(left_frame, text="Nom", font=("Arial 30"), bg='white').place(x=10, y=10)
pok_number = Label(left_frame, text="Numéro", font=("Arial", 16), bg='white').place(x=10, y=300)
pok_type = Label(left_frame, text="Type", font=("Arial", 16), bg='white').place(x=10, y=330)
pok_comp = Label(left_frame, text="Compétences", font=("Arial", 16), bg='white').place(x=10, y=360)
pok_hp = Label(left_frame, text="HP", font=("Arial", 16), bg='white').place(x=10, y=450)
pok_attack = Label(left_frame, text="Attaque", font=("Arial", 16), bg='white').place(x=10, y=480)
pok_defense = Label(left_frame, text="Défense", font=("Arial", 16), bg='white').place(x=10, y=510)
pok_vit = Label(left_frame, text="Vitesse", font=("Arial", 16), bg='white').place(x=10, y=540)
pok_total = Label(left_frame, text="Total", font=("Arial", 16), bg='white').place(x=10, y=600)

# Déclaration des variables
poke_name = Label(left_frame, text="Bulbizarre", font=("Arial 28"), bg='white', fg='black').place(x=150, y=14)
poke_number = Label(left_frame, text="#001", font=("Arial 16"), bg='grey', fg='white').place(x=190, y=300)
poke_type = Label(left_frame, text="Plante / Poison", font=("Arial 16"), bg='white', fg='black').place(x=190, y=330)
poke_comp1 = Label(left_frame, text="Fouet Lianes", font=("Arial 16"), bg='white', fg='black').place(x=190, y=360)
poke_comp2 = Label(left_frame, text="Vampigraine", font=("Arial 16"), bg='white', fg='black').place(x=190, y=390)
poke_hp = Label(left_frame, text='45', font=("Arial 16"),bg='white', fg='black').place(x=190, y=450)
poke_attack = Label(left_frame, text='49', font=("Arial 16"), bg='white', fg='black').place(x=190, y=480)
poke_defense = Label(left_frame, text='49', font=("Arial 16"), bg='white', fg='black').place(x=190, y=510)
poke_vit = Label(left_frame, text='45', font=("Arial 16"), bg='white', fg='black').place(x=190, y=540) 
poke_total = Label(left_frame, text='237', font=("Arial 16"), bg='white', fg='black').place(x=190, y=600)


# Déclaration de mes images
pok_image = Image.open("img/bg_pokemon.jpg")
pok_image = pok_image.resize((300, 200))
pok_image = ImageTk.PhotoImage(pok_image)

img_base = Label(left_frame, image=pok_image)
img_base.place(x=70, y=70)


# Déclaration de ma Listbox sur rigth_frame
pok_list = Label(rigth_frame, width=20, height=34, font=("Arial", 12), bg='white', relief=SUNKEN).place(x=10, y=10)


# Création d'un bouton pour ajouter un pokemon à la liste

fenetre.mainloop()