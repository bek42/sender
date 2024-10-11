def on_button_pressed_a():
    global item
    radio.send_number(1)
    item += 1
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    basic.show_string("S")
    basic.clear_screen()
input.on_button_pressed(Button.B, on_button_pressed_b)

radio.set_group(1)
radio.set_transmit_power(7)
item = 0
lightVal = 0
weatherbit.start_weather_monitoring()

def on_forever():
    global lightVal, item
    lightVal = input.light_level()
    if item == 0:
        basic.show_string("Temp C: ")
        basic.show_number(Math.idiv(weatherbit.temperature(), 100))
    elif item == 1:
        basic.show_string("Humidity %: ")
        basic.show_number(Math.idiv(weatherbit.humidity(), 1024))
    elif item == 2:
        basic.show_string("Pressure hPa: ")
        basic.show_number(Math.idiv(weatherbit.pressure(), 25600))
    else:
        item = 0
basic.forever(on_forever)
