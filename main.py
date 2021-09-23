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
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    music.play_melody("E B C5 A B G A F ", 120)
    basic.show_string("Hello!")
input.on_button_pressed(Button.B, on_button_pressed_b)
