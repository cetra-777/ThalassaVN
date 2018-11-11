################################################################################
## Click to Continue Screen
################################################################################
screen ctc():

    frame:
        at ctc_appear
        xalign .99
        yalign .99

        text _("(click to continue)"):
            size 18

transform ctc_appear:
    alpha 0.0
    pause 5.0
    linear 0.5 alpha 1.0

################################################################################
## Tutorial Screens
################################################################################
style centered_style:
    xalign 0.5
    yalign 0.5
    spacing 5

style centered_style_text is text:
    size 22
    hover_color "#d6db4a"
    outlines [ (0, "#b2b2b0", 1, 1) ]
    color "#ffffff"

style combo_text:
    size 50

style combo_hbox is centered_style

# Function creation
init python:
    def incTotal():
        global image_button_total
        image_button_total += 1

screen hbox_screen(buttons = ['Test'], text_size = 30):
    hbox:
        style "centered_style"
        spacing 10
        xmaximum 300
        box_wrap True # Respects xmaximum
        for button in buttons:
            textbutton button:
                action Null
                text_size text_size
                style "centered_style"

screen vbox_screen(buttons = ['Test'], text_size = 30):
    vbox:
        xalign 0.1
        yalign 0.1
        spacing 5
        for button in buttons:
            textbutton button:
                action Null
                text_size text_size
                style "centered_style"

# Displays children in a grid
screen grid_screen(buttons = ["Test1", "Test2"], text_size = 30):
    grid 2 len(buttons)/2+1:
        spacing 5
        xalign 0.8
        yalign 0.1
        for button in buttons:
            textbutton button:
                action Null
                text_size text_size
                style "centered_style"
        for i in range(0, (len(buttons)/2 +1) * 2 - len(buttons)):
            null

screen combo_screen:
    hbox:
        style_prefix "combo"
        vbox:
            yalign 0.5
            text "One"
            text "Two"
            text "Three"
        vbox:
            text "Four"
            text "Five"
            text "Six"
            text "Seven"
        text "Total: [image_button_total]" # shows global image_button_total
        imagebutton auto "button_%s.png":
            action Function(incTotal)

################################################################################
## Custom Inventory Screen
################################################################################
style inventory_items is button:
    background "#b2b2a9"
style inventory_items_text is text:
    size 22
    hover_color "#d6db4a"
    outlines [ (0, "#b2b2b0", 1, 1) ]
    color "#1c2428"

screen familiar():

    tag menu

    use game_menu(_("Inventory"), scroll="viewport"):

        style_prefix "inventory"

        has vbox:
            spacing 20

        python:
            inv = []
            for i in range(len(inventory)):
                inventory_text = inventory[i].name
                inv.append(inventory_text)
                inv.append("\n")

        text inv
################################################################################
## Inventory Item Screens
################################################################################
screen cheese():

    tag menu

    use game_menu(_("Inventory"), scroll="viewport"):

        style_prefix "inventory"

        has vbox:
            spacing 20

        text _("{b}Cheese:{/b} Tasty but addictive.")
