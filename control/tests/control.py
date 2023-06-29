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

    ams_netid_input = toga.TextInput(style=Pack(font_size = 20, padding_left = 20, width = 250))
    port_input = toga.TextInput(style=Pack(font_size = 20, padding_left = 20, width = 80))

    #Defining the Labels

    amsnetid_label = toga.Label("AMS Net ID", style=Pack( width=250, font_size = 20, font_family= ("serif") , background_color = ("#FFFFFF")))
    transalation_label = toga.Label("Translations", style=Pack(width=250, padding_left = 0, font_size = 20, font_family= ("serif"),  background_color = ("#FFFFFF")))
    rotation_label = toga.Label("Rotations",  style=Pack(width=250, padding_left = 90, font_size = 20, font_family= ("serif"),  background_color = ("#FFFFFF")))

    #Defining the Buttons

    connectPLC_button = toga.Button("Connect to PLC", style=Pack(width=250,padding_left=40 ,  font_size = 20, font_family= ("serif"), background_color = ("#acc5fa")))


    power_button = toga.Button("Power",style=Pack(padding_left= 120, background_color="#13f20f" ,  font_size = 20, font_family= ("serif")))
    halt_button = toga.Button("Halt",style=Pack(padding_left= 120 ,  font_size = 20, font_family= ("serif"), background_color =("#f2ae0f")))
    stop_button = toga.Button("Stop",style=Pack(padding_left= 120 ,  font_size = 20, font_family= ("serif"), background_color =("#f23224")))
    reset_button = toga.Button("Reset", style=Pack(padding_left= 20 ,  font_size = 20, font_family= ("serif"), background_color = ("#f2800f")))


    pX_button = toga.Button("+X" , style=Pack( width = 60, font_size = 20, font_family= ("serif")))
    nX_button = toga.Button("-X" , style=Pack( width = 60, padding_left = 30, font_size = 20, font_family= ("serif")))
    py_button= toga.Button("+Y" , style=Pack( width = 60, font_size = 20, font_family= ("serif")))
    ny_button = toga.Button("-Y", style=Pack(  width = 60,padding_left = 30, font_size = 20, font_family= ("serif")))
    pz_button = toga.Button("+Z", style=Pack(  width = 60,font_size = 20, font_family= ("serif")))
    nz_button = toga.Button("-Z", style=Pack(  width = 60, padding_left = 30, font_size = 20, font_family= ("serif")))


    pRoll_button = toga.Button("+Roll", style=Pack(padding_left= 150 ,  font_size = 20, font_family= ("serif"), width = 95))
    nRoll_button = toga.Button("-Roll" , style=Pack(  padding_left = 15, font_size = 20, font_family= ("serif") , width = 95))
    pPitch_button = toga.Button("+Pitch" , style=Pack(padding_left=150 ,  font_size = 20, font_family= ("serif") , width = 95))
    nPitch_button = toga.Button("-Pitch" , style=Pack(padding_left = 15, font_size = 20, font_family= ("serif") , width = 95))
    pYaw_button = toga.Button("+Yaw" , style=Pack(padding_left= 150,  font_size = 20, font_family= ("serif") , width = 95))
    nYaw_button = toga.Button("-Yaw" , style=Pack( padding_left = 15, font_size = 20, font_family= ("serif") , width = 95))

    #Defining the level of childrens

    ams_netid.add(amsnetid_label)
    ams_netid.add(ams_netid_input)
    ams_netid.add(port_input)
    ams_netid.add(connectPLC_button)

    x.add(transalation_label)
    x.add(rotation_label)

    y.add(pX_button)
    y.add(nX_button)
    y.add(pRoll_button)
    y.add(nRoll_button )
    y.add(power_button)
    y.add(reset_button)

    z.add(py_button)
    z.add(ny_button)
    z.add(pPitch_button)
    z.add(nPitch_button)
    z.add(halt_button)

    Roll.add(pz_button)
    Roll.add(nz_button)
    Roll.add(pYaw_button)
    Roll.add(nYaw_button)
    Roll.add(stop_button)
    
    box.add(ams_netid)
    box.add(port)
    box.add(x)
    box.add(y)
    box.add(z)
    box.add(Roll)
    box.add(Pitch)
    box.add(Yaw)

    box.style.update(direction=COLUMN, padding=10)
    x.style.update(direction=ROW, padding=5)
    y.style.update(direction=ROW, padding=5)
    z.style.update(direction=ROW, padding=5)
    Roll.style.update(direction=ROW, padding=5)
    Pitch.style.update(direction=ROW, padding=5)
    Yaw.style.update(direction=ROW, padding=5)

    return box

def main():
    return toga.App("Controller", "org.beeware.Controller", startup=build)


if __name__ == "__main__":
    main().main_loop()
