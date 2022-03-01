import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime



path = 'images'
images = []
studentNames = []
rollNO = []
myList = os.listdir(path)
print(myList)


for student in myList:
    curImg = cv2.imread(f'{path}/{student}')
    images.append(curImg)
    studentNames.append(os.path.splitext(student)[0])

                   
print(studentNames)


def findEncoding(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
        # print(encodeList)
    return encodeList


print("Loading.....")
encodeListKnown = findEncoding(images)
print("Encoding Complete")


def markAttendance(name):
    timestamp = datetime.now().strftime("%d_%m_%y")
    filename = "CSE_A_" + timestamp + ".csv"

    # The function which automatically make file when the program start

    open(os.path.join(f"attendance record/{filename}"),"a")
    with open(os.path.join(f"attendance record/{filename}"),'r+') as f:
        # f.writelines("Name  ,  Date | Time\n")
    # with open('attendance.csv','r+') as f:
        myDataList = f.readlines()
        nameList = []

        for line in myDataList:
            entry = line.split(',')
            nameList.append(entry[0])
        if name not in nameList:
            now = datetime.now()
            dtString = now.strftime('%D:%M:%Y | %H:%M:%S')
            f.writelines(f'\n{name},{dtString}')
            f.close()
        else:
            msg = "Recoded"
            cv2.putText(img,msg,(250,450),cv2.FONT_HERSHEY_COMPLEX,1,(243,14,14),2)



# to open the web camera
cap = cv2.VideoCapture(0)


while True:
    success, img = cap.read() # to read the image in webcam
    
    # it will resize the image to one fourth to make the program fast
    imgS = cv2.resize(img,(0,0), None,0.25,0.25) #optional
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)


    # it will find the image location and encode it in current frame
    faceCurFrame = face_recognition.face_locations(imgS)
    encodeCurFrame = face_recognition.face_encodings(imgS,faceCurFrame)


    # two loops at once thats why we use zip
    for encodeface,faceloc in zip(encodeCurFrame, faceCurFrame):
        matches = face_recognition.compare_faces(encodeListKnown, encodeface)
        faceDis = face_recognition.face_distance(encodeListKnown, encodeface)
        # print(faceDis)
        matchIndex = np.argmin(faceDis) # for min value


        # it will print the name
        if matches[matchIndex]:
            name = studentNames[matchIndex].upper()
            # print(name)
            y1,x2,y2,x1 = faceloc
            y1,x2,y2,x1 = y1*4,x2*4,y2*4,x1*4
            cv2.rectangle(img,(x1,y1),(x2,y2),(61,249,11),2)
            cv2.rectangle(img,(x1,y2-35),(x2,y2),(61,249,11), cv2.FILLED)
            cv2.putText(img,name,(x1+6,y2-6),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
            markAttendance(name)

        if faceDis[matchIndex]< 0.50:
            name = studentNames[matchIndex].upper()
            markAttendance(name)

        else:
            name = "Unknown"
            y1,x2,y2,x1 = faceloc
            y1,x2,y2,x1 = y1*4,x2*4,y2*4,x1*4
            cv2.rectangle(img,(x1,y1),(x2,y2),(14,14,243),2)
            cv2.rectangle(img,(x1,y2-35),(x2,y2),(14,14,243), cv2.FILLED)
            cv2.putText(img,name,(x1+6,y2-6),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
            
        # else: 
        #     name = 'Unknown'
        #     #print(name)
        #     y1,x2,y2,x1 = faceLoc
        #     y1, x2, y2, x1 = y1*4,x2*4,y2*4,x1*4
        #     cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)
        #     cv2.rectangle(img,(x1,y2-35),(x2,y2),(0,255,0),cv2.FILLED)
        #     cv2.putText(img,name,(x1+6,y2-6),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)

    
    cv2.imshow('Attendance | Webcam - Diljot Singh (Press Q to exit)', img)
    if cv2.waitKey(1000) & 0xff == ord('q'):
        break

