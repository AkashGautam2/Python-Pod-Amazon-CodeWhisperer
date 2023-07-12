import streamlit as st
import numpy as np
import cv2

#add title for streamlit page
st.title("Image")
#write on page
st.write("Upload the Image")

#creating class for test file
class Image:
    #crop function
    def crop(self, image):
        #Function to select region of interest
        r = cv2.selectROI("Image", image, showCrosshair=False)
        #image cropped
        cropped_image = image[int(r[1]):int(r[1]+r[3]), int(r[0]):int(r[0]+r[2])]
        #show image
        st.image(cropped_image, caption="Cropped Image", use_column_width=True)
        #saving image
        cv2.imwrite("Cropped.jpg", cropped_image)
        #destroy all the opencv windows
        cv2.destroyAllWindows()
        return cropped_image
    def resize(self, image, width, height):
        #resize the image
        resized_image = cv2.resize(image, (int(width), int(height)))
        #saving image
        cv2.imwrite("resized_image.jpg", resized_image)
        return [resized_image,width,height]
    def Brightness(self, image, brightness):
        #increase brightness of image by brightness
        brightness_image = cv2.addWeighted(image, float(brightness), image, 0, 0)
        #saving image
        cv2.imwrite("brightness_image.jpg", brightness_image)
        return brightness_image
    def contrast(self, image, contrast):
        #convert into opencv color
        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        h, s, v = cv2.split(hsv)
        lim = 0 + contrast
        v[v < lim] = 0
        v[v >= lim] -= contrast
        final_hsv = cv2.merge((h, s, v))
        img = cv2.cvtColor(final_hsv, cv2.COLOR_HSV2BGR)
        #saving image
        cv2.imwrite("contrast.jpg", img)
        st.image("contrast.jpg")
    def Edit(self):
        #file uploader widget
        file = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])
        if file is not None:
            #read the file
            file = file.read()
            image = cv2.imdecode(np.frombuffer(file, np.uint8), cv2.IMREAD_COLOR)
            #if button crop clicked
            if st.button("Crop"):
                self.crop(image)
            #Get the width and height
            width = st.text_input("width")
            height = st.text_input("height")
            if st.button("resize"):
                #checking if width and height are there
                if (width and height):
                        self.resize(image, width, height)
                else:
                    #showing warning
                    st.warning("Invalid Input")
            brightness = st.text_input("Brightness")
            if st.button("Brightness"):
                if (brightness):
                    self.Brightness(image, brightness)
            contrast = st.text_input("contrast")
            if st.button("contrast"):
                    if (contrast):
                        self.contrast(image, int(contrast))

Editor = Image()
Editor.Edit()