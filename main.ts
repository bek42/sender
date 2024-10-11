input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    radio.sendNumber(1)
    item += 1
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    basic.showString("S")
    basic.clearScreen()
})
radio.setGroup(1)
radio.setTransmitPower(7)
let item = 0
let lightVal = 0
weatherbit.startWeatherMonitoring()
basic.forever(function on_forever() {
    
    lightVal = input.lightLevel()
    if (item == 0) {
        basic.showString("Temp C: ")
        basic.showNumber(Math.idiv(weatherbit.temperature(), 100))
    } else if (item == 1) {
        basic.showString("Humidity %: ")
        basic.showNumber(Math.idiv(weatherbit.humidity(), 1024))
    } else if (item == 2) {
        basic.showString("Pressure hPa: ")
        basic.showNumber(Math.idiv(weatherbit.pressure(), 25600))
    } else {
        item = 0
    }
    
})
