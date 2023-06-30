"""
This application can used to control the 6-RSS parallel platform motion connected with Beckhoff controller.
"""
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW
import pyads
import numpy as np
import threading

def Rx(theta):
    rotx = np.array([
                    [1, 0, 0],
                    [0, np.cos(theta), -np.sin(theta)],
                    [0, np.sin(theta), np.cos(theta)]
                ])
    return rotx

def Ry(theta):    
    roty = np.array([
                    [np.cos(theta), 0, np.sin(theta)],
                    [0, 1, 0],
                    [-np.sin(theta), 0, np.cos(theta)]
                ])   
    return roty
    
def Rz(theta):    
    rotz = np.array([
                    [np.cos(theta), -np.sin(theta), 0],
                    [np.sin(theta), np.cos(theta), 0],
                    [0, 0, 1]
                ])   
    return rotz

def create(r_B, r_P, gamma_B, gamma_P, thi):
    ## Base platform
    b1 = np.zeros((3,1))
    b1[1] = -r_B*np.cos(gamma_B)
    b1[2] = -r_B*np.sin(gamma_B)
    b2 = Rx(-2*gamma_B) @ b1
    b3 = Rx(-2*np.pi/3) @ b1
    b4 = Rx(-2*np.pi/3) @ b2
    b5 = Rx(-2*np.pi/3) @ b3
    b6 = Rx(-2*np.pi/3) @ b4
    b = np.hstack((b1,b2,b3,b4,b5,b6))

    ## Top platform
    R=Rx(thi[5]) @ Ry(thi[4]) @ Rz(thi[3])
    T=np.vstack((np.hstack((R, thi[0:3].reshape(3,1))),np.array([0,0,0,1])))
    t1 = np.zeros((3,1))
    t1[1] = -r_P*np.cos(gamma_P)
    t1[2] = -r_P*np.sin(gamma_P)
    t2=Rx(-2*gamma_P) @ t1
    t3=Rx(-2*np.pi/3) @ t1
    t4=Rx(-2*np.pi/3) @ t2
    t5=Rx(-2*np.pi/3) @ t3
    t6=Rx(-2*np.pi/3) @ t4
    t1=T @ np.vstack((t1,1))
    t2=T @ np.vstack((t2,1))
    t3=T @ np.vstack((t3,1))
    t4=T @ np.vstack((t4,1))
    t5=T @ np.vstack((t5,1))
    t6=T @ np.vstack((t6,1))
    t = np.hstack((t1,t2,t3,t4,t5,t6))[0:3,]

    return b, t

def calcTheta(b, t, a1, a2, gamma):

    theta = np.zeros((6))

    for i in range(6):
        R_2_SM = Rx(-gamma[i]) @ (t[:,i]-b[:,i])
        theta_i_3 = -np.arcsin(R_2_SM[2]/a2)
        # print('theta_3: ', np.degrees(theta_i_3))

        a2_dash = a2*np.cos(theta_i_3)
        theta_i_2 = -np.arccos((R_2_SM[0]**2 + R_2_SM[1]**2 - a1**2 - a2_dash**2)/(2*a1*a2_dash))
        # print('theta_2: ', np.degrees(theta_i_2))

        Ax = a1 + a2_dash*np.cos(theta_i_2)
        # print('Ax: ', Ax)
        Ay = a2_dash*np.sin(theta_i_2)
        # print('Ay: ', Ay)
        A = np.sqrt(Ax**2 + Ay**2)
        # print('A: ', A)
        psi = np.arctan2(Ay, Ax)
        # print('psi: ', psi)
        # print('yi: ', y[i])
        theta_i_1 = np.pi/2 - np.arccos(R_2_SM[1]/A)-psi
        # print('theta_1: ', np.degrees(theta_i_1))

        theta[i] = theta_i_1

    return theta

def iKine(thi=[0.7064,0,0,0,0,0]):
    thi=np.array(thi)
    r_B = 0.52280841
    gamma_B = np.deg2rad(34.62433818)
    r_P = 0.46509452
    gamma_P = np.deg2rad(55.06623734)
    gamma = np.deg2rad([150, -150, 30, 90, -90, -30])
    a1 = 0.120
    a2 = 0.850
    b, t= create(r_B, r_P, gamma_B, gamma_P, thi)
    theta = calcTheta(b, t, a1, a2, gamma)
    return np.rad2deg(theta)

X,Y,Z,Roll,Pitch,Yaw= 0.7064,0,0,0,0,0
dpos=0.001
theta=iKine([X,Y,Z,Roll,Pitch,Yaw])
plc=0

