import cv2
import dlib
import blinkratio

cap = cv2.VideoCapture(0)

cv2.namedWindow('BlinkDetector')

detector = dlib.get_frontal_face_detector()

predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

left_eye_landmarks = [36, 37, 38, 39, 40, 41]
right_eye_landmarks = [42, 43, 44, 45, 46, 47]

threshold = 6.0
count = 0

while True:
    retval, frame = cap.read()

    if not retval:
        print("Can't receive frame...")
        break 

    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces,_,_ = detector.run(image = gray_frame, upsample_num_times = 0,
                             adjust_threshold = 0.0)

    for face in faces:
        landmarks = predictor(gray_frame, face)
        left_eye_ratio  = blinkratio.blinkratio_calc(left_eye_landmarks, landmarks)
        right_eye_ratio = blinkratio.blinkratio_calc(right_eye_landmarks, landmarks)
        blink_ratio     = (left_eye_ratio + right_eye_ratio) / 2
            
        if blink_ratio > threshold:
            cv2.putText(frame,"BLINKING",(10,50), cv2.FONT_HERSHEY_SIMPLEX,2,(255,255,255),2,cv2.LINE_AA)
            count += 1
            print("No. of Blinks:")
            print(count)
       
    cv2.imshow('BlinkDetector', frame)
    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()

 