'''
From The Picamera2 Library pdf, pg. 8, Chapter 2
There is NO on screen preview. It just records!!
this is just a smoke test - go/no-go - look for
other video programs to explore this more
'''
from picamera2 import Picamera2

picam2 = Picamera2()
picam2.start_and_record_video("test.mp4", duration=3)
#picam2.start_and_capture_file("test.jpg") # take a jpg, not an mp4