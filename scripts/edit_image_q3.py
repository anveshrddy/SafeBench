import cv2
import numpy as np
# Load the image
image = cv2.imread(r"C:\\24784\\c2\\SafeBench\\safebench\\scenario\\scenario_data\\template_od\\stopsign.jpg")

# # add rectangular patch with rotation from 0 to 90 degree to the image in specified location using opencv
# # angle should be part of saved image name
# for i in range(0, 90, 10):
#     image = cv2.rectangle(image_path, (210, 210), (410, 410), (0, 255, 255), -1)
#     cv2.imwrite("C:\\24784\\c2\\SafeBench\\safebench\\scenario\\scenario_data\\template_od\\stopsign_q3_" + str(i) + ".jpg", image)
    
#     import cv2

img = image

# Define the rotated rectangle properties
center = (100, 100) # x, y coordinates of the center
size = (50, 100) # width, height
angle = 30 # rotation angle in degrees, positive values mean counter-clockwise rotation

# Create a mask for the rotated rectangle
mask = np.zeros_like(img, dtype=np.uint8)
rotated_rect = cv2.RotatedRect(center, size, angle)
box = np.int0(cv2.boxPoints(rotated_rect))
cv2.drawContours(mask, [box], 0, (0, 255, 255), -1)

# Fill the rotated rectangle with a color
color = (0, 0, 255) # BGR color, e.g., red
patch = np.zeros_like(img, dtype=np.uint8)
patch[mask == 255] = color

# Add the rotated rectangle to the original image
result = cv2.addWeighted(img, 1, patch, 1, 0)

# Save the resulting image
# output_path = 'path/to/output/image.jpg'
# cv2.imwrite(output_path, result)


# Display the result
cv2.imwrite("C:\\24784\\c2\\SafeBench\\safebench\\scenario\\scenario_data\\template_od\\stopsign_q3_cg" + str(30) + ".jpg", result)

    
    
