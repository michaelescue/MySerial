#   main.py
#   Used to interface with Gt-U7
#   Michael Escue
#   May 25 2021

import MySerial

ser = MySerial()

while True:

    print(ser.read(256))

