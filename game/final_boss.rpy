# Final Boss
# Variables

# (!) Remove
define image_attack_button = "temp button.png"
define image_defend_button = "temp button.png"
define image_items_button = "temp button.png"
define image_run_button = "temp button.png"


# Font for fight. Use Style instead...
define pixel_font = "fonts/PressStart2P-Regular.ttf"

# Text Style for buttons. Deprecated
style button_style is text:
    size 40
    font pixel_font


#  Labels
label final_boss:

    scene fight bg
    play music music_final_boss

    show superbug idle

    "{font=[pixel_font]}Super Bug wants to Fight!{/font}"

    show superbug shoot
    "Fight!"

    call screen rpg_battle

    return


# (!) Not used
label attack:
    "Attack!"
    call screen rpg_battle
    return

# Final Battle
screen rpg_battle:

    textbutton "Attack" at button_animation:
        xanchor 0.5
        yanchor 0.5
        xpos 0.20
        ypos 0.80
        text_font pixel_font
        text_size 40
        text_color '#ffffff'
        action Jump("attack")

    textbutton "Defend" at button_animation:
        xanchor 0.5
        yanchor 0.5
        xpos 0.40
        ypos 0.80
        text_font pixel_font
        text_color '#ffffff'
        action Jump("attack")

    textbutton "Items" at button_animation:
        xanchor 0.5
        yanchor 0.5
        xpos 0.60
        ypos 0.80
        text_font pixel_font
        text_color '#ffffff'
        action Jump("attack")

    textbutton "Run!" at button_animation:
        xanchor 0.5
        yanchor 0.5
        xpos 0.80
        ypos 0.80
        text_font pixel_font
        text_color '#ffffff'
        action Jump("attack")


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
    xanchor 0.5
    yanchor 0.5
    xpos 0.25
    ypos 0.5
    im.FactorScale("bug shoot/bug shoot1.png", 3)
    pause 0.1
    im.FactorScale("bug shoot/bug shoot2.png", 3)
    pause 0.1
    repeat

transform button_animation():
    linear renpy.random.randint(1, 3) / 10.0 rotate renpy.random.randint(2, 10) / 20
    pause 0.2
    linear renpy.random.randint(1, 3) / 10.0 rotate renpy.random.randint(2, 10) * -1 / 20
    pause 0.2
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
