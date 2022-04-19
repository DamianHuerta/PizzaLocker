#imports
import time
import board
import adafruit_sht
import RPi.GPIO

#dictionaries
locker_to_gpio = {1:16, 2:20, 3:21}
# order_number_to_locker_and_gpio = {}
locker_status =  {} #1 is available 0 is busy
# locker_to_gpio = {}
locker_to_order_number = {"1": "9008382555852004972"}


#initialize harware. Might not actually need this
def initialize_hardware(free_lockers):
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(16, GPIO.OUT)
    GPIO.setup(20, GPIO.OUT)
    GPIO.setup(21, GPIO.OUT)
    locker_status[1] = 1
    locker_status[2] = 1
    locker_status[3] = 1
    return

def unlock_locker(locker):
    GPIO.output(locker_to_gpio[locker], 1)

def lock_locker(locker):
    GPIO.output(locker_to_gpio[locker], 0)

def get_free_locker():
    for locker in locker_status:
        if locker_status[locker] == 1:
            locker_status[locker] = 0
            return locker
    return -1

def get_locker_number(order_number):
    for locker in locker_to_order_number:
        if locker_to_order_number[locker] == order_number:
            return locker
    return -1

def checkTemp(locker_number):
    dhtDevice = adafruit_dht.DHT22(board.D18)
    while True:
        try:
            temperature_c = dhtDevice.temperature
            temperature_f = temperature_c * (9/5) + 32
            humidity = dhtDevice.humidity
            print("Temp: {:.1f} F / {:.1f} C Humidity: {}% ".format(temperature_f, temperature_c, humidity))
            #dhtDevice.exit()
            tup = (temperature_f, humidity)
            return tup
        except RuntimeError as error:
            # Errors happen fairly often, DHT's are hard to read, just keep going
            #print(error.args[0])
            time.sleep(2.0)
            continue
        except Exception as error:
            dhtDevice.exit()
            raise error
