#Import Libraries
import numpy as np
import cv2
import streamlit as st
#Create a title
st.title("Image Enhancer")
#Create sub title
st.write("Upload an image to edit")
#Create a Class named ImageEnhancer.
class ImageEnhancer:
    def __init__(self):
        pass
    #Write a function to crop image
    def crop(self,image):
        x, y, w, h = cv2.selectROI("select the area", image, showCrosshair=False)
        cropped_image = image[y:y + h, x:x + w]
        cv2.imwrite("crop.jpg", cropped_image)
        st.image("crop.jpg")
        cv2.destroyAllWindows()
        return cropped_image
    #Write a function to resize image
    def resize(self,image,width,height):
        img=cv2.resize(image,(int(width),int(height)))
        cv2.imwrite("resize_img.jpeg",img)
        st.image(img)
        return img,width,height
    #Write a function to increase brightness of image
    def brightness_increase(self,image,brightness_perct):
        brightness_image = cv2.addWeighted(image, float(brightness_perct), image,0,0)
        cv2.imwrite("brightness_image2.jpeg", brightness_image)
        st.image(brightness_image)
        return brightness_image
    #Write a function to contrast image
    def contrast(self,image,contrast):
        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        h, s, v = cv2.split(hsv)
        lim = contrast
        v[v > lim] -= contrast
        v[v <= lim] = 0
        final_hsv = cv2.merge((h, s, v))
        final_img = cv2.cvtColor(final_hsv, cv2.COLOR_HSV2BGR)
        st.image("contrast.jpg")
        cv2.imwrite("contrast.jpg", final_img)
        return final_img
    def function(self):
        uploaded_file = st.file_uploader("Choose an image...", type=['png', 'jpg', 'jpeg'])
        if uploaded_file is not None:
            image = np.array(bytearray(uploaded_file.read()), dtype=np.uint8)
            download_image = cv2.imdecode(image, cv2.IMREAD_COLOR)
            #Take input for width and height of resized image
            width = st.text_input("Width in pixels")
            height = st.text_input("height in pixels")
            #Write resize button and it's functionality
            if st.button("Resize"):
                if (width and height):
                    if (width.isdigit() and height.isdigit()):
                        self.resize(download_image, width, height)
                    else:
                        st.warning("Please enter numeric value")
                else:
                    st.warning("Invalid Input")
            #Take input for brightness in percentage
            brightness = st.text_input("Brightness in Percentage")
            # Write brightness button and it's functionality
            if st.button("Brightness"):
                if (brightness):
                    if (brightness.isdigit()):
                        self.brightness_increase(image, int(brightness))
                    else:
                        st.warning("Please enter numeric value")
                else:
                    st.warning("Invalid Input")
            #Take input for contrast in percentage
            contrast = st.text_input("Contrast in Percentage")
            # Write contrast button and it's functionality
            if st.button("Contrast"):
                if (contrast):
                    if (contrast.isdigit()):
                        self.contrast(image, int(contrast))
                    else:
                        st.warning("Please enter numeric value")
                else:
                    st.warning("Invalid Input")
            # Write crop button and it's functionality
            if st.button("Crop"):
                self.crop(download_image)
#Create an object for ImageEnhancer
imgObj=ImageEnhancer()
# Call default function from object
imgObj.function()
