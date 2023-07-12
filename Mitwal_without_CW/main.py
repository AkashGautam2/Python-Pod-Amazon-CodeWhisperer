import numpy as np
import cv2
import streamlit as st

st.title("Image Enhancer")
st.write("Upload an image to edit")
class ImageEnhancer:
    def __init__(self):
        pass
    def crop(self,image):
        x, y, w, h = cv2.selectROI("select the area", image, showCrosshair=False)
        cropped_image = image[y:y + h, x:x + w]
        cv2.imwrite("crop.jpg", cropped_image)
        st.image("crop.jpg")
        cv2.destroyAllWindows()
        return cropped_image
    def resize(self,image,width,height):
        img=cv2.resize(image,(int(width),int(height)))
        cv2.imwrite("resize_img.jpeg",img)
        st.image(img)
        return img,width,height
    def brightness(self,image,brightness):
        brightness_image = cv2.addWeighted(image, float(brightness), image, 0, 0)
        cv2.imwrite("brightness_image.jpg", brightness_image)
        st.image(brightness_image)
        return brightness_image
    def contrast(self,image,contrast):
        contrast_image = cv2.addWeighted(image, float(contrast), image, 0, 0)
        cv2.imwrite("brightness_image.png", contrast_image)
        #st.image(contrast_image)
        return contrast_image
    def function(self):
        uploaded_file = st.file_uploader("Choose an image...", type=['png', 'jpg', 'jpeg'])
        if uploaded_file is not None:
            image = np.array(bytearray(uploaded_file.read()), dtype=np.uint8)
            download_image = cv2.imdecode(image, cv2.IMREAD_COLOR)
            width = st.text_input("Width in pixels")
            height = st.text_input("height in pixels")
            if st.button("Resize"):
                if (width and height):
                    if (width.isdigit() and height.isdigit()):
                        # Call the function resize_image
                        self.resize(download_image, width, height)
                    else:
                        st.warning("Please enter numeric value")
                else:
                    st.warning("Invalid Input")
            brightness = st.text_input("Brightness in Percentage")
            if st.button("Brightness"):
                if (brightness):
                    if (brightness.isdigit()):
                        self.brightness(image, int(brightness))
                    else:
                        st.warning("Please enter numeric value")
                else:
                    st.warning("Invalid Input")
            contrast = st.text_input("Contrast in Percentage")
            if st.button("Contrast"):
                if (contrast):
                    if (contrast.isdigit()):
                        self.contrast(image, int(contrast))
                    else:
                        st.warning("Please enter numeric value")
                else:
                    st.warning("Invalid Input")
            if st.button("Crop"):
                self.crop(download_image)

imgObj=ImageEnhancer()
imgObj.function()
