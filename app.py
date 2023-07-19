import cv2
import numpy as np
from flask import Flask, render_template, request

app = Flask(__name__)

faceProto = "opencv_face_detector.pbtxt"
faceModel = "opencv_face_detector_uint8.pb"
faceNet = cv2.dnn.readNet(faceModel, faceProto)

ageProto = "age_deploy.prototxt"
ageModel = "age_net.caffemodel"
ageNet = cv2.dnn.readNet(ageModel, ageProto)

genderProto = "gender_deploy.prototxt"
genderModel = "gender_net.caffemodel"
genderNet = cv2.dnn.readNet(genderModel, genderProto)

genderList = ['Male', 'Female']
ageList = ['(0-2)', '(4-6)', '(8-12)', '(15-20)', '(25-32)', '(38-43)', '(48-53)', '(60-100)']

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
            cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0))
    return frame, bboxs

@app.route('/')
def index():
    return render_template('index4.html')

@app.route('/open_image', methods=['POST'])
def open_image():
    file = request.files['file']
    img = cv2.imdecode(np.frombuffer(file.read(), np.uint8), cv2.IMREAD_COLOR)
    frame, bboxs = faceBox(faceNet, img)
    # ... Rest of the code for face detection, age, and gender prediction ...
    cv2.imshow("image", frame)
    while True:
        if cv2.waitKey(20) & 0xFF == ord('n'):
            cv2.destroyAllWindows()
            break
        elif cv2.waitKey(20) & 0xFF == ord('r'):
            cv2.destroyAllWindows()
            return open_image()
        elif cv2.waitKey(20) & 0xFF == ord('e'):
            cv2.destroyAllWindows()
            return "Image processing aborted!"
    return "Image processing completed!"

if __name__ == '__main__':
    app.run()
