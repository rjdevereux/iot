# SPDX-FileCopyrightText: 2017 Limor Fried for Adafruit Industries
#
# SPDX-License-Identifier: MIT

import time

import adafruit_dht
import board

from datetime import datetime

dht = adafruit_dht.DHT22(board.D4)

now = datetime.utcnow()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
writefile = 0
output = ""
try:
    temperature = dht.temperature
    humidity = dht.humidity
    # Print what we got to the REPL
    output = "{}\tTemp:\t{:.1f} *C\tHumidity:\t{}%".format(dt_string, temperature, humidity)
    print(output)
    writefile = 1
except RuntimeError as e:
    # Reading doesn't always work! Just print error and we'll try again
    print("Reading from DHT failure: ", e.args)

dht.exit()

if writefile:
    try:
        dt_filename_string = now.strftime("%d-%m-%Y---%H-%M-%S.txt")
        file1 = open("/home/pi/logs/" + dt_filename_string, "w")
        file1.write(output + '\n')
        file1.close()
    except RuntimeError as e:
        print("Writing file didn't work: ", e.args)


