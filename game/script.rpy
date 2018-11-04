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
default selected_item = None
default pc = Player(7, 5, 5, 3, 2, 1)

default sword_item = Weapon("item1", 10, 5, "sword")
default pie_item = Consumable("item2", 50, 100, 0)
default cauldron_item = KeyItem("item2")
default shield_item = Armor("item1", 15, 5, 4, "shield")

# The game starts here.

label start:

    # Setup Inventory and other lists/dicts used by this game.
    $ numbers = ["One", "Two", "Three", "Four"]

    # Setup Variables
    $ image_button_total = 0

    # Load a scene and show a background.
    #scene bg example
    show screen hbox_screen(numbers, 50)

    # Show a character on the screen.
    #show evie happy

    n "This is Evette Sinclaire. A run of the mill worker at the Sea Foam Cafe
    in Asfaelia."

    hide screen hbox_screen
    show screen vbox_screen(numbers, 50)

    n "Thanks for playing."

    hide screen vbox_screen
    show screen grid_screen(numbers, 50)

    n "Thank you"

    hide screen grid_screen
    show screen combo_screen
    n "The end"
    # This ends the game.

    return
