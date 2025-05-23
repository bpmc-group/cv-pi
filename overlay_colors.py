# Copied from https://github.com/raspberrypi/picamera2/blob/main/examples/overlay_drm.py
# Very similar to First Example in Picamera2 Library Docs except that it creates an overlay
# of 4 color translucent squares. It does this by creating an np array and dividing it into
# quarters, with each quarter corresponding to a quarter of the screen. It then adds a
# value of 255 to just one of the three color 'channels' (RGB) to the 2nd - 4th quarter of 
# the screen. With the opacity set to 64, there is just a see-through rectangle of the 
# chosen color that shows on top of the preview window. If you change the opacity to 250
# or so, you get a solid block of color that hides everything behind it.
# NEC added the transform to the call to create_preview_configuration() just for laughs
import time

import numpy as np

from picamera2 import Picamera2, Preview
from libcamera import Transform

picam2 = Picamera2()
print("preview prep")
#original doesn't have the transform statement in  create_preview_config() below
picam2.configure(picam2.create_preview_configuration(transform = Transform(hflip=0, vflip=0)))
print("ready start preview")
picam2.start_preview(Preview.QTGL) #use Preview.DRM for non-GUI systems
#transform = Transform(vflip=1) ## this belongs in the create_preview_config() statement
picam2.start()
time.sleep(1)

print("overlay prep")
overlay = np.zeros((300, 400, 4), dtype=np.uint8)
overlay[:150, 200:] = (255, 0, 0, 64) #last number is opacity, 0 - 255, higher is more opaque
overlay[150:, :200] = (0, 255, 0, 64)
overlay[150:, 200:] = (0, 0, 255, 64)

picam2.set_overlay(overlay)
time.sleep(5)