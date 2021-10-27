import cv2
import mediapipe as mp
import numpy as np
import itertools as itert

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands

Array coords

# For webcam input:
cam = int(input('\nQué cámara quieres usar pa\n'))
cap = cv2.VideoCapture(cam)
with mp_hands.Hands(
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5) as hands:
  while cap.isOpened():
    success, image = cap.read()
    if not success:
      print("No hay cámara we jaja")
      # If loading a video, use 'break' instead of 'continue'.
      continue

    # Flip the image horizontally for a later selfie-view display, and convert
    # the BGR image to RGB.
    image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
    # To improve performance, optionally mark the image as not writeable to
    # pass by reference.
    image.flags.writeable = False
    results = hands.process(image)
    
    index = [4, 8, 12, 16, 20]
    
    # print(dir(results)) 
    # print(results.multi_hand_landmarks)
    
    # Draw the hand annotations on the image.
    image.flags.writeable = True
    
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    height, width, _ = image.shape
    
    if results.multi_hand_landmarks:
      for hand_landmarks in results.multi_hand_landmarks:
        
        # aquí hace dibujos bonitos uwu
        mp_drawing.draw_landmarks(
            image,
            hand_landmarks,
            mp_hands.HAND_CONNECTIONS,
            mp_drawing_styles.get_default_hand_landmarks_style(),
            mp_drawing_styles.get_default_hand_connections_style())
        
        # y aquí saca las coordenadas
        for (i, points) in enumerate (hand_landmarks.landmark):
          # print(hand_landmarks.landmark)
          if i in index:
            x = int(points.x * width) 
            y = int(points.y * height) 
  
            if i == 4:
              dedo="thumb"
            elif i == 8:
              dedo="index"
            elif i == 12:
              dedo="middle"
            elif i == 16:
              dedo="ring"
            elif i == 20:
              dedo="pinky"
            else:
              dedo="nose"
                  
            # imprime los datos de cada dedo
            coords = np.array([dedo,x,y])
            # print(coords)
            
            top5 = itertools.islice(my_list, 5) # grab the first five elements
            
            # circulito uwu
            cv2.circle(image, (x, y), 3,(190, 225, 230), 3) # (image, center_coordinates, radius, color, thickness)
        
    cv2.imshow('MediaPipe Hands', image)
    if cv2.waitKey(5) & 0xFF == 27:
    
      break
    
cap.release()
# cap.destroyAllWindows() # no funcionaaaaaaaa