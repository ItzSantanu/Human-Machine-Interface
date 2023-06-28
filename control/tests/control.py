import toga
from toga.style.pack import COLUMN, LEFT, RIGHT, ROW, Pack


def build(app):
    ams_netid = toga.Box(style=Pack(direction=ROW, padding=5))
    x = toga.Box()
    y = toga.Box()
    z = toga.Box()
    Roll = toga.Box()
    Pitch = toga.Box()
    Yaw = toga.Box()
    #Connect = toga.Box()
    ##calculate_IKIN = toga.Box()
    #Start = toga.Box()
    #Stop = toga.Box()
    #Halt = toga.Box()
    #Reset = toga.Box()
    box = toga.Box(style=Pack(background_color = ("#92b6e8")))

    ams_netid_input = toga.TextInput(readonly=True, style=Pack(width=100 , padding_left = 40))
    x_input = toga.TextInput(style=Pack(padding_left = 40))
    y_input = toga.TextInput(style=Pack(padding_left = 40))
    z_input = toga.TextInput(style=Pack(padding_left = 40))
    Roll_input = toga.TextInput(style=Pack(padding_left = 40))
    Pitch_input = toga.TextInput(style=Pack(padding_left = 40))
    Yaw_input = toga.TextInput(style=Pack(padding_left = 40))

    amsnetid_label = toga.Label("AMS_NET_ID")#, style=Pack(text_align=RIGHT))
    x_label = toga.Label("Enter the value of X", style=Pack(text_align=RIGHT))
    y_label = toga.Label("Enter the value of Y", style=Pack(text_align=RIGHT))
    z_label = toga.Label("Enter the value of Z", style=Pack(text_align=RIGHT))
    Roll_label = toga.Label("Enter the value of Roll (in Angles)", style=Pack(text_align=RIGHT))
    Pitch_label = toga.Label("Enter the value of Pitch (in Angles)", style=Pack(text_align=RIGHT))
    Yaw_label = toga.Label("Enter the value of Yaw (in Angles)", style=Pack(text_align=RIGHT))

   ##def ikin_connection(widget):
   ##     try:
   ##         c_input.value = (float(f_input.value) - 32.0) * 5.0 / 9.0
   ##     except ValueError:
   ##         c_input.value = "???"

    
    
    ##button1 = toga.Button("Calculate Ikin", on_press=calculate)

    button1 = toga.Button("Connect to PLC", style=Pack(width=100,padding_left=45))
    button2 = toga.Button("Calculate Ikin", style=Pack(alignment= "right", padding_left = 20))
    button3 = toga.Button("Power",style=Pack(padding_left= 40))
    button4 = toga.Button("Halt",style=Pack(padding_left= 40))
    button5 = toga.Button("Stop",style=Pack(padding_left= 40))
    button6 = toga.Button("Reset")


    ams_netid.add(amsnetid_label)
    ams_netid.add(ams_netid_input)
    ams_netid.add(button1)
    
    # x.add(amsnetid_label)
    x.add(x_label)
    x.add(x_input)
    x.add(button2)
    
    # y.add(button1)
    y.add(y_label)
    y.add(y_input)
    y.add(button3)
    y.add(button6)

    z.add(z_label)
    z.add(z_input) 
    z.add(button4)

    Roll.add(Roll_label)
    Roll.add(Roll_input)
    Roll.add(button5)

    Pitch.add(Pitch_label)
    Pitch.add(Pitch_input)
    
    Yaw.add(Yaw_label)
    Yaw.add(Yaw_input)
    
    box.add(ams_netid)
    box.add(x)
    box.add(y)
    box.add(z)
    box.add(Roll)
    box.add(Pitch)
    box.add(Yaw)
    # box.add(button1)
    # box.add(button2)
    # box.add(button3)
    # box.add(button4)
    # box.add(button5)
    # box.add(button6)

    box.style.update(direction=COLUMN, padding=10)
    # ams_netid.style.update(direction=ROW, padding=5)
    x.style.update(direction=ROW, padding=5)
    y.style.update(direction=ROW, padding=5)
    z.style.update(direction=ROW, padding=5)
    Roll.style.update(direction=ROW, padding=5)
    Pitch.style.update(direction=ROW, padding=5)
    Yaw.style.update(direction=ROW, padding=5)


    # x.style.update(flex=1)
    # y.style.update(flex=1, padding_left=160)
    # x_label.style.update(width=100, padding_left=10)
    # y_label.style.update(width=100, padding_left=10)

    # button1.style.update(padding=15)

    return box


def main():
    return toga.App("Controller", "org.beeware.Controller", startup=build)


if __name__ == "__main__":
    main().main_loop()