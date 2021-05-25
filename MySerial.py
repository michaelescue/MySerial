#   MySerial.py
#   File for connecting seriallly

import serial

class MySerial:

    def __init__(self):

        self.ser = None

        while self.ser is not None:

            try:
                self.ser = MySerial(input("Serial Port: "))
            except Exception as e:
                print("MySerial: ", e)
                continue

        return self.ser
