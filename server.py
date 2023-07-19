import cv2
import os
from flask import Flask, render_template, request

app = Flask(__name__)

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

@app.route("/")
def index():
    return render_template("index4.html")

@app.route("/start_capture", methods=["POST"])
def start_capture():
    video = cv2.VideoCapture(0)
    while True:
        ret, frame = video.read()
        frame, bboxs = faceBox(faceNet, frame)
        for bbox in bboxs:
            face = frame[bbox[1]:bbox[3], bbox[0]:bbox[2]]
            blob = cv2.dnn.blobFromImage(face, 1.0, (227, 227), (78.4263377603, 87.7689143744, 114.895847746), swapRB=False)

            # Age prediction
            ageNet.setInput(blob)
            agePred = ageNet.forward()
            ageId = agePred[0].argmax()
            ageRange = ageList[ageId]

            # Gender prediction
            genderNet.setInput(blob)
            genderPred = genderNet.forward()
            genderId = genderPred[0].argmax()
            gender = genderList[genderId]

            cv2.rectangle(frame, (bbox[0], bbox[1] - 30), (bbox[2], bbox[1]), (135, 206, 250), -1)
            cv2.putText(frame, f'Age: {ageRange}', (bbox[0], bbox[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
            cv2.putText(frame, f'Gender: {gender}', (bbox[0], bbox[1] - 60), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

            if cv2.waitKey(1) & 0xFF == ord('s'):
                # Create a filename with age and gender information
                filename = f'face_{ageRange}_{gender}.jpg'

                # Save the frame with annotations
                cv2.imwrite(filename, frame)

                # Show a confirmation message
                print(f"Saved {filename} with age: {ageRange} and gender: {gender}")

        cv2.imshow("camera", frame)
        k = cv2.waitKey(1)
        if k == ord('q'):
            break

    video.release()
    cv2.destroyAllWindows()
    return "Video capture completed."

@app.route("/open_image", methods=["POST"])
def open_image():
    def process_image(image_path):
        img = cv2.imread(image_path)
        frame, bboxs = faceBox(faceNet, img)
        for bbox in bboxs:
            face = frame[bbox[1]:bbox[3], bbox[0]:bbox[2]]
            blob = cv2.dnn.blobFromImage(face, 1.0, (227, 227), (78.4263377603, 87.7689143744, 114.895847746), swapRB=False)

            # Age prediction
            ageNet.setInput(blob)
            agePred = ageNet.forward()
            ageId = agePred[0].argmax()
            ageRange = ageList[ageId]

            # Gender prediction
            genderNet.setInput(blob)
            genderPred = genderNet.forward()
            genderId = genderPred[0].argmax()
            gender = genderList[genderId]

            cv2.rectangle(frame, (bbox[0], bbox[1] - 30), (bbox[2], bbox[1]), (135, 206, 250), -1)
            cv2.putText(frame, f'Age: {ageRange}', (bbox[0], bbox[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
            cv2.putText(frame, f'Gender: {gender}', (bbox[0], bbox[1] - 60), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

            if cv2.waitKey(1) & 0xFF == ord('s'):
                # Create a filename with age and gender information
                filename = f'face_{ageRange}_{gender}.jpg'

                # Save the frame with annotations
                cv2.imwrite(filename, frame)

                # Show a confirmation message
                print(f"Saved {filename} with age: {ageRange} and gender: {gender}")

        cv2.imshow("image", frame)
        while True:
            if cv2.waitKey(20) & 0xFF == ord('n'):
                cv2.destroyAllWindows()
                break
            elif cv2.waitKey(20) & 0xFF == ord('r'):
                cv2.destroyAllWindows()
                process_image(image_path)
            elif cv2.waitKey(20) & 0xFF == ord('e'):
                cv2.destroyAllWindows()
                exit()

    image_path = request.form.get("path")
    process_image(image_path)
    return "Image processing completed."

if __name__ == "__main__":
    app.run()
