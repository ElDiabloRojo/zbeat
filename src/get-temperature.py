#!/usr/bin/env python

import time
import datetime
from max30105 import MAX30105

max30105 = MAX30105()
max30105.setup(leds_enable=0)

delay = 10

print("Starting readings in {} seconds...\n".format(delay))
time.sleep(delay)

try:
    while True:
        temp = max30105.get_temperature()
        print("{:.2f}\n".format(temp))
        time.sleep(1.0)

except KeyboardInterrupt:
    pass