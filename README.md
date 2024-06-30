# Face-Recognition-Attendance-System

## Table of Contents
- [Overview](#overview)
- [Built With](#built-with)
- [Features](#features)
- [Contact](#contact)

## Overview
This project is an attempt to modernise the current attendance taking practices in several organisations.
<br>
Before starting with the project I would like to divide the whole project into two parts:<br>
    1. The 'Basics.py' file and the 'ImageBasics' folder as one entity and,<br>
    2. The 'Attendance.py', 'Attendance.csv' files along with the 'Students' folder as another.<br>
<br>
The first entity matches a particular person in any two photos using Linear Support Vector Machine Classifier.<br>
The file contains the code where as the folder contains the images of both 'to be trained' ones as well as the 'to be matced' ones.<br>
It does so in the following manner:<br>
      1. Load a training face image of a kown person.<br>
      2. Load another picture of the same known person.<br>
      3. Encode both the pictures using Histogram of Gradients (HOG).<br>
      4. Calculate the 128 measurements and pass them through the trained model.<br>
      5. Then find the Euclidean Distance and if the value is less than a threshold value the face is a match.<br>
<br>
The second part of the project is the main deal which captures the faces from your webcam and upon enouuntering a match updates the attendance. The file 'Attendance.py' contains the code, where as the folder 'Students' contains the images of the students of whose faces are to be matched. The 'Attendance.csv' file acts as an attendance sheet marking the attendance of the students whose faces have been matched.<br>
<br>
The general skeleton of this entity remains the same, except for a given change i.e. the second point changes as the faces are captured live with the help of the OpenCV library.
Also, lastly a part is also added where the csv is updated on matching a face from the database.
<br>

### Built With
1. Dlib<br>
2. face-recognition<br>
3. OpenCV<br>
4. SVM<br>

## Features
1. Histogram of Gradients (HOG) marks 128 landmarks on the face.<br>
2. The system identifies the face in the frame by finding the least Euclidean distance in 128 dimentional space of the encoded faces in the database.<br>
3. Once a face is identified, it registers the attendance in a CSV file along with the time of identification.<br>
4. To avoid redundancy, the time gets updated only after 24 hours for repeated identifications.<br>
5. In case a new face is captured, the model labels it as UNKNOWN and does not enter it in the attendance log.<br>
6. Another feature to increase the robustness is that once a name is recognised it should remain the same for atleast 3 seconds for it to be entered in the attendance log.<br>

## Contact
E-mail: savitraj81597@gmail.com<br>
Linkedin: www.linkedin.com/in/savit-raj<br>
Webpage: https://savit-raj.github.io/Portfolio/<br>


