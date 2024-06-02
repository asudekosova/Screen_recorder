import pyautogui
import cv2
import numpy as np
import time


resolution = (1920, 1080)


codec = cv2.VideoWriter_fourcc(*"XVID")


filename = "Recording.avi"


fps = 60.0


out = cv2.VideoWriter(filename, codec, fps, resolution)


cv2.namedWindow("Live", cv2.WINDOW_NORMAL)


cv2.resizeWindow("Live", 480, 270)


duration = 10
end_time = time.time() + duration

while time.time() < end_time:
    
    img = pyautogui.screenshot()

    
    frame = np.array(img)

    
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    
    out.write(frame)
    
    
    cv2.imshow('Live', frame)
    
    
    if cv2.waitKey(1) == ord('q'):
        break


out.release()


cv2.destroyAllWindows()


cap = cv2.VideoCapture(filename)
cv2.namedWindow("Playback", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Playback", 480, 270)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    cv2.imshow('Playback', frame)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
