import cv2

cap=cv2.VideoCapture(0)
face_cascade=cv2.CascadeClassifier(r"C:\Users\LIPIKA\AppData\Roaming\Python\Python37\site-packages\cv2\data\haarcascade_frontalface_alt.xml")

while True:

	ret,frame=cap.read()
	gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

	if ret==False:
		continue

	face=face_cascade.detectMultiScale(gray,1.3,5)

		
	#cv2.imshow("FRAME",frame)
	#cv2.imshow("gray",gray)


	for (x,y,w,h) in face:
		cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)

	cv2.imshow("video frame", frame)

	key_pressed=cv2.waitKey(1) & 0xFF
	if key_pressed ==ord('q'):
		break

cap.release()
cv2.destroyAllWindows()
