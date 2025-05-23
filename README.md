# cv-pi
## Code for learning about CV on Raspberry Pi

The Raspberry Pi (RasPi) has its own cameras (Model 3 & AI) and software system (Picamera2) to manage the cameras. Picamera2 has software that is specialized to handle the details of their cameras. For example, the Image Sensor Processor (ISP) normally splits the stream of data coming from the camera into two channels, main and lores (low resolution). Each channel can be independently configured EXCEPT that they must use the same color schema.

When pursuing low-end/low-cost edge devices that will do object detection and pose estimation, RasPi has significant capabilities but they may be unique. In addition to the Picamera2 library, the RasPi can load and use OpenCV as well as Yolo/Ultralytics and TensorFlowLite.

Be sure to find the doc, The Picamera2 Library PDF. It contains all sorts of detailed features that the camera can perform, such as transforms and colour_space, etc. Note that the word "transform" is a keyword, with its usage like `transform=Transform(hflip=True)`. Most of the apps in this repos are derived from that doc.

## Environment

* `python3 -m venv --system-site-packages env` (this creates a virtual environment in the cv-pi folder that was named "env". The sub-folder was named "env" and it was set to include the system files (the --system-site-packages option))
* `source env/bin activate` to start the virtual env.  `deactivate` to stop the virtual env
* `pip install opencv-python`  OR `sudo apt install python3-opencv` (second option maybe better)
* `pip install ultralytics`
* `pip install matplotlib`
* `pip install tflite-runtime` (installed TensorFlow Lite)

## Goals

* Explore the Picamera2 software without using models from other projects as much as possible
* Explore the RasPi AI camera
* Explore the capabilities of the RasPi AI Kit - how does it compare to the RasPi AI camera?
* Can the RasPi AI camera and AI Kit be used together for improved capabilites?
* Can the RasPi add cameras from other manufacturers? 
* Can the Pi Zero/ Pi Pico do Object Detection/Pose Estimation when matched with the right camera/etc?

## Program Notes

* pi_cam_test1.py uses YOLO to detect objects. It is sort of laggy when run against live video using Rasp Pi Camera 3 and no other optimizations (FPS, image size, etc)
* overlay_colors.py creates a preview window that shows for 1 second and then displays the same image with 3 colored overlays in 3 of the 4 quadrants of the image.
* test_pre_callback.py inserts the timestamp onto each image frame before any other processing is done. The original program was modified to experiment with different features, such as image size and preveiw image size and location of the window. It would fail to run with error messages about not being able to initialze Qt plugin xcb. Turned out it needed QT_PLUGIN_PATH to be set to /lib/aarch64-linux-gnu/qt/plugins/platforms. It also turns out that OpenCV is normally compiled with Qt support which is a classic tool to help write X-window interactions - latest Raspberry Pi OS (bookworm) ships with wayland that supercedes X-windows so Qt isn't needed unless your app (opencv) needs it. If you do need it, the appropriate Qt5 libs are already there, waiting to be pointed to and accessed

* Packages installed with Ultralytics:Successfully installed contourpy-1.3.2 cycler-0.12.1 filelock-3.18.0 fonttools-4.58.0 fsspec-2025.5.0 kiwisolver-1.4.8 matplotlib-3.10.3 mpmath-1.3.0 networkx-3.4.2 opencv-python-4.11.0.86 packaging-25.0 pandas-2.2.3 py-cpuinfo-9.0.0 python-dateutil-2.9.0.post0 pyyaml-6.0.2 scipy-1.15.3 sympy-1.14.0 torch-2.7.0 torchvision-0.22.0 typing-extensions-4.13.2 tzdata-2025.2 ultralytics-8.3.142 ultralytics-thop-2.0.14
