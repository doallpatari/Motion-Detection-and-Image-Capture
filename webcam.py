import cv2
import time
import os

global i
i=0
path = 'C:/Users/yashp/OneDrive/Desktop/Project Work/AE/Images'
class web_c:
    

    def start_wc(self):
        timeout = time.time() + 5
        cap = cv2.VideoCapture(0)


        if not cap.isOpened():
            raise IOError("Cannot open webcam")

        while True:
            ret, frame = cap.read()
            frame = cv2.resize(frame, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
            cv2.imshow('Input', frame)
            global i

            cv2.imwrite(os.path.join(path,"img_+"+str(i)+".jpg"),frame )
            i=i+1
            print(i)
            c = cv2.waitKey(1)
            if c == 27 or time.time() > timeout or i==5:
                cap.release()
                cv2.destroyAllWindows()
                break
            
