#Import Libraries
import streamlit as st
import cv2
import numpy as np
#Create a title and sub title
st.title("Image Enhancer")
st.write("Upload an image to see the enhanced image.")
#Create a Class named ImageEnhancer.
class ImageEnhancer:
    def __init__(self):
        pass
#Write a function to resize image which takes input as image, width and height and returns width, height and resized image
    def resize_image(self,image, width, height):
        resized_image = cv2.resize(image, (int(width), int(height)))
        cv2.imwrite("resize.jpg", resized_image)
        #show resized image
        st.image("resize.jpg")
        return [resized_image,int(width),int(height)]
    #Write a function to crop an image where user will select crop area using select ROI,take input as image and return cropped image
    def crop_image(self,image):
        x,y,w,h = cv2.selectROI("select the area",image,showCrosshair=False)
        cropped_image = image[y:y+h, x:x+w]
        cv2.imwrite("crop.jpg", cropped_image)
        #show cropped image
        st.image("crop.jpg")
        #Close all windows
        cv2.destroyAllWindows()
        return cropped_image
    #Write a function that will take input image and percentage and increase the brightness of image with that percentage
    def brightness_increase(self,image, percentage=30):
        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        h, s, v = cv2.split(hsv)
        lim = 255 - percentage
        v[v > lim] = 255
        v[v <= lim] += percentage
        final_hsv = cv2.merge((h, s, v))
        final_img = cv2.cvtColor(final_hsv, cv2.COLOR_HSV2BGR)
        # show brightness increased image
        st.image("brightness.jpg")
        cv2.imwrite("brightness.jpg", final_img)
        return final_img
    #Write a function that will take input image and percentage and decrease the brightness of image with that percentage
    def brightness_decrease(self,image, percentage=30):
        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        h, s, v = cv2.split(hsv)
        lim = percentage
        v[v > lim] -= percentage
        v[v <= lim] = 0
        final_hsv = cv2.merge((h, s, v))
        final_img = cv2.cvtColor(final_hsv, cv2.COLOR_HSV2BGR)
        #show contrast image
        st.image("contrast.jpg")
        cv2.imwrite("contrast.jpg", final_img)
        return final_img
    #Write a function to remove background using masking, take input as image and return image with background removed
    def remove_background(self,image):
        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        lower_red = np.array([0, 0, 0])
        upper_red = np.array([0, 0, 0])
        mask = cv2.inRange(hsv, lower_red, upper_red)
        res = cv2.bitwise_and(image, image, mask=mask)
        cv2.imwrite("remove_background.jpg", res)
        return res
    def default(self):
        uploaded_file = st.file_uploader("Choose an image...", type=['png', 'jpg', 'jpeg'])
        if uploaded_file is not None:
            image = np.array(bytearray(uploaded_file.read()), dtype=np.uint8)
            download_image = cv2.imdecode(image,  cv2.IMREAD_COLOR)
    #Create variables as width and take input as text
            width = st.text_input("Enter the width in pixel")
    # Create variables as height and take input as text
            height = st.text_input("Enter the height in pixel")
    #Create a button named resize
            if st.button("Resize"):
                if (width and height):
                    if (width.isdigit() and height.isdigit()):
#Call the function resize_image
                        self.resize_image(download_image, width, height)
                    else:
                        st.warning("Please enter numeric value")
                else:
                    st.warning("Invalid Input")
    #Create button named crop
            if st.button("Crop"):
                self.crop_image(download_image)
            # Create variables as brightness and take input as text
            brightness = st.text_input("Brightness in Percentage")
            # Create button named brightness
            if st.button("Brightness"):
                self.brightness_increase(download_image, int(brightness))
            # Create variables as brightness and take input as text
            contrast = st.text_input("Contrast in Percentage")
            # Create button named contrast
            if st.button("Contrast"):
                self.brightness_decrease(download_image, int(contrast))

#Create an object for ImageEnhancer and call default function
obj=ImageEnhancer()
obj.default()