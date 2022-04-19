#imports
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QLabel
import sys
import time
from api import order_temp_update, delete_order_number
from bacode import *
from hardware import *


class Window(QMainWindow):
    def __init__(self):
       super().__init__()
       self.setGeometry(300, 300, 600, 400)
       self.setWindowTitle("Pizza Locker GUI")
       self.UiButtons()
    #    self.labels()
       self.show()

    #method to setup initial buttons
    def UiButtons(self):
        self.start_btn = QPushButton("Start", self)
        self.start_btn.move(250,150)
        self.start_btn.pressed.connect(self.start_app)
        self.text_label = QLabel(self)
        self.text_label.setGeometry(220,0,300,50)
        # self.employee_btn = QPushButton("Employe", self)
        # self.employee_btn.move(250,200)
        # self.employee_btn.pressed.connect(self.employee_pushed)   

    #method to create intial label
    # def labels(self):
    #     self.user_employee_label = QLabel(self)
    #     self.user_employee_label.setGeometry(220,0, 300, 50)
    #     self.user_employee_label.setText("Please select your perference")

    #method executed on button push
    # def user_pushed(self):
    #     print("User pushed")

    #     #removing buttons to prepare for next screen
    #     self.user_btn.deleteLater()
    #     self.employee_btn.deleteLater()
    #     self.user_employee_label.clear()

    #     #setting up new window
    #     print("setting up new window")
    #     self.scan_label = QLabel(self) 
    #     self.scan_label.setGeometry(500, 0, 300, 50)
    #     self.scan_label.setText("Please scan your barcode")
    #     self.q_btn = QPushButton("Quit", self)
    #     self.q_btn.setStyleSheet("background-color: red")
    #     self.q_btn.clicked.connect(self.close)

    #     #fake barcode reading and new label
    #     display_string = read_barcode()
    #     self.result_label = QLabel(self)
    #     self.result_label.setGeometry(220,100,300,50)
    #     self.result_label.setText(display_string)
        
    #     print("setup finished")

    #method executed on button push
    # def employee_pushed(self):
    #     print("Employee pushed")

    #     #removing buttons to prepare for next screen
    #     self.employee_btn.deleteLater()
    #     self.user_btn.deleteLater()
    #     self.user_employee_label.clear()    

    #start application method
    def start_app(self):
        self.start_btn.deleteLater()
        self.show()
        self.scan()
        # time.sleep(2)
        # while 1:
        #     print("GUI fake work")   
        #     time.sleep(5)
    
    def scan(self):
        print("start scanning")
        barcode = read_barcode()
        split_barcode = barcode.split("$")

        if split_barcode[0] == store_barcode:
            #barcode read was store barcode so now read for user barcode
            user_barcode = split_barcode[1]
            locker = get_free_locker()
            if locker == -1:
                print("No locker available")
            else:
                #unlock locker
                self.text_label.setText("Employee, place order in locker {}".format(locker))
                unlock_locker(locker)
                time.sleep(5)
                lock_locker(locker)

                #send API call now
                (temp, humidty) = checkTemp(locker)
                order_number = user_barcode #might need to change this to just part of what was read
                order_temp_update(order_number, temp, locker)
                self.text_label.setText("User has been notified that their order is ready for pickup")
                
                #update dictionaries
                locker_to_order_number[str(locker)] = order_number

        else :
            #read user barcode
            print("dealing with user barcode")
            locker_number = get_locker_number(order_number)
            if (locker_number == -1):
                print("order not found")
            else:
                print("found order")

            #notify user where their order is placed and unlock
            self.text_label.setText("User, locker {} has been unlocked. Please close after retreiving order".format(locker_number))
            unlock_locker(locker_number)
            time.sleep(5)
            lock_locker(locker_number)
            delete_order_number(barcode)

        time.sleep(5)
        self.text_label.clear()    
        self.scan()


#read barcode function
def read_fake_barcode():
    return "fake barcode"


def setup_initial_gui():
    app = QApplication(sys.argv)
    window = Window()
    app.exec_() 


