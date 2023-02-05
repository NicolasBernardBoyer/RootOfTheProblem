label computer_final_scene:
    # (!) Change Music
    
    play music music_ambience2 fadeout 2
    scene boss computer
    call screen screen_computer2

    return

screen screen_computer2:
    imagebutton: #Paint
        xanchor 0.5
        yanchor 0.5
        xpos 0.5
        ypos 0.5
        idle icon_virus
        hover im.FactorScale(icon_virus, 1.1)
        action [Play(file=renpy.random.choice(sound_clicks),channel="sound"), Jump("final_boss")]
        mouse "computer"
