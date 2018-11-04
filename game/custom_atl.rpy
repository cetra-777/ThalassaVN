# ATL Animation and Transition Language

# Custom transforms, call with the keyword "at" such as "show pika at bounce"

# A bounce animation
transform bounce:
    xalign 0.5 yalign 0.5
    linear 0.5 yalign 0.0
    linear 1.0 yalign 0.5

# Define an Indivdual Image
#image pika:
#    "pika.jpg"
#    size(200,200)

# Define an animation
#
#image run_animation:
    #frame0.png
    #0.1
    #frame1.png
    #0.1
    #etc...
    #repeat #Repeats animation in a loop.
