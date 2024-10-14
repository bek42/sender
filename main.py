# 3 seconds delay between weather data sends

def on_button_pressed_a():
    pass
input.on_button_pressed(Button.A, on_button_pressed_a)

def send_rainfall_data():
    return "1"
def send_weather_data():
    global lightVal, row
    weather_group = 0
    lightVal = input.light_level()
    row = "" + str(Math.idiv(weatherbit.temperature(), 100)) + ";" + ("" + str(Math.idiv(weatherbit.humidity(), 1024))) + ";" + ("" + str(Math.idiv(weatherbit.pressure(), 25600))) + ";" + ("" + str(weatherbit.altitude()))
    radio.set_group(weather_group)
    # Switch to weather data group
    radio.send_string(row)
    # send the weather info via radio
    basic.pause(50)

def on_button_pressed_b():
    basic.show_string("S")
    basic.clear_screen()
input.on_button_pressed(Button.B, on_button_pressed_b)

row = ""
lightVal = 0
radio.set_transmit_power(7)
weatherbit.start_weather_monitoring()

def on_forever():
    # Send weather data every 3 seconds
    send_weather_data()
    basic.pause(3000)
basic.forever(on_forever)

def on_forever2():
    rain_group = 1
    radio.set_group(rain_group)
    send_rainfall_data()
basic.forever(on_forever2)
