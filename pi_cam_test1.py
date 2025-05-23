# Raspberry Pi Camera 3 test from https://docs.ultralytics.com/guides/raspberry-pi/#inference-with-camera
# Note that the picamera2 library (for the Rasp Pi Camera 3) is part of the latest Rasp Pi OS
# but you have to include the --system-site-packages when creating the virt env. For example:
#     python3 -m venv --system-site-packages env

import cv2
from picamera2 import Picamera2, Preview

from ultralytics import YOLO

#initialize the Picamera2
picam2 = Picamera2()
picam2.preview_configuration.main.size = (1280, 720)
picam2.preview_configuration.main.format = "RGB888"
picam2.preview_configuration.align()
picam2.configure("preview")
picam2.start()

#load the YOLO11 model
model = YOLO("resources/model/yolo11n.pt")

while True:
    #Capture frame-by-frame
    frame = picam2.capture_array()

    # Run Yolo11 inference on the frame
    results = model(frame)

    # Visualize the results on the frame
    annotated_frame = results[0].plot()

    # Display the resulting frame
    cv2.imshow("Camera", annotated_frame)

    # Break the loop is 'q' is pressed
    if cv2.waitKey(1) == ord("q"):
        break

# Release resources and close windows
cv2.destroyAllWindows()
