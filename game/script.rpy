# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")

screen clickable_item:
    imagebutton:
        xpos 0.5
        ypos 0.5
        idle "click temp.png"
        action Jump("end")

    imagebutton:
        xpos 0.2
        ypos 0.2
        idle "click temp.png"
        hover "click temp.png"

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg temp
    call screen clickable_item

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.
    # show eileen happy

    # These display lines of dialogue.

    # e "You've created a new Ren'Py game."

    # e "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return

# End
label end:
    
    e "Next Step"
    return