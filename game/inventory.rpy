init python:
    class InventoryItem:
        def __init__(self, value):
            self.value = value

    class Familiar(InventoryItem):
        def __init__(self, name, hp_bonus, mp_bonus, atk_bonus, def_bonus, charm_bonus, courage_bonus, academics_bonus, ability = "None"):
            self.name = name
            self.hp_bonus = hp_bonus
            self.mp_bonus = mp_bonus
            self.atk_bonus = atk_bonus
            self.def_bonus = def_bonus
            self.charm_bonus = charm_bonus
            self.courage_bonus = courage_bonus
            self.academics_bonus = academics_bonus
            self.ability = ability