class _6RSSController(toga.App):

    def sendPos(self):
        # print(X)
        # print(Y)
        # print(Z)
        # print(Roll)
        # print(Pitch)
        # print(Yaw)
        rPos=['GVL.rPos1','GVL.rPos2','GVL.rPos3','GVL.rPos4','GVL.rPos5','GVL.rPos6']
        rVelo=['GVL.rVelo1','GVL.rVelo2','GVL.rVelo3','GVL.rVelo4','GVL.rVelo5','GVL.rVelo6']
        global theta
        pre_theta=theta
        theta=iKine([X,Y,Z,Roll,Pitch,Yaw])
        print(theta)
        try:
            if np.all(np.isnan(theta)) == False:
                if np.all(np.isnan(pre_theta)) == True:
                    dtheta=np.zeros((6))
                else:
                    dtheta=10*np.abs(theta-pre_theta)
                rVeloDict=dict(zip(rVelo,dtheta.tolist()))
                plc.write_list_by_name(rVeloDict)
                rPosDict=dict(zip(rPos,theta.tolist()))
                plc.write_list_by_name(rPosDict)
            else:
                print('Invalid Values !!!!')
        except:
            print('Invalid Values !!!!')

    def connectPLC(self, widget):
        try:
            # print('connectPLC')
            global plc
            plc = pyads.Connection(self.ams_netid_input.value, int(self.port_input.value))
            # Open the connection
            plc.open()
            print('PLC Connected....')
            # # To check if the connection is correct
            # print('Current connection status (PLC ON ?): ', plc.is_open)
            # print('Current Status: ', plc.read_state())
            # print('PLC device info: ', plc.read_device_info())  # The result should be something like - ('Plc30 App', <pyads.structs.AdsVersion at 0x54a2c50>)
            # bEnPower = plc.get_symbol('GVL.bEnPower', auto_update=True)
            # bEnHalt = plc.get_symbol('GVL.bEnHalt', auto_update=True)
            # bEnStop = plc.get_symbol('GVL.bEnStop', auto_update=True)
            # bUpdEn = plc.get_symbol('GVL.bUpdEn', auto_update=True)
            # bEnReset = plc.get_symbol('GVL.bEnReset', auto_update=True)
        except:
            print('Connection not established !!')

    def pX(self,widget):
        def increase():
            pX_pressed=True
            while pX_pressed:
                global X
                X = X + dpos
                self.sendPos()
                pX_pressed=False
        threading.Thread(target=increase).start()
    
    def nX(self,widget):
        global X
        X = X - dpos
        self.sendPos()

    def pY(self,widget):
        global Y
        Y = Y + dpos
        self.sendPos()

    def nY(self,widget):
        global Y
        Y = Y - dpos
        self.sendPos()

    def pZ(self,widget):
        global Z
        Z = Z + dpos
        self.sendPos()    

    def nZ(self,widget):
        global Z
        Z = Z - dpos
        self.sendPos()

    def pRoll(self,widget):
        global Roll
        Roll = Roll + dpos
        self.sendPos()

    def nRoll(self,widget):
        global Roll
        Roll = Roll - dpos
        self.sendPos()

    def pPitch(self,widget):
        global Pitch
        Pitch = Pitch + dpos
        self.sendPos()

    def nPitch(self,widget):
        global Pitch
        Pitch = Pitch - dpos
        self.sendPos()

    def pYaw(self,widget):
        global Yaw
        Yaw = Yaw + dpos
        self.sendPos()

    def nYaw(self,widget):
        global Yaw
        Yaw = Yaw - dpos
        self.sendPos()

    def power(self,widget):
        global plc
        plc.write_by_name('GVL.btnPower', True)
        # plc.write_by_name('GVL.bEnPower', True)
        plc.write_by_name('GVL.bUpdEn', True)

    def halt(self,widget):
        global plc
        plc.write_by_name('GVL.bEnHalt', True)

    def stop(self,widget):
        global plc
        plc.write_by_name('GVL.bEnStop', True)

    def reset(self,widget):
        global plc
        plc.write_by_name('GVL.bEnReset', True)
        
    def disconnect(self,widget):
        global plc, X, Y, Z, Roll, Pitch, Yaw
        X,Y,Z,Roll,Pitch,Yaw= 0.7064,0,0,0,0,0
        self.sendPos()
        plc.close()
        print('PLC Disconnected')

    def startup(self):
        """9
        Construct and show the Toga application.

        Usually, you would add your application to a main content box.
        We then create a main window (with a name matching the app), and
        show the main window.
        """
        main_box = toga.Box(style=Pack(direction=COLUMN, flex=1))

        ## AMS box
        amsnetid_label = toga.Label("AMS Net ID", style=Pack( width=250, font_size = 20, font_family= ("serif")))
        self.ams_netid_input = toga.TextInput(style=Pack(font_size = 20, padding_left = 20, width = 250), placeholder='AMS Net ID')
        self.port_input = toga.TextInput(style=Pack(font_size = 20, padding_left = 20, width = 80), placeholder='Port')
        connectPLC_button = toga.Button("Connect to PLC", on_press = self.connectPLC, style=Pack(width=250,padding_left=40 ,  font_size = 20, font_family= ("serif"), background_color = ("#acc5fa")))
        ams_box = toga.Box(children=[amsnetid_label,self.ams_netid_input,self.port_input,connectPLC_button],style=Pack(direction=ROW, padding=5))

        ## Control box
        # Translation box
        transalation_label = toga.Label("Translations", style=Pack(width=250, padding_left = 10, font_size = 20, font_family= ("serif")))

        self.pX_button = toga.Button("+X", on_press = self.pX , style=Pack( width = 60, font_size = 20, font_family= ("serif")))
        self.nX_button = toga.Button("-X", on_press = self.nX , style=Pack( width = 60, padding_left = 30, font_size = 20, font_family= ("serif")))
        x_box = toga.Box(children=[self.pX_button, self.nX_button], style=Pack(direction = ROW , padding = 5))

        self.py_button= toga.Button("+Y" , on_press = self.pY, style=Pack( width = 60, font_size = 20, font_family= ("serif")))
        self.ny_button = toga.Button("-Y", on_press = self.nY, style=Pack(  width = 60,padding_left = 30, font_size = 20, font_family= ("serif")))
        y_box = toga.Box(children= [self.py_button, self.ny_button],style=Pack(direction = ROW , padding = 5))

        self.pz_button = toga.Button("+Z", on_press = self.pZ, style=Pack(  width = 60,font_size = 20, font_family= ("serif")))
        self.nz_button = toga.Button("-Z", on_press = self.nZ, style=Pack(  width = 60, padding_left = 30, font_size = 20, font_family= ("serif")))
        z_box = toga.Box(children=[self.pz_button,self.nz_button], style=Pack(direction = ROW , padding = 5))

        translation_control_box=toga.Box(children=[transalation_label, x_box, y_box, z_box],style=Pack(direction = COLUMN , padding = 5))
        
        # Rotation box
        rotation_label = toga.Label("Rotations",  style=Pack(width=250, padding_left = 90, font_size = 20, font_family= ("serif")))

        self.pRoll_button = toga.Button("+Roll", on_press= self.pRoll, style=Pack(padding_left= 50 ,  font_size = 20, font_family= ("serif"), width = 95))
        self.nRoll_button = toga.Button("-Roll" , on_press=self.nRoll, style=Pack(  padding_left = 15, font_size = 20, font_family= ("serif") , width = 95))
        Roll_box = toga.Box(children = [self.pRoll_button, self.nRoll_button], style=Pack(direction = ROW , padding = 5))

        self.pPitch_button = toga.Button("+Pitch" , on_press=self.pPitch, style=Pack(padding_left=50 ,  font_size = 20, font_family= ("serif") , width = 95))
        self.nPitch_button = toga.Button("-Pitch" , on_press=self.nPitch, style=Pack(padding_left = 15, font_size = 20, font_family= ("serif") , width = 95))
        Pitch_box = toga.Box(children=[self.pPitch_button, self.nPitch_button], style=Pack(direction = ROW , padding = 5))

        self.pYaw_button = toga.Button("+Yaw" , on_press=self.pYaw, style=Pack(padding_left= 50,  font_size = 20, font_family= ("serif") , width = 95))
        self.nYaw_button = toga.Button("-Yaw" , on_press=self.nYaw, style=Pack( padding_left = 15, font_size = 20, font_family= ("serif") , width = 95))
        Yaw_box = toga.Box(children = [self.pYaw_button,self.nYaw_button], style=Pack(direction = ROW , padding = 5))

        rotation_control_box=toga.Box(children=[rotation_label, Roll_box, Pitch_box, Yaw_box],style=Pack(direction = COLUMN , padding = 5))

        # Motion control box
        self.power_button = toga.Button("Power", on_press=self.power, style=Pack(width = 150 , padding_left= 100, background_color="#13f20f" ,  font_size = 20, font_family= ("serif")))
        self.halt_button = toga.Button("Halt",  on_press=self.halt, style=Pack(width = 150 , padding_left= 100 ,  font_size = 20, font_family= ("serif"), background_color =("#eddf15")))
        self.stop_button = toga.Button("Stop",on_press=self.stop, style=Pack(width = 150 , padding_left= 100 ,  font_size = 20, font_family= ("serif"), background_color =("#f23224")))
        self.reset_button = toga.Button("Reset", on_press=self.reset, style=Pack(width = 150 , padding_left= 100 ,  font_size = 20, font_family= ("serif"), background_color = ("#f2800f")))
        self.disconnect_button = toga.Button("Disconnect",on_press= self.disconnect, style=Pack(width = 150 , padding_left = 100 , font_size = 20, font_family= ("serif")))

        motion_control_box = toga.Box(children = [self.power_button,self.halt_button,self.stop_button,self.reset_button, self.disconnect_button],style=Pack(direction = COLUMN , padding = 5))
        control_box=toga.Box(children=[translation_control_box, rotation_control_box,motion_control_box], style=Pack(direction = ROW , padding = 5))
    
        main_box.add(ams_box)
        main_box.add(control_box)
        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()


def main():
    return _6RSSController()
