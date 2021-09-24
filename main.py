def on_button_pressed_a():
    basic.show_leds("""
        # . # . .
                . # # # .
                . . # . #
                . # . # .
                . # . . #
    """)
    basic.show_leds("""
        . . # . .
                # # # # #
                . . # . .
                . # . # .
                . # . # .
    """)
    basic.show_leds("""
        . . # . #
                . # # # .
                # . # . .
                . # . # .
                # . . # .
    """)
    basic.show_leds("""
        . . # . .
                # # # # #
                . . # . .
                . # . # .
                . # . # .
    """)
    basic.show_leds("""
        # . # . #
                . # # # .
                . . # . .
                . # . # .
                . # . # .
    """)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    basic.show_string("Hello!")
    music.play_melody("E B C5 A B G A F ", 120)
    music.play_melody("C5 A B G A F G E ", 120)
    music.play_melody("A F E F D G E F ", 120)
input.on_button_pressed(Button.B, on_button_pressed_b)
