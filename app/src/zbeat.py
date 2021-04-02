#!/usr/bin/env python

import prometheus_client
import time
from max30105 import MAX30105, HeartRate

# Max30105 Setup

max30105 = MAX30105()
max30105.setup(leds_enable=2)

max30105.set_led_pulse_amplitude(1, 0.2)
max30105.set_led_pulse_amplitude(2, 12.5)
max30105.set_led_pulse_amplitude(3, 0)

max30105.set_slot_mode(1, 'red')
max30105.set_slot_mode(2, 'ir')
max30105.set_slot_mode(3, 'off')
max30105.set_slot_mode(4, 'off')

hr = HeartRate(max30105)

# Metric Declarations

heart_rate = prometheus_client.Gauge('heart_rate_bpm',
                                     'Current heart rate bpm.',
                                     ['bpm'])
beat_detected = prometheus_client.Gauge('beat_detected',
                                     'Heart beat detected.',
                                     ['beat'])
temperature = prometheus_client.Gauge('temperature',
                                     'Curent temperature.',
                                     ['temp'])


def publish_heartrate(beat, bpm, avg_bpm):
    beat_detected.labels('beat').set(beat)
    heart_rate.labels('bpm').set(bpm)
    heart_rate.labels('avg_bpm').set(avg_bpm)

if __name__ == '__main__':
    prometheus_client.start_http_server(9999)

while True:
    hr.on_beat(publish_heartrate, average_over=4)
    temp = max30105.get_temperature()
    temperature.labels('temp').set(temp)
