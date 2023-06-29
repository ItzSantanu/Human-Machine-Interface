import toga
from toga.style.pack import COLUMN, LEFT, RIGHT, ROW, Pack, Font


def build(app):
    
    #Defining the Boxes
    
    ams_netid = toga.Box(style=Pack(direction=ROW, padding=5))
    port = toga.Box(style= Pack(direction=ROW, padding = 5))
    x = toga.Box()
    y = toga.Box()
    z = toga.Box()
    Roll = toga.Box()
    Pitch = toga.Box()
    Yaw = toga.Box()
    box = toga.Box(style=Pack(background_color = ("#FFFFFF")))

    #Defining the Input

    ams_netid_input = toga.TextInput(style=Pack(font_size = 20, padding_left = 140, width = 200))
    port_input = toga.TextInput(style=Pack(font_size = 20, padding_left = 140, width = 200))
    x_input = toga.TextInput(style=Pack(padding_left = 90 , font_size = 20 , width =200))
    y_input = toga.TextInput(style=Pack(padding_left = 90, font_size = 20 , width =200))
    z_input = toga.TextInput(style=Pack(padding_left = 140 , font_size = 20, width = 200))
    Roll_input = toga.TextInput(style=Pack(padding_left = 40 , font_size = 20 , width = 200))
    Pitch_input = toga.TextInput(style=Pack(padding_left = 40 ,font_size = 20 , width = 200))
    Yaw_input = toga.TextInput(style=Pack(padding_left = 40, padding_top = 10 , width = 200, font_size = 20))

    #Defining the Labels

    amsnetid_label = toga.Label("AMS_NET_ID", style=Pack( width=250, font_size = 20, font_family= ("serif") , background_color = ("#FFFFFF")))
    port_label = toga.Label("Enter Port number", style=Pack(width=250, padding_left = 0, font_size = 20, font_family= ("serif"),  background_color = ("#FFFFFF")))
    x_label = toga.Label("Enter the value of X", style=Pack( width =300 , font_size = 20, font_family= ("serif"),  background_color = ("#FFFFFF") ))
    y_label = toga.Label("Enter the value of Y", style=Pack(  width =300 , font_size = 20, font_family= ("serif"),   background_color = ("#FFFFFF")))
    z_label = toga.Label("Enter the value of Z", style=Pack( width = 250 , font_size = 20, font_family= ("serif"),  background_color = ("#FFFFFF")))
    Roll_label = toga.Label("Enter the value of Roll", style=Pack( width = 350 , font_size = 20, font_family= ("serif"),  background_color = ("#FFFFFF") ))
    Pitch_label = toga.Label("Enter the value of Pitch", style=Pack( width = 350 , font_size = 20 , font_family= ("serif"),  background_color = ("#FFFFFF")))
    Yaw_label = toga.Label("Enter the value of Yaw", style=Pack(padding_top= 10 , width =350, font_size = 20, font_family= ("serif"),  background_color = ("#FFFFFF")))

    #Defining the Buttons

    button1 = toga.Button("Connect to PLC", style=Pack(width=250,padding_left=40 ,  font_size = 20, font_family= ("serif"), background_color = ("#acc5fa")))
    button2 = toga.Button("Calculate Ikin", style=Pack(alignment= "right", padding_left = 40 ,  font_size = 20, font_family= ("serif")))
    button3 = toga.Button("Power",style=Pack(padding_left= 40, background_color="#13f20f" ,  font_size = 20, font_family= ("serif")))
    button4 = toga.Button("Halt",style=Pack(padding_left= 40 ,  font_size = 20, font_family= ("serif"), background_color =("#f2ae0f")))
    button5 = toga.Button("Stop",style=Pack(padding_left= 40 ,  font_size = 20, font_family= ("serif"), background_color =("#f23224")))
    button6 = toga.Button("Reset", style=Pack(padding_left= 20 ,  font_size = 20, font_family= ("serif"), background_color = ("#f2800f")))
    button7 = toga.Button("Port", style=Pack(padding_left=40 ,  font_size = 20, font_family= ("serif"), background_color = ("#FFFFFF")))

    #arranging the childrens
    
    ams_netid.add(amsnetid_label)
    ams_netid.add(ams_netid_input)
    ams_netid.add(button1)
    port.add(port_label)
    port.add(port_input)
    port.add(button7)
    
    
    x.add(x_label)
    x.add(x_input)
    x.add(button2)
    
    
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
    box.add(port)
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
