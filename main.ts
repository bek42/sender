//  3 seconds delay between weather data sends
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
})
function send_rainfall_data(): string {
    return "1"
}

function send_weather_data() {
    
    let weather_group = 0
    lightVal = input.lightLevel()
    row = "" + ("" + Math.idiv(weatherbit.temperature(), 100)) + ";" + ("" + ("" + Math.idiv(weatherbit.humidity(), 1024))) + ";" + ("" + ("" + Math.idiv(weatherbit.pressure(), 25600))) + ";" + ("" + ("" + weatherbit.altitude()))
    radio.setGroup(weather_group)
    //  Switch to weather data group
    radio.sendString(row)
    //  send the weather info via radio
    basic.pause(50)
}

input.onButtonPressed(Button.B, function on_button_pressed_b() {
    basic.showString("S")
    basic.clearScreen()
})
let row = ""
let lightVal = 0
radio.setTransmitPower(7)
weatherbit.startWeatherMonitoring()
basic.forever(function on_forever() {
    //  Send weather data every 3 seconds
    send_weather_data()
    basic.pause(3000)
})
basic.forever(function on_forever2() {
    let rain_group = 1
    radio.setGroup(rain_group)
    send_rainfall_data()
})
