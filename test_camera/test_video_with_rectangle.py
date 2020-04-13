# USAGE
# python test_video_with_rectangle.py

# import the necessary packages
from picamera.array import PiRGBArray
from picamera import PiCamera
import datetime
import imutils
import time
import cv2

# Define constants
conf = {
        "camera_warmup_time": 2.5,
        "resolution": [1280, 720],
        "fps": 30
        }

# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
camera.resolution = tuple(conf["resolution"])
camera.framerate = conf["fps"]
rawCapture = PiRGBArray(camera, size=tuple(conf["resolution"]))

# allow the camera to warmup, then initialize the average frame, last
# uploaded timestamp, and frame motion counter
print("[INFO] warming up...")
time.sleep(conf["camera_warmup_time"])
avg = None

# capture frames from the camera
for f in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    # grab the raw NumPy array representing the image and initialize
    # the timestamp and movement/no movement text
    frame = f.array
    timestamp = datetime.datetime.now()

    # if the average frame is None, initialize it
    if avg is None:
        print("[INFO] starting background model...")
        avg = gray.copy().astype("float")
        rawCapture.truncate(0)
        continue
        
    # draw rectangle as reference on video
    cv2.rectangle(frame,(450,180),(600,220),(0,255,0),2)
    
    # draw the text and timestamp on the frame
    ts = timestamp.strftime("%A %d %B %Y %I:%M:%S%p")
    cv2.putText(frame, ts, (10, frame.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX,
        0.35, (0, 0, 255), 1)

    # display the security feed
    cv2.imshow("Cuthbert camera", frame)
    key = cv2.waitKey(1) & 0xFF

    # if the `q` key is pressed, break from the lop
    if key == ord("q"):
        break

    # clear the stream in preparation for the next frame
    rawCapture.truncate(0)
