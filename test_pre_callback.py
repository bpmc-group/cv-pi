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

#normalSize = (2400, 1350)
normalSize = (1920, 1080)
#normalSize = (640, 480)
lowresSize = (320, 240)

def apply_timestamp(request):
    timestamp = time.strftime("%Y-%m-%d %X  ") + "Resolution = " + 'X'.join(str(x) for x in normalSize) 
    with MappedArray(request, "main") as m:
        cv2.putText(m.array, timestamp, origin, font, scale, font_colour, thickness) #Qt required for this

# I tried and failed to display the FPS - it would just hang when I tried to capture metadata before
#   the camera was running. I think the behavior of pre_callback is that apply_timestamp is RUN 
#   BEFORE the camera has started and that causes it to hang. Can I apply_timestamp as postcallback?
picam2.pre_callback = apply_timestamp
config = picam2.create_preview_configuration(main={"size": normalSize},
                                             lores={"size": lowresSize, "format": "YUV420"},display="main")
picam2.configure(config)

#x&y set location of preview, normalsize sets image size in preview window, width&height set preview window size
picam2.start_preview(Preview.QTGL, x=400, y=100, width=normalSize[0], height=normalSize[1])
#picam2.start_preview(Preview.QTGL, x=400, y=400) #preview window seems happier without width & height setting
picam2.start(show_preview=True)
metadata = picam2.capture_metadata() # this has to run AFTER camera has started
print(metadata)
time.sleep(5)
