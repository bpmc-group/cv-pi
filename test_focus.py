from picamera2 import Picamera2
import time
from libcamera import controls
picam2 = Picamera2()
picam2.start(show_preview=True)
# AutoFocus Mode = CONTINUOUS
picam2.set_controls({"AfMode": controls.AfModeEnum.Continuous})

# AutoFocus Mode = MANUAL
# LensPos = 10.0 is max close focus about 3" | LensPos = 0.0 is infinity focus
# picam2.set_controls({"AfMode": controls.AfModeEnum.Manual, "LensPosition": 0.0})

# AutoFocuse Mode = AUTO
# Note that the autofocus_cycle doesn't block waiting for results
# Instead, success waits for the job to complete and then prints result (True)
#job = picam2.autofocus_cycle(wait = False)
#success = picam2.wait(job)
#print(success)

time.sleep(10)