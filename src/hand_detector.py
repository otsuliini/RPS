import mediapipe as mp
import cv2
import numpy as np

class HandDetector:
    def __init__(self, video_path):
        self.cap = cv2.VideoCapture(video_path)  # Initialize video capture
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands()
        self.mp_draw = mp.solutions.drawing_utils

    def detect_hands(self):
        hand_landmarks_list = []
        while self.cap.isOpened():
            ret, frame = self.cap.read()
            if not ret:
                break

            # Convert BGR to RGB for MediaPipe
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            # Process the frame
            results = self.hands.process(rgb_frame)

            # Collect hand landmarks
            if results.multi_hand_landmarks:
                for hand_landmarks in results.multi_hand_landmarks:
                    hand_landmarks_list.append(hand_landmarks)
                    self.mp_draw.draw_landmarks(frame, hand_landmarks, self.mp_hands.HAND_CONNECTIONS)

            # Display the frame
            cv2.imshow('Hand Detection', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        # Release resources
        self.cap.release()
        cv2.destroyAllWindows()
        return hand_landmarks_list

# Usage
video_path = "path_to_video.mp4"  # Update with the correct path
detector = HandDetector(video_path)
landmarks = detector.detect_hands()
