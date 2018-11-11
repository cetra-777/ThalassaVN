# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# define e = Character("Eileen")
define e = Character("Evie")
define s = Character("Subitha")
define t = Character("Timon")
define l = Character("Lei Ti")
define k = Character("Kor Ti")
define n = Character("Narrator")

# Declare variables used by this game.
default inventory = []

# hp, mp, max_hp, max_mp, atk, defense, charm, courage, academics, familiar, amulet
default pc = Player(10, 5, 10, 5, 2, 1, 0, 0, 0, None, None)

# name, hp_bonus, mp_bonus, atk_bonus, def_bonus, charm_bonus, courage_bonus, academics_bonus, ability
default pixie = Familiar("Pixie", 1, 1, 0, 1, 1, 0, 0)
default salamander = Familiar("Salamander", 1, 1, 2, 2, 1, 0, 0)
default ring = Familiar("Ring", 0, 0, 0, 0, 0, 0, 0)

# The game starts here.

label start:

    # images

    # Starting Items


    # Setup Variables

    # Show a character on the screen.
    #show evie happy

    n "This is Evette Sinclaire. A run of the mill worker at the Sea Foam Cafe
    in Asfaelia."
    $ pc.equip_familiar(ring)

    n "Her stats are: hp [pc.hp] mp [pc.mp] atk [pc.atk] defense [pc.defense] charm [pc.charm] courage [pc.courage] academics [pc.academics] familiar [pc.familiar] amulet [pc.amulet]"

    n "Here"
    $ inventory.append(pixie)
    $ inventory.append(salamander)
    $ pc.equip_familiar(pixie)

    n "Now her stats are: hp [pc.hp] mp [pc.mp] atk [pc.atk] defense [pc.defense] charm [pc.charm] courage [pc.courage] academics [pc.academics] familiar [pc.familiar.name] amulet [pc.amulet]"

    $pc.unequip_familiar(pixie)

    n "Now her stats are: hp [pc.hp] mp [pc.mp] atk [pc.atk] defense [pc.defense] charm [pc.charm] courage [pc.courage] academics [pc.academics] familiar [pc.familiar.name] amulet [pc.amulet]"
    # This ends the game.

    return
