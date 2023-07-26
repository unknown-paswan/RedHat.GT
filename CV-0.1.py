import cv2

def faceBox(faceNet, frame):
    frameHeight = frame.shape[0]
    frameWidth = frame.shape[1]
    blob = cv2.dnn.blobFromImage(frame, 1.0, (227, 227), [104, 117, 123], swapRB=True, crop=False)
    faceNet.setInput(blob)
    detections = faceNet.forward()
    bboxs = []
    for i in range(detections.shape[2]):
        confidence = detections[0, 0, i, 2]
        if confidence > 0.7:  # Adjust the confidence threshold as needed
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

ageList = ['(0-2)', '(4-6)', '(8-12)', '(15-20)', '(25-32)', '(38-43)', '(48-53)', '(60-100)']

while True:
    a = int(input("Enter 1 to start video capture, or 2 to open an image file: "))
    if a == 1:
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

                cv2.rectangle(frame, (bbox[0], bbox[1] - 30), (bbox[2], bbox[1]), (135, 206, 250), -1)
                cv2.putText(frame, f'Age: {ageRange}', (bbox[0], bbox[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

                if cv2.waitKey(1) & 0xFF == ord('s'):
                    # Create a filename with age information
                    filename = f'face_{ageRange}.jpg'

                    # Save the frame with annotations
                    cv2.imwrite(filename, frame)

                    # Show a confirmation message
                    print(f"Saved {filename} with age: {ageRange}")

            cv2.imshow("camera", frame)
            k = cv2.waitKey(1)
            if k == ord('q'):
                break

        video.release()
        cv2.destroyAllWindows()
        break
    elif a == 2:
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

                cv2.rectangle(frame, (bbox[0], bbox[1] - 30), (bbox[2], bbox[1]), (135, 206, 250), -1)
                cv2.putText(frame, f'Age: {ageRange}', (bbox[0], bbox[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

                if cv2.waitKey(1) & 0xFF == ord('s'):
                    # Create a filename with age information
                    filename = f'face_{ageRange}.jpg'

                    # Save the frame with annotations
                    cv2.imwrite(filename, frame)

                    # Show a confirmation message
                    print(f"Saved {filename} with age: {ageRange}")

            cv2.imshow("image", frame)
            while True:
                if cv2.waitKey(20) & 0xFF == ord('n'):
                    cv2.destroyAllWindows()
                    break
                elif cv2.waitKey(20) & 0xFF == ord('r'):
                    cv2.destroyAllWindows()
                    gh()
                elif cv2.waitKey(20) & 0xFF == ord('e'):
                    cv2.destroyAllWindows()
                    exit()

        def gh():
            b = input(r'Enter the path for the image file: ')
            process_image(b)

        gh()
