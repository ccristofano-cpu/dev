class Personnage : 

    def __init__(self, name: str):
       self.name: str = name 
       self.hp: int = 100
       self.mana: int = 50
       self.atq : int = 5
       self.defense: float = 0.5 

    def attack (self, cible : any) : 
        cible.hp -= self.atq / cible.defense

    def capacite(self,cible: any) :
        cout_mana = 10
        degats = 20
        if self.mana >= cout_mana:
        self.mana -= cout_mana
        cible.hp -= degats / cible.defense

    def __str__(self) :
        return f"(self.name) : (self.hp) , (self mana),(self attaque)"

       ####################

    perso_1 = Personnage(Alex)
    perso_2 = Personnage(Thomas)
     perso_1.attack (perso_2)
    perso_1.capacite(perso_2)

  print(f"Nom:(self.name)"
  print(f"HP: self.hp)"
  print(f"Mana: self.mana)"
  print(f"Attaque: self.atq)"
  print(f"Defense: self.defense)"
    