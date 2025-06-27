import cv2 as cv
import mediapipe as mp
import time
from math import hypot

cap=cv.VideoCapture(0)
pTime=0
mpDraw=mp.solutions.drawing_utils
mpFaceMesh=mp.solutions.face_mesh
faceMesh=mpFaceMesh.FaceMesh(max_num_faces=2)
drawspec=mpDraw.DrawingSpec(thickness=1, circle_radius=1, color=(0, 255, 0))

# Landmark pairs for better accuracy
right_eye_pairs = [(386, 374), (385, 380), (387, 373)]
left_eye_pairs = [(159, 145), (158, 153), (160, 144)]


def eye_closed(landmarks, pairs, w, h, threshold=5):
    distances=[]
    for top_id,bottom_id in pairs:
        top = landmarks[top_id]
        bottom = landmarks[bottom_id]
        
        x1, y1 = int(top.x * w), int(top.y * h)
        x2, y2 = int(bottom.x * w), int(bottom.y * h)

        distances.append(hypot(x2 - x1, y2 - y1))
        
    avg_distance = sum(distances) / len(distances) if distances else 0
    return avg_distance < threshold

while True:
    success,img=cap.read()
    if not success or img is None:
        break 
    rgb=cv.cvtColor(img,cv.COLOR_BGR2RGB)
    results=faceMesh.process(rgb)

    if results.multi_face_landmarks:
        for facelms in results.multi_face_landmarks:
            h, w, c = img.shape

            is_left_closed = eye_closed(facelms.landmark, left_eye_pairs, w, h)
            is_right_closed = eye_closed(facelms.landmark, right_eye_pairs, w, h)

            if is_left_closed and is_right_closed:
                cv.putText(img, "Blinking", (30, 60), cv.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 255), 3)

            mpDraw.draw_landmarks(img, facelms, mpFaceMesh.FACEMESH_TESSELATION,drawspec, drawspec)
            
            for id,lm in enumerate(facelms.landmark):
                x = int(lm.x * w)
                y = int(lm.y * h)
                cv.circle(img, (x, y), 1, (0, 255, 0), 1)
                print(id,x,y)

    cTime= time.time()
    fps=1/(cTime-pTime)
    pTime=cTime
    cv.putText(img,f'FPS: {int(fps)}',(10,30),cv.FONT_HERSHEY_PLAIN,1,(255,0,0),2)
    cv.imshow("Image",img)
    key=cv.waitKey(1)
    if key & 0xFF == ord('q'):
        break
cap.release()
cv.destroyAllWindows()