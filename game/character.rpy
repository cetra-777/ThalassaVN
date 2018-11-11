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
                self.unequip_familiar(familiar)

            self.familiar = familiar
            self.hp += self.familiar.hp_bonus
            self.mp += self.familiar.mp_bonus
            self.atk += self.familiar.atk_bonus
            self.defense += self.familiar.def_bonus
            self.charm += self.familiar.charm_bonus
            self.courage += self.familiar.courage_bonus
            self.academics += self.familiar.academics_bonus

        def unequip_familiar(self, familiar):
            self.familiar = pc.familiar

            self.hp -= self.familiar.hp_bonus
            self.mp -= self.familiar.mp_bonus
            self.atk -= self.familiar.atk_bonus
            self.defense -= self.familiar.def_bonus
            self.charm -= self.familiar.charm_bonus
            self.courage -= self.familiar.courage_bonus
            self.academics -= self.familiar.academics_bonus
            self.familiar = ring
