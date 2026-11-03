contadorA = 0
contadorB = 0

def on_button_pressed_a():
    global contadorA
    contadorA += 1
    basic.show_number(contadorA)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global contadorB
    contadorB += 1
    basic.show_number(contadorB)
input.on_button_pressed(Button.B, on_button_pressed_b)
