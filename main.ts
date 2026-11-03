let contadorA = 0
let contadorB = 0
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    contadorA += 1
    basic.showNumber(contadorA)
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    
    contadorB += 1
    basic.showNumber(contadorB)
})
