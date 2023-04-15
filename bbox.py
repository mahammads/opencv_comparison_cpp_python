import cv2
import os
import time

def get_box_python(input_file):
    img = cv2.imread(input_file)

    # Convert the image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply thresholding to preprocess the image
    ret, thresh1 = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV)

    rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (25, 25))

    dilation = cv2.dilate(thresh1, rect_kernel, iterations=1)
    # Find contours in the image
    contours, hierarchy = cv2.findContours(dilation, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # Loop through each contour and draw a bounding box
    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)

        # Draw the bounding box on the image
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
        
    file_name = os.path.basename(input_file)
    folder_name = os.path.dirname(input_file)
    output_f_name = os.path.join(folder_name,"Bbox_"+file_name)

    cv2.imwrite(output_f_name, img)

if __name__ == "__main__":
    st_time = time.time()
    path = r"C:\Users\sarwa\Documents\text_extract_cpp\images"
    for file in os.listdir(path):
        fulpath = os.path.join(path, file)
        get_box_python(fulpath)
    end_time = time.time()
    total_time = end_time-st_time
    print(f"total time taken to process: {total_time}")