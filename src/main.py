from hardware import *
from locker_threads import* 

# from gui import *


#dictionaries
order_number_to_locker_and_gpio = {}
free_lockers =  {}
locker_to_gpio = {}
locker_to_order_number = {}




def locker_temp_check():
    print("checking locker temp")
    return




def main():

    

    #initialize hardware
    initialize_hardware(free_lockers)

    #launching GUI thread
    print("Launching GUI Thread")
    gui_thread = myThread(1, "GUI-Thread")
    gui_thread.start()



    #start periodically sending temp information to lockers that are open
    while 1:
        locker_temp_check()
        time.sleep(5)
    
    #waiting for gui thread to finish
    gui_thread.join()






if __name__ == "__main__":
    main()