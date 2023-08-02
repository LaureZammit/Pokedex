from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk


fenetre = Tk()
fenetre.title("Pokedex")
fenetre.geometry("1000x700")
fenetre.resizable(False, False)

fenetre.config(bg='red')

ttk.Separator(fenetre, orient=VERTICAL).grid(row=0, columnspan=1, ipadx=272)


# Déclaration de la taille de mes fenêtres
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
poke_name = Label(left_frame, text="Bulbizarre", font=("Arial 28"), bg='white', fg='black')
poke_name.place(x=150, y=14)
poke_number = Label(left_frame, text="#001", font=("Arial 16"), bg='grey', fg='white')
poke_number.place(x=190, y=300)
poke_type = Label(left_frame, text="Plante / Poison", font=("Arial 16"), bg='white', fg='black')
poke_type.place(x=190, y=330)
poke_comp1 = Label(left_frame, text="Fouet Lianes", font=("Arial 16"), bg='white', fg='black')
poke_comp1.place(x=190, y=360)
poke_comp2 = Label(left_frame, text="Vampigraine", font=("Arial 16"), bg='white', fg='black')
poke_comp2.place(x=190, y=390)
poke_hp = Label(left_frame, text='45', font=("Arial 16"),bg='white', fg='black')
poke_hp.place(x=190, y=450)
poke_attack = Label(left_frame, text='49', font=("Arial 16"), bg='white', fg='black')
poke_attack.place(x=190, y=480)
poke_defense = Label(left_frame, text='49', font=("Arial 16"), bg='white', fg='black')
poke_defense.place(x=190, y=510)
poke_vit = Label(left_frame, text='45', font=("Arial 16"), bg='white', fg='black')
poke_vit.place(x=190, y=540) 
poke_total = Label(left_frame, text='237', font=("Arial 16"), bg='white', fg='black')
poke_total.place(x=190, y=600)


class Pokemon():
    def __init__(self, name, type, number, hp, attack, defense, vit, competence1, competence2):
        self.name = name
        self.type = type
        self.number = number
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.vit = vit
        self.total = int(self.hp) + int(self.attack) + int(self.defense) + int(self.vit)
        self.competence1 = competence1
        self.competence2 = competence2

Bulbizarre = Pokemon("Bulbizarre", 
                     "Plante / Poison", 
                     '#001', 
                     '45', '49', '49', '45', 
                     'Vampigraine', 'Fouet Lianes')

Herbizarre = Pokemon("Herbizarre", 
                     "Plante / Poison", 
                     '#002', 
                     '60', '62', '63', '60', 
                     'Danse Fleur', 'Tempête Florale')

Florizarre = Pokemon("Florizarre", 
                     "Plante / Poison", 
                     '#003', 
                     '80', '82', '83', '80', 
                     'Tranch\'Herbe', 'Poudre Dodo')

listPokemons = [Bulbizarre, Herbizarre, Florizarre]

# Ajouter un pokemon saisie
def ajouter_pokemon():
    add_poke = listPokemons.append(Pokemon(saisie_pok_name.get(), 
                                saisie_pok_type.get(), 
                                saisie_pok_number.get(), 
                                saisie_pok_hp.get(), 
                                saisie_pok_attack.get(), 
                                saisie_pok_defense.get(), 
                                saisie_pok_vit.get(), 
                                saisie_pok_comp1.get(), 
                                saisie_pok_comp2.get()
                                ))
    add_pokename = listbox.insert(END, saisie_pok_name.get())

# Choisir le pokemon à afficher
def choose_pokemon():
    index = listbox.curselection()[0]
    poke_name.config(text=listPokemons[index].name)
    poke_number.config(text=listPokemons[index].number)
    poke_type.config(text=listPokemons[index].type)
    poke_comp1.config(text=listPokemons[index].competence1)
    poke_comp2.config(text=listPokemons[index].competence2)
    poke_hp.config(text=listPokemons[index].hp)
    poke_attack.config(text=listPokemons[index].attack)
    poke_defense.config(text=listPokemons[index].defense)
    poke_vit.config(text=listPokemons[index].vit)
    poke_total.config(text=listPokemons[index].total)


