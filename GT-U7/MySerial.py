#   MySerial.py
#   File for connecting seriallly

import serial

class MySerial:

    ser = None

    def __init__(self):

        while self.ser is not None:

            try:
                self.ser = MySerial(input("Serial Port: "))
            except Exception as e:
                print("MySerial: ", e)
                continue

        return self.ser
