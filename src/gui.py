#imports
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QLabel
import sys


class Window(QMainWindow):
    def __init__(self):
       super().__init__()
       self.setGeometry(300, 300, 600, 400)
       self.setWindowTitle("Pizza Locker GUI")
       self.UiButtons()
       self.labels()
       self.show()

    #method to setup initial buttons
    def UiButtons(self):
        self.user_btn = QPushButton("User", self)
        self.user_btn.move(250,150)
        self.user_btn.pressed.connect(self.user_pushed)
        self.employee_btn = QPushButton("Employe", self)
        self.employee_btn.move(250,200)
        self.employee_btn.pressed.connect(self.employee_pushed)   

    #method to create intial label
    def labels(self):
        self.user_employee_label = QLabel(self)
        self.user_employee_label.setGeometry(220,0, 300, 50)
        self.user_employee_label.setText("Please select your perference")

    #method executed on button push
    def user_pushed(self):
        print("User pushed")

        #removing buttons to prepare for next screen
        self.user_btn.deleteLater()
        self.employee_btn.deleteLater()
        self.user_employee_label.clear()

        #setting up new window
        print("setting up new window")
        self.scan_label = QLabel(self) 
        self.scan_label.setGeometry(500, 0, 300, 50)
        self.scan_label.setText("Please scan your barcode")
        self.q_btn = QPushButton("Quit", self)
        self.q_btn.setStyleSheet("background-color: red")
        self.q_btn.clicked.connect(self.close)

        #fake barcode reading and new label
        display_string = read_barcode()
        self.result_label = QLabel(self)
        self.result_label.setGeometry(220,100,300,50)
        self.result_label.setText(display_string)
        
        print("setup finished")

    #method executed on button push
    def employee_pushed(self):
        print("Employee pushed")

        #removing buttons to prepare for next screen
        self.employee_btn.deleteLater()
        self.user_btn.deleteLater()
        self.user_employee_label.clear()       

#read barcode function
def read_barcode():
    return "fake barcode"