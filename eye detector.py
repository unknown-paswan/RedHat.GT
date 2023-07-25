import cv2
import time
import numpy as np
import pyaudio
import threading


def play_emergency_alarm_sound():
    duration = 0.2  # seconds
    frequency = 2000  # Hz
    sample_rate = 44100  # Samples per second
    num_beeps = 10

    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paFloat32,
                    channels=1,
                    rate=sample_rate,
                    output=True)

    for i in range(num_beeps):
        t = np.linspace(0, duration, int(sample_rate * duration), False)
        wave = 0.5 * np.sin(2 * np.pi * frequency * t)
        stream.write(wave.tobytes())
        time.sleep(0.1)  # Pause between beeps

    # Close the audio stream and terminate PyAudio
    stream.stop_stream()
    stream.close()
    p.terminate()

def faceBox(faceNet, frame):
    frameHeight = frame.shape[0]
    frameWidth = frame.shape[1]
    blob = cv2.dnn.blobFromImage(frame, 1.0, (300, 300), [104, 117, 123], swapRB=True, crop=False)
    faceNet.setInput(blob)
    detections = faceNet.forward()
    bboxs = []
    for i in range(detections.shape[2]):
        confidence = detections[0, 0, i, 2]
        if confidence > 0.7:
            x1 = int(detections[0, 0, i, 3] * frameWidth)
            y1 = int(detections[0, 0, i, 4] * frameHeight)
            x2 = int(detections[0, 0, i, 5] * frameWidth)
            y2 = int(detections[0, 0, i, 6] * frameHeight)
            bboxs.append([x1, y1, x2, y2])
            cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), 2)
    return frame, bboxs

def detect_eyes(cascade_left, cascade_right, gray_frame):
    left_eye = cascade_left.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=5, minSize=(25, 25))
    right_eye = cascade_right.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=5, minSize=(25, 25))
    return left_eye, right_eye

def main():
    # Load the pre-trained eye detection cascade classifiers for left and right eyes
    eye_cascade_left = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_lefteye_2splits.xml")
    eye_cascade_right = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_righteye_2splits.xml")

    # Start the webcam
    video_capture = cv2.VideoCapture(0)

    # Load the pre-trained face detection model
    faceProto = "opencv_face_detector.pbtxt"
    faceModel = "opencv_face_detector_uint8.pb"
    faceNet = cv2.dnn.readNet(faceModel, faceProto)

    # Variables to keep track of time
    start_time = None
    wakeup_time_threshold = 2

    while True:
        # Capture frame-by-frame
        ret, frame = video_capture.read()
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect faces and draw rectangles around them
        frame, _ = faceBox(faceNet, frame)

        # Detect eyes in the frame
        left_eye, right_eye = detect_eyes(eye_cascade_left, eye_cascade_right, gray_frame)

        if len(left_eye) == 0 or len(right_eye) == 0:
            # If either eye is closed
            if start_time is None:
                # Start timer
                start_time = time.time()
            else:
                # Check if the time threshold has been exceeded
                current_time = time.time()
                elapsed_time = current_time - start_time
                if elapsed_time > wakeup_time_threshold:
                    # Play the emergency alarm sound in a separate thread
                    alarm_thread = threading.Thread(target=play_emergency_alarm_sound)
                    alarm_thread.start()

                    start_time = None  # Reset the timer

        else:
            # If both eyes are open, reset the timer
            start_time = None

            # Draw rectangles around both eyes
            for (x, y, w, h) in left_eye:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

            for (x, y, w, h) in right_eye:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        cv2.imshow('Eye and Face Detection', frame)

        # Exit the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the webcam and close the window
    video_capture.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
