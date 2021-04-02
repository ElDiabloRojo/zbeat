#!/usr/bin/env python

import prometheus_client
import time

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