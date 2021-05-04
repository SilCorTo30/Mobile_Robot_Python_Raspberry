#Autor Silverio Coronado Torres
#GitHub 'SilCorTo30'
from pyfirmata import Arduino #Librería para la comunicación
import time

Led = 13
arduino = Arduino("/dev/ttyUSB0") #puerto donde
                    #está conectado el arduino

for x in range (10):
    arduino.digital[Led].write(1)
    time.sleep(1)
    arduino.digital[Led].write(0)
    time.sleep(1)