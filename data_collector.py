import os
import cv2
import time
import uuid

IMAGE_PATH = "CollectedImages"

labels = ['Hello', 'Yes', 'No', 'Thanks', 'IloveYou', 'Please']

number_of_images = 5

# Create the main directory if it doesn't exist
if not os.path.exists(IMAGE_PATH):
    os.makedirs(IMAGE_PATH)

for label in labels:
    img_path = os.path.join(IMAGE_PATH, label)
    os.makedirs(img_path, exist_ok=True)

    # Open camera 
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print(f"Error: Could not open video capture for {label}")
        continue

    print(f"Collecting images for {label}")
    time.sleep(3)

    for imgnum in range(number_of_images):
        ret, frame = cap.read()
        if not ret:
            print(f"Error: Could not read frame for {label}")
            break

        imagename = os.path.join(IMAGE_PATH, label, label + '.' + '{}.jpg'.format(str(uuid.uuid1())))
        cv2.imwrite(imagename, frame)
        cv2.imshow('frame', frame)
        time.sleep(2)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

