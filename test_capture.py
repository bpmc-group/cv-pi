'''
from The Picamera2 Library pdf, pg 47, chap 6
initial delay: 1 s, then takes num_files(10) pictures delay(1) second apart
'''
from picamera2 import Picamera2

picam2 = Picamera2()
picam2.start_and_capture_files("runs/test{:d}.jpg", initial_delay=1, delay=1, num_files=10)