import cv2

# Load the image
image_path = cv2.imread(r"C:\\24784\\c2\\SafeBench\\safebench\\scenario\\scenario_data\\template_od\\stopsign.jpg")


# Add rectanglular patch to the image in specified location using opencv with gradient fill yellow color
image = cv2.rectangle(image_path, (210, 210), (410, 410), (0, 255, 255), -1)

# save the image in specified folder
cv2.imwrite("C:\\24784\\c2\\SafeBench\\safebench\\scenario\\scenario_data\\template_od\\stopsign_q2.jpg", image)

