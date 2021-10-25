import cv2
import mediapipe as mp

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

# For static images:
with mp_hands.Hands(
    static_image_mode=True,
    max_num_hands=2,
    min_detection_confidence=0.5) as hands:

    image = cv2.imread("manos1.jpg")
    height, width, _ = image.shape
    image = cv2.flip(image, 1)

  # ---------------------------------------------
    # Convert the BGR image to RGB before processing.
    results = hands.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
  # ---------------------------------------------
    # Print handedness and draw hand landmarks on the image.
    # print('Handedness:', results.multi_handedness)
  # ---------------------------------------------
    index = [4, 8, 12, 16, 20]
    for hand_landmarks in results.multi_hand_landmarks:
          # ---------------------------------------------
            # print(hand_landmarks)
      # ---------------------------------------------
            # dibujando las conexiones
        for (i, points) in enumerate(hand_landmarks.landmark):
            if i in index:
                x = int(points.x * width)
                y = int(points.y * height)
                if i == 4:
                  nom="thumb"
                elif i == 8:
                  nom="index"
                elif i == 12:
                  nom="middle"
                elif i == 16:
                  nom="ring"
                elif i == 20:
                  nom="pinky"
                else:
                  nom="unidentified"
                print(nom,x,y)
                cv2.circle(image, (x, y), 3,(255, 0, 255), 3)


    image = cv2.flip(image, 1)
    cv2.imshow("Image",image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()