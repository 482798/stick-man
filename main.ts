input.onButtonPressed(Button.A, function () {
    basic.showLeds(`
        # . # . .
        . # # # .
        . . # . #
        . # . # .
        . # . . #
        `)
    basic.showLeds(`
        . . # . .
        # # # # #
        . . # . .
        . # . # .
        . # . # .
        `)
    basic.showLeds(`
        . . # . #
        . # # # .
        # . # . .
        . # . # .
        # . . # .
        `)
    basic.showLeds(`
        . . # . .
        # # # # #
        . . # . .
        . # . # .
        . # . # .
        `)
    basic.showLeds(`
        # . # . #
        . # # # .
        . . # . .
        . # . # .
        . # . # .
        `)
})
input.onButtonPressed(Button.B, function () {
    basic.showString("Hello!")
    basic.showIcon(IconNames.Happy)
    music.playMelody("E B C5 A B G A F ", 120)
    music.playMelody("C5 A B G A F G E ", 120)
    music.playMelody("A F E F D G E F ", 120)
})
