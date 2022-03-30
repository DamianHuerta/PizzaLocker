from gettext import translation
from traceback import print_tb
# from gui import *


#dictionaries
order_number_to_locker_and_gpio = {}
free_lockers =  {}
locker_to_gpio = {}
locker_to_order_number = {}


def barcode_translation(barcode):
    print("printing barcode: {}".format(barcode))
    locker_gpio = (1,2) #dummy numbers rn
    return locker_gpio 

def read_barcode():
    return "fakebarcode123"

def main():

    #setting up application and window
    # app = QApplication(sys.argv)
    # window = Window()
    
    #running app
    # app.exec_()

    #read barcode
    barcode = read_barcode()
    locker_to_gpio = barcode_translation(barcode)
    order_number_to_locker_and_gpio[barcode] = locker_to_gpio

    print("printing dictionary entry")
    print(order_number_to_locker_and_gpio[barcode])





if __name__ == "__main__":
    main()