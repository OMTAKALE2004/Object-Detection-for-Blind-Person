import cv2
import time
from picamera2 import Picamera2
import pyttsx3
import RPi.GPIO as GPIO

flag=False

GPIO.setmode(GPIO.BCM)
TRIG=21
ECHO=20
GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)



text_speech = pyttsx3.init()




from tflite_support.task import core
from tflite_support.task import processor
from tflite_support.task import vision
#import utils



model='efficientdet_lite0.tflite'
num_threads=3

dispW=320
dispH=240

piCam2=Picamera2()
piCam2.preview_configuration.main.size=(dispW,dispH)
piCam2.preview_configuration.main.format='RGB888'
piCam2.preview_configuration.align()
piCam2.configure("preview")
piCam2.start()




font=cv2.FONT_HERSHEY_SIMPLEX


labelHeight=1.5
labelWeight=(2)
labelColor=(0,255,0)


boxColor=(255,0,0)
boxWeight=2






base_options=core.BaseOptions(file_name=model, num_threads=num_threads)
detection_options=processor.DetectionOptions(max_results=3, score_threshold=.6)
options=vision.ObjectDetectorOptions(base_options=base_options,detection_options=detection_options)
detector=vision.ObjectDetector.create_from_options(options)

def measure_distance():
    
    GPIO.output(TRIG,False)
    time.sleep(0.2)
    GPIO.output(TRIG,True)
    time.sleep(0.00001)
    GPIO.output(TRIG,False)
    while GPIO.input(ECHO)==0:
        pulse_start=time.time()
    while GPIO.input(ECHO)==1:
        pulse_end=time.time()
    pulse_duration=pulse_end-pulse_start
    distance=pulse_duration*17150
    distance=round(distance,2)
    
        
    return distance




while True:
    distance=measure_distance()
    while distance < 40.0 :
        flag=True
        text_speech.say("Stop")
        text_speech.runAndWait()
        distance=measure_distance()
    if flag:
        text_speech.say("Continue")
        text_speech.runAndWait()
        flag=False
        

    im=piCam2.capture_array()
    #im=cv2.flip(im,1)
    imRGB=cv2.cvtColor(im,cv2.COLOR_BGR2RGB)
    imTensor=vision.TensorImage.create_from_array(imRGB)
    myDetects=detector.detect(imTensor)
    
    for myDetect in myDetects.detections:
    
        UL=(myDetect.bounding_box.origin_x,myDetect.bounding_box.origin_y)
        LR=(myDetect.bounding_box.origin_x+myDetect.bounding_box.width,myDetect.bounding_box.origin_y+myDetect.bounding_box.height)
        objName=myDetect.categories[0].category_name
    
        im=cv2.rectangle(im,UL,LR,boxColor,boxWeight)
        cv2.putText(im,objName,UL,font,labelHeight,labelColor,labelWeight)
        #object position code
        center_x=(myDetect.bounding_box.origin_x+myDetect.bounding_box.origin_x+myDetect.bounding_box.width)/2
        #center_y=(myDetect.bounding_box.origin_y+myDetect.bounding_box.origin_y+myDetect.bounding_box.height)/2
        image_center_x=dispW/2
        #image_center_y=dispH/2
        
        if center_x<image_center_x:
            position="left"
        elif center_x>image_center_x:
            position="right"
        else:
            position="center"
            
        
        text_speech.say(objName+"detected on"+position)
        text_speech.runAndWait()
        time.sleep(3)
    
    
        
        

    cv2.imshow('Camera',im)
    if cv2.waitKey(1)==ord('q'):
        break


cv2.destroyAllWindows()

#ultrasonic sensor code
