import cv2
import subprocess
from flask import Flask,render_template,request
import requests
import cv2
import numpy as np
import imutils

app = Flask(__name__)

@app.route('/')
def homePage():
    return render_template('index.html')

@app.route("/openwebcam",methods = ["POST"])
def predict_datapoint():

    # Replace the below URL with your own. Make sure to add "/shot.jpg" at last.
    url = "http://192.168.1.4:8080/shot.jpg"

    while True:
        # Fetching data from the URL
        img_resp = requests.get(url)
        img_arr = np.array(bytearray(img_resp.content), dtype=np.uint8)
        img = cv2.imdecode(img_arr, -1)
        img = imutils.resize(img, width=1000, height=1800)

        # Display the image
        cv2.imshow("Android_cam", img)

        # Press 's' to capture a snapshot
        key = cv2.waitKey(1)
        if key == ord('s'):
            cv2.imwrite("snapshot.jpg", img)
            print("Snapshot taken!")

        # Press 'Esc' key to exit
        elif key == 27:
            break

    # Release the OpenCV window
    cv2.destroyAllWindows()

    # BELOW CODE TO OPEN WEBCAM OF LAPTOP

    # cam = cv2.VideoCapture(0)

    # # cv2.namedWindow("python webcam screenshot App")

    # image_counter = 0

    # while True:
    #     ret,frame = cam.read()

    #     if not ret:
    #         print('failed to grab frame')
    #         break

    #     cv2.imshow('test',frame)

    #     k = cv2.waitKey(1)

    #     if k %256 == 27:
    #         print('Escaped this, closing the app')
    #         break
    #     elif k%256 == 32:
    #         img_name = './seedTestImage1.JPEG'
    #         cv2.imwrite(img_name,frame)
    #         print('Screenshot taken')
    #         image_counter = image_counter + 1
    # cam.release()

    # cv2.destroyAllWindows()
    return render_template('displayImage.html')

@app.route("/RunningMacros",methods = ["POST"])
def run_macros():
    # Note the macros is running on seedTestImage, and we saving seedTestImage1 for now just checking
    # remember once everything complited remove the 1 from seedTestImage1 so we can save properly in seedTestImage and run macros on it
    imagej_path = "D:\Computer_science\BE_PROJECT\Seed_Project\imageJ software\ImageJ\ImageJ.exe"

    subprocess.run([imagej_path])
    return render_template('dataCollected.html')

if __name__ == '__main__':
    app.run(host='127.0.0.1',port=5000)