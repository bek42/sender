/**
 * 3 seconds delay between weather data sends
 */
input.onButtonPressed(Button.A, function () {
	
})
function send_weather_data () {
    lightVal2 = input.lightLevel()
    row = "" + Math.idiv(weatherbit.temperature(), 100) + ";" + ("" + Math.idiv(weatherbit.humidity(), 1024)) + ";" + ("" + Math.idiv(weatherbit.pressure(), 25600)) + ";" + ("" + weatherbit.altitude())
    radio.setGroup(weather_group)
    // Switch to weather data group
    radio.sendString(row)
    // send the weather info via radio
    basic.pause(50)
}
input.onButtonPressed(Button.B, function () {
    basic.showString("S")
    basic.clearScreen()
})
let lightVal2 = 0
let weather_group = 0
let row = ""
let lightVal = 0
let row2 = ""
row = ""
weather_group = 1
radio.setGroup(1)
radio.setTransmitPower(7)
weatherbit.startWeatherMonitoring()
basic.forever(function () {
    // Send weather data every 3 seconds
    send_weather_data()
    basic.pause(3000)
})
