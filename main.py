# 3 seconds delay between weather data sends

row = ""
row2 = ""
lightVal = 0
row = ""
weather_group = 0
weather_group = 1
radio.set_group(1)
radio.set_transmit_power(7)
weatherbit.start_weather_monitoring()


def on_button_pressed_a():
    pass
input.on_button_pressed(Button.A, on_button_pressed_a)

def send_weather_data():
    global row
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

def on_forever_weather():
    # Send weather data every 3 seconds
    send_weather_data()
    basic.pause(3000)
basic.forever(on_forever_weather)



# def on_forever():
    
#     row2 = "" + str(Math.idiv(weatherbit.temperature(), 100)) + "," + ("h" + ("" + str(Math.idiv(weatherbit.humidity(), 1024)))) + "," + ("p" + ("" + str(Math.idiv(weatherbit.pressure(), 25600)))) + "," + ("a" + ("" + str(weatherbit.altitude())))
#     radio.send_string(row2)
#     basic.pause(1 * 3000)
# basic.forever(on_forever)
