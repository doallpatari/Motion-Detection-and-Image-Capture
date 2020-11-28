import serial
import time
import webcam as wc
import threading as th
import cv2

wc_obj = wc.web_c()

class reader:
    z1baudrate = 9600
    z1port = 'COM1'  

    z1serial = serial.Serial(port=z1port, baudrate=z1baudrate)
    z1serial.timeout = 1 
    print(z1serial.is_open)  
    if z1serial.is_open:
        while True:
            size = z1serial.inWaiting()
            if size:
                data = z1serial.read(size).decode('utf-8')
                print(data)
                if(data == "cam_start"):
                    wc_obj.start_wc()
                elif(data == "cam_stop"):
                    print("no_cam")
                    
            else:
                print ('no data')
            time.sleep(0.5)
    else:
        print ('z1serial not open')




