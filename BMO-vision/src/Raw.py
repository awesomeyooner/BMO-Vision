import cv2
import uuid
import os
import time

labels = ['bmo']
num_imgs = 5

#workpath for imagespip 
path = os.path.join('resources', 'images', 'train')

#create the image path if it doesnt exist already
if not os.path.exists(path):
    os.makedirs(path)

#create a path for each label
for label in labels:
    label_path = os.path.join(path, label)

    if not os.path.exists(label_path):
        os.makedirs(label_path)

cap = cv2.VideoCapture(0)
cv2.imshow('frame', cap.read()[1])

for label in labels:
    print("Collecting image for {}".format(label))
    time.sleep(5)

    index = 0

    while index < num_imgs + 1:

        ret, frame = cap.read()
        cv2.imshow('frame', frame)
        

        if(cv2.waitKey(1) & 0xFF == ord('q')):
            print('Collecting image {}'.format(index))
            image_name = os.path.join(path, label + '.' + '{}.png'.format(str(uuid.uuid1())))
            cv2.imwrite(image_name, frame)
            time.sleep(0.5)
            print("Captured!")
            index += 1

        if(cv2.waitKey(1) & 0xFF == ord('c')):
            break

cap.release()
cv2.destroyAllWindows()


