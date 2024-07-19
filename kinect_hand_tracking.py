import cv2
import mediapipe as mp
import pyautogui
from pyk4a import PyK4A, Config, ImageFormat, DepthMode, FPS

# Initialize the Kinect camera
k4a = PyK4A(
    Config(
        color_format=ImageFormat.COLOR_BGRA32,
        depth_mode=DepthMode.NFOV_UNBINNED,
        camera_fps=FPS.FPS_30
    )
)
k4a.start()

hand_detector = mp.solutions.hands.Hands()
drawing_utils = mp.solutions.drawing_utils
screen_width, screen_height = pyautogui.size()
index_y = 0

try:
    while True:
        # Capture a frame from the Kinect camera
        capture = k4a.get_capture()
        if capture.color is not None:
            # Access the color image
            frame = capture.color

            # Convert the color image from BGRA to BGR for OpenCV
            frame = cv2.cvtColor(frame, cv2.COLOR_BGRA2BGR)

            frame = cv2.flip(frame, 1)
            frame_height, frame_width, _ = frame.shape
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            output = hand_detector.process(rgb_frame)
            hands = output.multi_hand_landmarks

            if hands:
                for hand in hands:
                    drawing_utils.draw_landmarks(frame, hand)
                    landmarks = hand.landmark
                    for id, landmark in enumerate(landmarks):
                        x = int(landmark.x * frame_width)
                        y = int(landmark.y * frame_height)
                        if id == 8:
                            cv2.circle(img=frame, center=(x, y), radius=10, color=(0, 255, 255))
                            index_x = screen_width / frame_width * x
                            index_y = screen_height / frame_height * y
                            pyautogui.moveTo(index_x, index_y)
                        if id == 4:
                            cv2.circle(img=frame, center=(x, y), radius=10, color=(0, 255, 255))
                            thumb_x = screen_width / frame_width * x
                            thumb_y = screen_height / frame_height * y
                            if abs(index_y - thumb_y) < 30:
                                pyautogui.click()
                                pyautogui.sleep(0.1)

            cv2.imshow('Virtual Mouse', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
finally:
    k4a.stop()
    cv2.destroyAllWindows()
