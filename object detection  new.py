from ultralytics import YOLO
# from gtts import gTTS
# from playsound import playsound 
 
import cv2
import cvzone
import math


 


#cap=cv2.VideoCapture(0)
cap=cv2.VideoCapture("C:\\Users\\OM\\Desktop\\Object Detection for blind person project\\video\\objdemovid.mp4")

# cap.set(3,640)
# cap.set(4,480)
model=YOLO("../YOLO-Weights/yolov8n.pt")
classNames=['person', 'bicycle', 'car', 'motorcycle', 'airplane', 'bus', 'train', 'truck', 'boat',  'traffic light', 'fire hydrant',
            'stop sign', 'parking meter', 'bench', 'bird', 'cat',  'dog', 'horse', 'sheep', 'cow', 'elephant', 'bear', 'zebra',
            'giraffe', 'backpack',  'umbrella', 'handbag', 'tie', 'suitcase', 'frisbee', 'skis', 'snowboard', 'sports ball', 
            'kite', 'baseball bat', 'baseball glove', 'skateboard', 'surfboard', 'tennis racket',  'bottle', 'wine glass', 'cup',
            'fork', 'knife', 'spoon', 'bowl', 'banana', 'apple',  'sandwich', 'orange', 'broccoli', 'carrot', 'hot dog', 'pizza',
            'donut', 'cake',  'chair', 'couch', 'potted plant', 'bed', 'dining table', 'toilet', 'tv', 'laptop',
            'mouse', 'remote', 'keyboard', 'cell phone', 'microwave', 'oven', 'toaster', 'sink',  'refrigerator', 'book',
            'clock', 'vase', 'scissors', 'teddy bear', 'hair drier', 'toothbrush']

# pygame.mixer.init()
# pygame.mixer.set_num_channels(1) 

while True:
    ret,frame=cap.read()
    
    if not ret:
        break
    
    frame = cv2.resize(frame, (320, 240))
    results=model(frame, stream=True)
    



    for r in results:
        boxes=r.boxes
        for box in boxes:
            
            # Confidence
            conf=math.ceil((box.conf[0]*100))/100
             # Bounding Box
            x1,y1,x2,y2=box.xyxy[0]
            x1,y1,x2,y2=int(x1),int(y1),int(x2),int(y2)
            #print(x1,y1,x2,y2)
            if(conf>0.4):
           
                cv2.rectangle(frame,(x1,y1),(x2,y2),(2550,0,255),3)
                #Class Name
                cls=int(box.cls[0])
                cvzone.putTextRect(frame,f'{classNames[cls]} {conf}',(max(0,x1),max(35,y1)),thickness=1,scale=0.8)
                

    cv2.imshow("Image",frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()

