# cv-pi
## Code for learning about CV on Raspberry Pi

The Raspberry Pi (RasPi) has its own cameras (Model 3 & AI) and software system (Picamera2) to manage the cameras. Picamera2 has software that is specialized to handle the details of their cameras. For example, the Image Sensor Processor (ISP) routinely splits the stream of data coming from the camera into two channels, main and lores (low resolution). Each channel can be independently configured EXCEPT that they must use the same color scheme.

When pursuing low-end/low-cost edge devices that will do object detection and pose estimation, RasPi has significant capabilities but they may be unique. The RasPi can load and use OpenCV as well as Yolo/Ultralytics and TensorFlowLite.

## Goals

* Explore the Picamera2 software without using models from other projects as much as possible
* Explore the RasPi AI camera
* Explore the capabilities of the RasPi AI Kit - how does it compare to the RasPi AI camera?
* Can the RasPi AI camera and AI Kit be used together for improved capabilites?
* Can the RasPi add cameras from other manufacturers? 
* Can the Pi Zero/ Pi Pico do Object Detection/Pose Estimation when matched with the right camera/etc?
