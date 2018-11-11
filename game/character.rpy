init python:
    class Player:
        def __init__(self, hp, mp, max_hp, max_mp, atk, defense, charm, courage, academics, familiar, amulet):
            self.hp = hp
            self.mp = mp
            self.max_hp = max_hp
            self.max_mp = max_mp
            self.atk = atk
            self.defense = defense
            self.charm = charm
            self.courage = courage
            self.academics = academics
            self.familiar = None
            self.amulet = None

        def addHP(self, amount):
            self.hp += amount
            if self.hp > self.max_hp:
                self.hp = self.max_hp

        def addMP(self, amount):
            self.mp += amount
            if self.mp > self.max_mp:
                self.mp = self.max_mp

        def equip_familiar(self, familiar):
            if self.familiar != None:
                unequip_familiar()

            self.familiar = familiar
            self.hp += familiar.hp_bonus
            self.mp += familiar.mp_bonus
            self.charm += familiar.charm_bonus
            self.courage += familiar.courage_bonus
            self.academics += familiar.academics_bonus

        def unequip_familiar(self):
            self.hp -= familiar.hp_bonus
            self.mp -= familiar.mp_bonus
            self.charm -= familiar.charm_bonus
            self.courage -= familiar.courage_bonus
            self.academics -= familiar.academics_bonus
            self.familiar = None
