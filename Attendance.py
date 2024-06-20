import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime, timedelta

path = 'Students'
images = []
classNames = []
myList = os.listdir(path)
print(myList)

for cl in myList:
    curImg = cv2.imread(f'{path}/{cl}')
    if curImg is None:
        print(f"Image {cl} not loaded correctly.")
        continue
    images.append(curImg)
    classNames.append(os.path.splitext(cl)[0])
print(classNames)


def findEncodings(images):
    encodeList = []
    for img in images:
        if img is not None:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            encode = face_recognition.face_encodings(img)[0]
            encodeList.append(encode)
    return encodeList


def markAttendance(name):
    with open('Attendance.csv', 'r+') as f:
        myDataList = f.readlines()
        nameList = [line.split(',')[0] for line in myDataList]

        if name not in nameList:
            now = datetime.now()
            dtString = now.strftime('%H:%M:%S')
            f.writelines(f'\n{name},{dtString}')


encodeKnown = findEncodings(images)
print('Encoding Complete')

cap = cv2.VideoCapture(0)
recognition_times = {}

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

    facesInFrame = face_recognition.face_locations(imgS)
    encodesInFrame = face_recognition.face_encodings(imgS, facesInFrame)

    for encodeFace, faceLoc in zip(encodesInFrame, facesInFrame):
        matches = face_recognition.compare_faces(encodeKnown, encodeFace)
        faceDis = face_recognition.face_distance(encodeKnown, encodeFace)
        # print(faceDis)
        matchIndex = np.argmin(faceDis)

        if matches[matchIndex] and faceDis[matchIndex] < 0.5:
            name = classNames[matchIndex].upper()
        else:
            name = 'UNKNOWN'

        y1, x2, y2, x1 = faceLoc
        y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
        cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0))
        cv2.putText(img, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)

        if name != 'UNKNOWN':
            now = datetime.now()
            if name in recognition_times:
                if now - recognition_times[name] >= timedelta(seconds=3):
                    markAttendance(name)
                    del recognition_times[name]
            else:
                recognition_times[name] = now

            # Clean up recognition times to remove outdated entries
        current_time = datetime.now()
        recognition_times = {name: time for name, time in recognition_times.items() if
                             current_time - time < timedelta(seconds=3)}

        cv2.imshow('Webcam', img)
        cv2.waitKey(1)

