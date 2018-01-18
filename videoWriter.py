import cv2,numpy as np
cam = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('sachinflipedcideo.avi',fourcc,20.0,(640,480))
while(cam.isOpened()):

    ret,frame    = cam.read()
    if ret == True:

        frae = cv2.flip(frame,0)
        out.write(frae)

        cv2.imshow("video fliped window :) ",frae)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
cam.release()
out.release()
cv2.destroyAllWindows()
