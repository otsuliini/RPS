from hand_detector import HandDetector

# Initialize the hand detector with the video path
video_path = "path_to_video.mp4"  # Update with the correct path
detector = HandDetector(video_path)

# Get the hand landmarks
hand_landmarks = detector.detect_hands()

# Process the hand landmarks as needed
for landmarks in hand_landmarks:
    print(landmarks)  # Example: print the landmarks
