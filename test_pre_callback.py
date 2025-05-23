# copied from The Picamera2 Library, page 60
# NEC added a lot to explore main and lores streams
from picamera2 import Picamera2, MappedArray, Preview
import cv2
import time

picam2 = Picamera2()

font_colour = (0, 255, 0)
origin = (10, 30)
font = cv2.FONT_HERSHEY_SIMPLEX
scale = 1
thickness = 2

normalSize = (1920, 1080)
#normalSize = (640, 480)
lowresSize = (400, 300)

def apply_timestamp(request):
    timestamp = time.strftime("%Y-%m-%d %X")
    with MappedArray(request, "main") as m:
        cv2.putText(m.array, timestamp, origin, font, scale, font_colour, thickness)

picam2.pre_callback = apply_timestamp

config = picam2.create_preview_configuration(main={"size": normalSize},
                                             lores={"size": lowresSize, "format": "YUV420"},display="main")
picam2.configure(config)

#x&y set location of preview, normalsize sets image size in preview window, width&height set preview window size
picam2.start_preview(Preview.QTGL, x=400, y=100, width=1920, height=1080)
#picam2.start_preview(Preview.QTGL, x=400, y=400) #preview window seems happier without width & height setting
picam2.start(show_preview=True)
time.sleep(5)
