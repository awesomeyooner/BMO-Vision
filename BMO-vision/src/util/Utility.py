import cv2

def draw_crosshair(frame, x_mid, y_mid, length):

    cv2.line(
            frame, 
            (x_mid - length, y_mid), 
            (x_mid + length, y_mid),
            (0, 0, 255), 
            5
        )
    
    cv2.line(
            frame, 
            (x_mid, y_mid - length), 
            (x_mid, y_mid + length),
            (0, 0, 255), 
            5
        )
    
def draw_box(frame, x_min, x_max, y_min, y_max):

    cv2.line(
            frame, 
            (x_min, y_min), 
            (x_min, y_max),
            (0, 0, 255), 
            5
        )
    
    cv2.line(
            frame, 
            (x_max, y_min), 
            (x_max, y_max),
            (0, 0, 255), 
            5
        )
    
    cv2.line(
            frame, 
            (x_min, y_min), 
            (x_max, y_min),
            (0, 0, 255), 
            5
        )
    
    cv2.line(
            frame, 
            (x_min, y_max), 
            (x_max, y_max),
            (0, 0, 255), 
            5
        )
    
def put_text(frame, text, x, y):
    cv2.putText(
            img = frame, 
            text = str(text), 
            org = (x, y), 
            fontFace = cv2.FONT_HERSHEY_SIMPLEX, 
            fontScale = 1,
            thickness = 3,
            lineType = cv2.LINE_AA,   
            color = (0, 0, 255)
            )