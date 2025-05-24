'''
From The Picamera2 Library pdf, pg 23, Chap 4, Configurations
'''
from picamera2 import Picamera2, Preview
import time 

picam2 = Picamera2()
mode = picam2.sensor_modes[1] #valid modes = 0, 1, 2
# mode 0 = ~30 fps, mode 1 = ~37 fps, mode 2 = ~14 fps
mode_size = mode['size']
mode_w = mode_size[0]
if mode_w > 4000: #Max width is 4096 
    mode_w = 4000
mode_h = mode_size[1]
if mode_h > 2500: #Don't know if there is a max height but might as well set it
    mode_h = 2500
config = picam2.create_preview_configuration(sensor={'output_size': mode['size'], 'bit_depth': mode['bit_depth']},
                                             main={"size": (mode_w, mode_h)}, 
                                             lores={"size":(320,240)}, display="main")
picam2.configure(config)
print("Cam Config2: " + str(picam2.camera_config['controls']))

'''
Originally, the output of this prog is a bunch of streams the camera can use
In the line, "mode = ...[0]" it is selecting the first sensor mode
Today, the behavior is that 4 streams are listed. The first [0] is the lowest
res, second is medium res, and third is the highest res. The actual
selected mode is listed last. Selecting the first mode **[0]** results in the
lowest res mode being the "Selected CFE format: 1536x864-PC1B" 
After these configs show, start the preview window to see how the diff modes look
'''
picam2.start_preview(Preview.QTGL, x=400, y=100, width=mode_w, height=mode_h) #set preview window per sensor_mode
picam2.title_fields = ["ExposureTime", "AnalogueGain", "FrameDuration"] # Preview window requires Qt
# See Picamara2 Library Appendix C for more potential title_fields
picam2.start()
time.sleep(5)
#picam2.stop()

''' get back to this
preview = picam2.create_preview_configuration(main={"size": (1920, 1080)})
picam2.configure(preview)
picam2.start_preview(Preview.QTGL)
picam2.start()
time.sleep(2)
'''                                      