# Déclaration de ma Listbox sur rigth_frame
listbox = Listbox(rigth_frame, width=20, height=25, font=("Arial", 12), bg='white', relief=SUNKEN)

# Ajout d'éléments à ma listbox
listbox.insert(END, "Bulbizarre")
listbox.insert(END, "Herbizarre")
listbox.insert(END, "Florizarre")

listbox.place(x=10, y=80)

# Label pour ajouter un pokemon à la liste
l_add_pok_name = Label(rigth_frame, text="Ajouter un pokemon\nAjouter son nom", font=("Arial", 12), bg='white').place(x=220, y=20)
saisie_pok_name = Entry(rigth_frame, font=("Arial", 12), bg='white', relief=SUNKEN)
saisie_pok_name.place(x=210, y=80)

l_add_pok_number = Label(rigth_frame, text="Son numéro", font=("Arial", 12), bg='white').place(x=220, y=110)
saisie_pok_number = Entry(rigth_frame, font=("Arial", 12), bg='white', relief=SUNKEN)
saisie_pok_number.place(x=210, y=140)

l_add_pok_type = Label(rigth_frame, text="Son type", font=("Arial", 12), bg='white').place(x=220, y=170)
saisie_pok_type = Entry(rigth_frame, font=("Arial", 12), bg='white', relief=SUNKEN)
saisie_pok_type.place(x=210, y=200)

l_add_pok_comp = Label(rigth_frame, text="Deux attaques", font=("Arial", 12), bg='white').place(x=220, y=230)
saisie_pok_comp1 = Entry(rigth_frame, font=("Arial", 12), bg='white', relief=SUNKEN)
saisie_pok_comp1.place(x=210, y=260)
saisie_pok_comp2 = Entry(rigth_frame, font=("Arial", 12), bg='white', relief=SUNKEN)
saisie_pok_comp2.place(x=210, y=290)


l_add_pok_hp = Label(rigth_frame, text="HP", font=("Arial", 12), bg='white').place(x=220, y=320)
saisie_pok_hp = Entry(rigth_frame, font=("Arial", 12), bg='white', relief=SUNKEN)
saisie_pok_hp.place(x=210, y=350)

l_add_pok_attaque = Label(rigth_frame, text="Attaque", font=("Arial", 12), bg='white').place(x=220, y=380)
saisie_pok_attack = Entry(rigth_frame, font=("Arial", 12), bg='white', relief=SUNKEN)
saisie_pok_attack.place(x=210, y=410)

l_add_pok_defense = Label(rigth_frame, text="Défense", font=("Arial", 12), bg='white').place(x=220, y=440)
saisie_pok_defense = Entry(rigth_frame, font=("Arial", 12), bg='white', relief=SUNKEN)
saisie_pok_defense.place(x=210, y=470)

l_add_pok_vitesse = Label(rigth_frame, text="Vitesse", font=("Arial", 12), bg='white').place(x=220, y=500)
saisie_pok_vit = Entry(rigth_frame, font=("Arial", 12), bg='white', relief=SUNKEN)
saisie_pok_vit.place(x=210, y=530)

l_add_pok_total = Label(rigth_frame, text="Total", font=("Arial", 12), bg='white').place(x=220, y=560)
saisie_pok_total = Entry(rigth_frame, font=("Arial", 12), bg='white', relief=SUNKEN)
saisie_pok_total.place(x=210, y=590)

# Création d'un bouton pour ajouter un pokemon à la liste
btn_add_poke = Button(rigth_frame, text="Ajouter le Pokemon", command=ajouter_pokemon, font=("Arial", 12), bg='white', relief=RAISED)
btn_add_poke.place(x=10, y=600)

# Création d'un bouton pour sélectionner un pokemon dans la liste
bts_select_pok = Button(rigth_frame, text="Sélectionner", command=choose_pokemon, font=("Arial", 12), bg='white', relief=RAISED)
bts_select_pok.place(x=10, y=20)

fenetre.mainloop()