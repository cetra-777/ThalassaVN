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
default variableOne = False
# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    # scene bg room
    scene bg cafe

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # show eileen happy
    show evie happy

    # These display lines of dialogue.

    n "This is Evette Sinclaire. A run of the mill worker at the Sea Foam Cafe in Asfaelia."

    show evie waving

    e "Hello!"

    n "She doesn't know it yet but you and her are going to be having quite and adventure!"

    e "Wait, what did he say?"

    n "Ahem, nothing, nothing at all. Now then, I believe things are about to begin."

    # play doorbell

    show evie happy at center

    e "Oh hello! Welcome to the Sea Foam. What can I get started for you."

    show subitha cloak at right

    s "A black coffee please."

    e "Okie-dokie, have that for you in just a second"

    # This ends the game.

    return
