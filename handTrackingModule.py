import cv2
import mediapipe as mp
import time


cap = cv2.VideoCapture(0)

mpHands = mp.solutions.hands #formalityMustDo
hands= mpHands.Hands() #ctrl click on Hands to see default parameters. Change if neccesary
mpDraw= mp.solutions.drawing_utils #gives the dots on hands
pTime=0 #previous time
cTime=0 #currenttime


while True:
    success, img = cap.read()
    imgRGB= cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(img) #processes the frame to give result
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                #print(id, lm)
                h, w, c = img.shape #height width channel
                cx, cy = int(lm.x*w), int(lm.y*h)
                print(id, cx, cy) #which lm, x val , y val
                '''if id ==5:
                    cv2.circle(img, (cx,cy), 30, (255,0,100), cv2.FILLED)
'''
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS) #DRAW HAND AND CONNNCET EM

    cTime=time.time()
    fps = 1/(cTime-pTime)
    pTime=cTime

    cv2.putText(img, str(int(fps)), (10,70), cv2.FONT_HERSHEY_PLAIN,3,(205,0,255),3)
    #10,70 pos of text; font; scale;color; thickness

    cv2.imshow("i", img)
    cv2.waitKey(1)
        # Check if the window is closed
    if cv2.getWindowProperty("i", cv2.WND_PROP_VISIBLE) < 1:
        break

    # Press 'q' to break the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()