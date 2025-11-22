import cv2
myCam=cv2.VideoCapture(0)
while True:
    _,frame=myCam.read()
    cv2.imshow("My Cam",frame)
    cv2.moveWindow("My Cam",0,0)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
myCam.release()