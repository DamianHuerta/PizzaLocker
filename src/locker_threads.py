#regular imports
import time
import threading
# from bacode import read_barcode
from gui import *

#custom file imports
# from hardware import*
# from gui import *
from api import *
worker_start = False



class myThread (threading.Thread):
   def __init__(self, threadID, name):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
   def run(self):
      print ("Starting " + self.name)
      gui_thread()
      print ("Exiting " + self.name)

#gui thread. First will just prompt user to scan barcode
#continuously read barcode until we get an actual value
#determine if barcode read is user or employee
#make appropriate API calls to make this work
# GUI: when user scans barcode, make a prompt to tell them their
# locker number and give them an arbitrary time to grab order
# display time to user and then close lock after time
#when user/employee transaction is done just go back to screen
#that prompts user to scan their barcode
def gui_thread():
    print("Inside GUI thread")
   #  barcode = read_barcode()
   #  print("Barcode read: {}".format(barcode))
    i = 0

    setup_initial_gui()

    # while 1:
    #     time.sleep(5)
    #   #   setup_initial_gui()
    #     fake_barcode = read_fake_barcode()
    #     print("fake work done")



    #ANNIE DO UR SHIT HERE
    #setting up application and window: ANNIE DO THIS SHIT
   #  app = QApplication(sys.argv)
   #  window = Window()
    
   #  #running app
   #  window.show()
   #  app.exec_() 
    return



#gui_thread()