import serial                                                              #Serial imported for Serial communication
import time                                                                #delay 
ArduinoUnoSerial = serial.Serial('com3',9600)       #Create Serial port object called ArduinoUnoSerialData time.sleep(2)                                                             #wait for 2 secounds for the communication to get established
print (ArduinoUnoSerial.readline())           #read the serial data and print it as line ("Arduino connected")
print ("Press 1 to turn on LED. Press 0 to turn off LED. Press \"e\" to exit.")
looping = True
while looping:         #Do this until "e" is pressed
    var = input()                                          #get input from user             
    if (var == '1'):                                                #if the value is 1         
        ArduinoUnoSerial.write(str.encode('1'))                      #send 1 to the arduino's Data code       
        print ("LED turned ON")         
        time.sleep(1)
    if (var == '0'): #if the value is 0         
        ArduinoUnoSerial.write(str.encode('0'))            #send 0 to the arduino's Data code
        print ("LED turned OFF")         
        time.sleep(1)
    if (var == "e"):
        looping = False
        print("Goodbye!")
