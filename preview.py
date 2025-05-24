'''
From The Picamera2 Library pdf, pgs. 10-11, Chap 3
'''
from picamera2 import Picamera2, Preview
from libcamera import Transform
import time

picam2 = Picamera2()
picam2.start_preview(Preview.QTGL) #simple format
# mess around with width & height settings to change size of preview window
#picam2.start_preview(Preview.QTGL, x=100, y=200, width=800, height=600, transform=Transform(vflip=1))
#picam2.start_preview(True) #autodetect mode for preview - see pg12
picam2.start()
time.sleep(2)