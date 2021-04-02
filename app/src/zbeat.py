#!/usr/bin/env python

import prometheus_client
import time
from max30105 import MAX30105, HeartRate

max30105 = MAX30105()
max30105.setup(leds_enable=2)

max30105.set_led_pulse_amplitude(1, 0.2)
max30105.set_led_pulse_amplitude(2, 12.5)
max30105.set_led_pulse_amplitude(3, 0)

max30105.set_slot_mode(1, 'red')
max30105.set_slot_mode(2, 'ir')
max30105.set_slot_mode(3, 'off')
max30105.set_slot_mode(4, 'off')

UPDATE_PERIOD = 300

hr = HeartRate(max30105)
heart_rate = prometheus_client.Gauge('heart_rate_bpm',
                              'Depth of water in water tank. Full = 2.7m',
                              ['location'])

def publish_heartrate(beat, bpm, avg_bpm):
    heart_rate.labels('beat').set(beat)
    heart_rate.labels('bpm').set(bpm)
    heart_rate.labels('avg_bpm').set(avg_bpm)

if __name__ == '__main__':
  prometheus_client.start_http_server(9999)
  
while True:
  hr.on_beat(publish_heartrate, average_over=4)
  time.sleep(UPDATE_PERIOD)