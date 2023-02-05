# Characters
define mc = Character("[mc_name]")
define v = Character("Vina", color="#4b65ad")
define n = Character("Nor", color="#9d471f")
define se = Character("ShadowEdge12", color="#736568")
define s = Character("Superbug", color="#2e8838")
define unknown = Character("???", color="#5195c0")

# music
define music_ambience = "audio/music/AMBIENCE 1.mp3"
define music_ambience2 = "audio/music/AMBIENCE 2.mp3"
define music_character_creation = "audio/music/CHARACTER CREATION THEME.mp3"
define music_final_boss = "audio/music/FINAL BOSS THEME.mp3"

define sound_click_slow = "audio/SFX/Button Slow.mp3"
define sound_click_normal = "audio/SFX/Button Normal.mp3"
define sound_click_fast = "audio/SFX/Button Fast.mp3"
define sound_clicks = [sound_click_slow, sound_click_normal, sound_click_fast]

# Image Effects
define hover_effect = im.Flip("click temp.png", vertical=True)
define scale_effect = im.FactorScale("click temp.png", 1.2)
define tint_effect = im.MatrixColor(
    "click temp.png",
    im.matrix.tint(1, 0.5, 1)
)

# Images
define icon_folder = "computer files.png"
define icon_checker = "file pic.png"
define icon_mug = "mug pic.png"
define icon_mug_egg = "mug easter egg.png"
define icon_paint = "mspaint icon.png"
define icon_text = "txt icon.png"
define icon_solitaire = "solitare icon.png"
define icon_trash = "computer trash.png"
define icon_virus = "virus icon.png"
define icon_webpage = "webpage icon.png"

define app_folder = "file explorer.png"
define app_paint = "mspaint.png"
define app_real = "error for real.PNG"
define app_text = "txt page.png"
define app_web = "webpage.png"

transform edge_position:
    xalign 0.25
    yalign 1.0



# Transforms
transform left_to_right:
    xalign 0.0
    linear 2.0 xalign 1.0
    repeat

transform button_animation():
    linear renpy.random.randint(1, 3) / 10.0 rotate renpy.random.randint(2, 10)
    pause 0.2
    linear renpy.random.randint(1, 3) / 10.0 rotate renpy.random.randint(2, 10) * -1
    pause 0.2
    repeat
