import cv2
import subprocess
from flask import Flask,render_template,request
import requests
import cv2
import numpy as np
import imutils
from PIL import Image
import os
import base64
from io import BytesIO


# Define the folder to store captured images
image_folder = "D:/Computer_science/BE_PROJECT/Seed_Project/"

# Create the folder if it doesn't exist
if not os.path.exists(image_folder):
    os.makedirs(image_folder)

# Initialize the variable to store the captured image
captured_image = None

app = Flask(__name__)
# Define the custom filter
def pil_to_base64(image):
    buffered = BytesIO()
    image.save(buffered, format="JPEG")
    return base64.b64encode(buffered.getvalue()).decode('utf-8')

# Register the custom filter
app.jinja_env.filters['pil_to_base64'] = pil_to_base64

@app.route('/')
def homePage():
    return render_template('index.html')

@app.route("/openwebcam",methods = ["POST"])
def predict_datapoint():

    # Replace the below URL with your own. Make sure to add "/shot.jpg" at last.
    # url = "http://192.168.1.2:8080/shot.jpg"

    # while True:
    #     # Fetching data from the URL
    #     img_resp = requests.get(url)
    #     img_arr = np.array(bytearray(img_resp.content), dtype=np.uint8)
    #     img = cv2.imdecode(img_arr, -1)
    #     img = imutils.resize(img, width=1000, height=1800)

    #     # Display the image
    #     cv2.imshow("Android_cam", img)

    #     # Press 's' to capture a snapshot
    #     key = cv2.waitKey(1)
    #     if key == ord('s'):
    #         cv2.imwrite("seedTestImage1.Jpeg", img)
    #         # Convert the captured image to RGB format (Pillow uses RGB)
    #         captured_image = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    #         print("Snapshot taken!")

    #     # Press 'Esc' key to exit
    #     elif key == 27:
    #         break

    # # Release the OpenCV window
    # cv2.destroyAllWindows()

    # BELOW CODE TO OPEN WEBCAM OF LAPTOP
    cam = cv2.VideoCapture(1)
    while True:
        ret,frame = cam.read()

        if not ret:
            print('failed to grab frame')
            break

        cv2.imshow('test',frame)

        k = cv2.waitKey(1)

        if k %256 == 27:
            print('Escaped this, closing the app')
            break
        elif k%256 == 32:
            # Convert the captured image to RGB format (Pillow uses RGB)
            captured_image = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            
            # Save the captured image to the specified folder
            img_name = os.path.join(image_folder, f"seedTestImage1.png")
            captured_image.save(img_name)
            img_name = os.path.join(image_folder, f"seedTestImage1.png")
            captured_image.save(img_name)
            print('Screenshot taken')
    cam.release()

    cv2.destroyAllWindows()
    return render_template('displayImage.html',captured_image=captured_image)

@app.route("/RunningMacros",methods = ["POST"])
def run_macros():
    # Note the macros is running on seedTestImage, and we saving seedTestImage1 for now just checking
    # remember once everything complited remove the 1 from seedTestImage1 so we can save properly in seedTestImage and run macros on it
    imagej_path = "D:\Computer_science\BE_PROJECT\Seed_Project\imageJ software\ImageJ\ImageJ.exe"

    subprocess.run([imagej_path])
    return render_template('dataCollected.html')

if __name__ == '__main__':
    app.run(host='127.0.0.1',port=5000)