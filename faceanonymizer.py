import os
import cv2
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision



#reading webcam
webcam = cv2.VideoCapture(0)
#New face detection model for recent mediapipe model
base_options = python.BaseOptions(
    model_asset_path="models/blaze_face_short_range.tflite"
)

options = vision.FaceDetectorOptions(
    base_options=base_options,
    running_mode=vision.RunningMode.IMAGE,
    min_detection_confidence=0.5
)
#media pipe face detector
detector = vision.FaceDetector.create_from_options(options)

#with mp_face_detection.FaceDetection(model_selection=0, min_detection_confidence=.5) as face_detection:
#visualizing webcam
while True:
    ret, frame = webcam.read()
    h, w = frame.shape[:2]
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    # wrap image for MediaPipe Tasks
    mp_image = mp.Image(
        image_format=mp.ImageFormat.SRGB,
        data =frame_rgb
    )
    #run face detection
    result = detector.detect(mp_image)
    # draw boxes
    for detection in result.detections:
        bbox = detection.bounding_box
        x1=bbox.origin_x
        y1=bbox.origin_y
        x2=x1+bbox.width
        y2=y1+bbox.height
        cv2.rectangle(frame, (x1,y1), (x2,y2),(0,255,0), 2)
    #visualize webcam
    cv2.imshow("Webcam", frame)
    if cv2.waitKey(1)& 0xFF == ord("q"):
        break
webcam.release()
cv2.destroyAllWindows()








#detect faces

#model_selection higher value for further away faces closer to 0 close to screen faces
#with mp_face_detection.FaceDetection(model_selection=0, min_detection_confidence=.5) as face_detection:
#    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#    out = face_detection.process(img_rgb)
#
#    if out.detections is not None:
#        for detection in out.detections:
#            location_data = detection.location_data
#            bbox = location_data.relative_bounding_box
#
#            x1,y1,w,h = bbox.xmin, bbox.ymin, bbox.width,bbox.height