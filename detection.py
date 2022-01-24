import cv2 import numpy as np from datetime import datetime    
 
def nothing(x): 
    pass 
 
cap = cv2.VideoCapture(0) cv2.namedWindow("Trackbars") 
 
cv2.createTrackbar("L - H", "Trackbars", 0, 179, nothing) cv2.createTrackbar("L - S", "Trackbars", 0, 255, nothing) cv2.createTrackbar("L - V", "Trackbars", 0, 255, nothing) cv2.createTrackbar("U - H", "Trackbars", 179, 179, nothing) cv2.createTrackbar("U - S", "Trackbars", 255, 255, nothing) cv2.createTrackbar("U - V", "Trackbars", 255, 255, nothing) 
 
while True:     try: 
        _, frame = cap.read() 
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) 
 
        l_h = cv2.getTrackbarPos("L - H", "Trackbars") 
        l_s = cv2.getTrackbarPos("L - S", "Trackbars")         l_v = cv2.getTrackbarPos("L - V", "Trackbars")         u_h = cv2.getTrackbarPos("U - H", "Trackbars")         u_s = cv2.getTrackbarPos("U - S", "Trackbars")         u_v = cv2.getTrackbarPos("U - V", "Trackbars") 
 
        lower_blue = np.array([l_h, l_s, l_v])         upper_blue = np.array([u_h, u_s, u_v])         mask = cv2.inRange(hsv, lower_blue, upper_blue) 
 
        result = cv2.bitwise_and(frame, frame, mask=mask)         gray_img=cv2.cvtColor(result,cv2.COLOR_BGR2GRAY)         img= cv2.medianBlur(gray_img,5) 
        cimg = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)         circles= 
cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,120,param1=100,param2=
30,minRadius=20,maxRadius=35) 
        circles= np.uint16(np.around(circles))         for i in circles[0,:]: 
                        cv2.circle(frame,(i[0],i[1]),i[2],(0,255,0),6)                         r=int(pow(pow((i[0]-240),2)+pow((i[1]-320),2),0.5))                         if r>200:                             p='false'                         else: 
                            p='true' 
                        now = datetime.now() 
                        response = requests.post('https://pua177euf5.execute-api.us-east-
2.amazonaws.com/test/circle', 	json={'timestamp': 
now.strftime("%H:%M:%S"),'radius': r,'pass':p })                         print("Status code: ", response.status_code)                         print("Printing Entire Post Request")                         print(response.json()) 
                        cv2.circle(frame,(i[0],i[1]),2,(0,0,255),3)         cv2.imshow("HoughCirlces",frame)     except AttributeError as error: 
        print("error1") 
        cv2.imshow("HoughCirlces",frame)     except TypeError as error: 
        print("error1") 
        cv2.imshow("HoughCirlces",frame)     key = cv2.waitKey(1)     if key == 27: 
        break 
 
 
cap.release() cv2.destroyAllWindows() 
