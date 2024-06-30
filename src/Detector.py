from ultralytics import YOLO
import cv2
from util import Utility

capture = cv2.VideoCapture(0)

capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

model = YOLO("C:/Users/aweso/Documents/BoeingVision/src/best.pt")
model.to('cuda')

highestConfidence = 0.8
lineLength = 20

while(True):
    isOK, frame = capture.read()

    if not isOK:
        break

    results = model(frame)
    detections = results[0] 
    annotatedFrame = detections.plot()

    frame_to_use = frame

    #cv2.imshow("annotated", frame_to_use)

    #[[xmin, ymin, xmax, ymax, confidence_score, class_id], ...]

    for data in detections.boxes.data.tolist():
        confidence = data[4]
        id = data[5]

        if(confidence <= highestConfidence):
            continue

        xmin, ymin, xmax, ymax = int(data[0]), int(data[1]), int(data[2]), int(data[3])

        xMiddle = int((xmax + xmin) / 2)
        yMiddle = int((ymax + ymin) / 2)

        #cv2.putText(annotatedFrame, str(xMiddle), (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 8)


        Utility.draw_crosshair(
            frame = frame_to_use,
            x_mid = xMiddle,
            y_mid = yMiddle,
            length = lineLength
        )

        Utility.draw_box(
            frame = frame_to_use,
            x_min = xmin,
            x_max = xmax,
            y_min = ymin,
            y_max = ymax
        )

        Utility.put_text(
            frame = frame_to_use,
            text = round(confidence, 3),
            x = xmin,
            y = ymax + 25  
        )

        Utility.put_text(
            frame = frame_to_use,
            text = id,
            x = xmin,
            y = ymin - 10
        )
        

        print(id)
        #cv2.rectangle(frame, (xmin, ymin) , (xmax, ymax), (0, 0, 255), 2)
        #cv2.putText(frame, str(id), (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 8)

    cv2.imshow("annotated", frame_to_use)

    if cv2.waitKey(1) == ord("q"):
        break

capture.release()
cv2.destroyAllWindows()