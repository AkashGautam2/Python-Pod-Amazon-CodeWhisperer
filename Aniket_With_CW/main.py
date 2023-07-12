import streamlit as st
#import image processing library
from PIL import Image
#import opencv library
import cv2
import numpy as np

#create streamlit title
st.title("Image Processing App")

#create a class named ImageProcessor
class ImageProcessor:

    #create function named crop
    def crop(self, image):
        #create a selectroi from opencv
        roi = cv2.selectROI("Image", image, showCrosshair=False)
        #create a cropped image
        cropped_image = image[int(roi[1]):int(roi[1]+roi[3]), int(roi[0]):int(roi[0]+roi[2])]
        #display the cropped image
        st.image(cropped_image, caption="Cropped Image", use_column_width=True)
        #save the cropped image
        cv2.imwrite("cropped_image.jpg", cropped_image)
        #destroy all windows
        cv2.destroyAllWindows()
        #retrun cropped image
        return cropped_image

    #create a function named Resize
    def Resize(self, image, Width, Height):
        #create a resized image
        resized_image = cv2.resize(image, (int(Width), int(Height)))
        #save the resized image
        cv2.imwrite("resized_image.jpg", resized_image)
        #return resized image
        return [resized_image,Width,Height]

    #create a function named Brightness
    def Brightness(self, image, brightness):
        #create a brightness image
        brightness_image = cv2.addWeighted(image, float(brightness), image, 0, 0)
        #save the brightness image
        cv2.imwrite("brightness_image.jpg", brightness_image)
        #return brightness image
        return brightness_image

    #create a function named contrast
    def contrast(self, image, contrast):
        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        h, s, v = cv2.split(hsv)
        lim = 0 + contrast
        v[v < lim] = 0
        v[v >= lim] -= contrast
        final_hsv = cv2.merge((h, s, v))
        img = cv2.cvtColor(final_hsv, cv2.COLOR_HSV2BGR)
        cv2.imwrite("contrast.jpg", img)
        st.image("contrast.jpg")

    #create a function named process
    def process(self):
        #create a file uploader
        file = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])
        if file is not None:
            file = file.read()
            np_array = np.frombuffer(file, np.uint8)
            image = cv2.imdecode(np_array, cv2.IMREAD_COLOR)
            #display the image
            st.image(file, caption="Uploaded Image", use_column_width=True)
            #craate a streamlit button
            if st.button("Crop"):
                #call function crop()
                self.crop(image)
            #create a text input named width
            Width = st.text_input("Width")
            #create a text input named height
            Height = st.text_input("Height")
            #create a button for resizing
            if st.button("Resize"):
                if (Width and Height):
                    if (Width.isdigit() and Height.isdigit()):
                        self.Resize(image, Width, Height)
                    else:
                        st.warning("Please enter numeric value")
                else:
                    st.warning("Invalid Input")
                #call function resize()
                self.Resize(image, Width, Height)
            #create a text input named brightness
            brightness = st.text_input("Brightness")
            #create a button with name brightness
            if st.button("Brightness"):
                #check if brightness
                if (brightness):
                    #call function brightness()
                    self.Brightness(image, brightness)
            # create a text input named contrast
            contrast = st.text_input("contrast")
            # create a button with name contrast
            if st.button("contrast"):
                # check if contrast
                    if (contrast):
                        # call function contrast()
                        self.contrast(image, int(contrast))

#create a object of class ImageProcessor
processor = ImageProcessor()
#call the method process()
processor.process()