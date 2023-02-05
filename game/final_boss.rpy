# Final Boss
# Variables
define image_attack_button = "temp button.png"
define image_defend_button = "temp button.png"
define image_items_button = "temp button.png"
define image_run_button = "temp button.png"



#  Labels
label final_boss:

    scene fight bg
    play music music_final_boss

    show superbug idle

    # (!)
    $ font = "fonts/PressStart2P-Regular.ttf"
    "Super Bug wants to Fight!"

    show superbug shoot
    "Fight!"

    call screen rpg_battle

    return


# Final Battle
screen rpg_battle:
    imagebutton: # Button 1
        xanchor 0.5
        yanchor 0.5
        xpos 0.30
        ypos 0.80
        idle "temp button.png" at button_animation()

    imagebutton: # Button 2
        xanchor 0.5
        yanchor 0.5
        xpos 0.50
        ypos 0.80
        idle "temp button.png" at button_animation()

    imagebutton: # Button 3
        xanchor 0.5
        yanchor 0.5
        xpos 0.70
        ypos 0.80
        idle "temp button.png" at button_animation()


# Animations
image superbug idle:
    xanchor 0.5
    yanchor 0.5
    xpos 0.25
    ypos 0.5
    im.FactorScale("bug idle/bug idle1.png", 3)
    pause 0.5
    im.FactorScale("bug idle/bug idle2.png", 3)
    pause 0.5
    repeat


image superbug shoot:
    xpos 0.3
    im.FactorScale("bug shoot/bug shoot1.png", 5)
    pause 0.1
    im.FactorScale("bug shoot/bug shoot2.png", 5)
    pause 0.1
    repeat


# Python for animation (not working!)
init python:
    def shoot(st, at):
        if st > 5.0:
            return "bug idle/bug idle1.png", None
        elif st % 0.2 == 0:
            return im.FactorScale("bug shoot/bug shoot1.png", 5), 0.1
        else:
            return im.FactorScale("bug shoot/bug shoot2.png", 5), 0.1
