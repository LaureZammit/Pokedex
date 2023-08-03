class Pokemon():
    def __init__(self, name, type, number, hp, attack, defense, vit, competence1, competence2, image):
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
        self.image = image