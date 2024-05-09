import cv2
import numpy as np
import face_recognition

imgMom = face_recognition.load_image_file('ImagesBasics/Sushma.jpeg')
imgMom = cv2.cvtColor(imgMom, cv2.COLOR_BGR2RGB)

imgTest = face_recognition.load_image_file('ImagesBasics/Sushma_Test.jpeg')
imgTest = cv2.cvtColor(imgTest, cv2.COLOR_BGR2RGB)

faceLoc = face_recognition.face_locations(imgMom)[0]
EncodeMom = face_recognition.face_encodings(imgMom)[0]
cv2.rectangle(imgMom, (faceLoc[3],faceLoc[0]),(faceLoc[1],faceLoc[2]),(255,0,255),10)

faceTest = face_recognition.face_locations(imgTest)[0]
EncodeMomTest = face_recognition.face_encodings(imgTest)[0]
cv2.rectangle(imgTest, (faceTest[3],faceTest[0]),(faceTest[1],faceTest[2]),(255,0,255),10)

results = face_recognition.compare_faces([EncodeMom],EncodeMomTest)
faceDis = face_recognition.face_distance([EncodeMom],EncodeMomTest)
print(results, faceDis)

cv2.putText(imgTest,f'{results} {(100-round(faceDis[0],2)*100)}%',(50,200),cv2.FONT_HERSHEY_COMPLEX,5,(0,255,0),5)

cv2.imshow('Sushma', imgMom)
cv2.imshow('Sushma Test', imgTest)
cv2.waitKey(0)