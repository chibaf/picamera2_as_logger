from picamera2 import Picamera2, Preview
from libcamera import controls
import time

pc2 = Picamera2()
pc2.start_preview( True )

i=0

while True:

  i=i+1

# start??????set_controls??????
  pc2.start()

# Continuous???
#  ?????????????????????
  pc2.set_controls( {"AfMode" : controls.AfModeEnum.Continuous} )
  pc2.capture_file("test"+str(i)+".jpg")

  time.sleep( 5 )
