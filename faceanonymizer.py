import os
import cv2
import mediapipe as mp


img = cv2.imread(os.path.join('.', 'data', 'drakemaye.jpg'))

img_h, img_w = img.shape[:2]

#reading webcam
webcam = cv2.VideoCapture(0)
#media pipe face detector
mp_face_detection = mp.solutions.face_detection

with mp_face_detection.FaceDetection(model_selection=0, min_detection_confidence=.5) as face_detection:
#visualizing webcam
    while True:
        ret, frame = webcam.read()

        h, w = frame.shape[:2]

        frame_rgb = cv2.cvtCOLOR(frame, cv2.COLOR_BGR2RGB)

        #run detector on this frame
        result = face_detection.process(frame_rgb)

        #if faces exists loop through them and draw boxes
        if results.detections:
            for detection in result.detections:
                bbox = detection.location_data.relative_bounding_box

                # Convert relative coords -> pixel coords
                x1 = int(bbox.xmin * w)
                y1 = int(bbox.ymin * h)
                bw = int(bbox.width * w)
                bh = int(bbox.height * h)

                x2 = x1 + bw
                y2 = y1 + bh

                # Clamp to image bounds (prevents negative coords / overflow)
                x1 = max(0, x1); y1 = max(0, y1)
                x2 = min(w, x2); y2 = min(h, y2)

                # Confidence score (0..1)
                score = detection.score[0]

                # 7) Draw rectangle + score on the ORIGINAL BGR frame
                cv2.rectangle(frame_bgr, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.putText(
                    frame_bgr,
                    f"{score:.2f}",
                    (x1, max(0, y1 - 10)),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.8,
                    (0, 255, 0),
                    2
                )
                



        cv2.imshow("Webcam", frame)
        if cv2.waitKey(0)& 0xFF == ord("q"):
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