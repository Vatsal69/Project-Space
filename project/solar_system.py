import cv2
	
# path
path = "solar-system.jpg"
	
# Reading an image in default mode
image = cv2.imread(path)
	
# Window name in which image is displayed
window_name = 'Image'

# font
font = cv2.FONT_HERSHEY_SIMPLEX


# fontScale
fontScale = 1

# Blue color in BGR
color = (255, 255, 255)

# Line thickness of 2 px
thickness = 2

# Using cv2.putText() method
image = cv2.putText(image, 'SUN', (20, 178), font,
				fontScale, color, thickness, cv2.LINE_AA)

image = cv2.putText(image, 'Mercury', (119,278), font,
				fontScale, color, thickness, cv2.LINE_AA)

image = cv2.putText(image, 'Venus', (178,178), font,
				fontScale, color, thickness, cv2.LINE_AA)

image = cv2.putText(image, 'Earth', (278,278), font,
				fontScale, color, thickness, cv2.LINE_AA)

image = cv2.putText(image, 'Mars', (384,178), font,
				fontScale, color, thickness, cv2.LINE_AA)

image = cv2.putText(image, 'Jupiter', (514,278), font,
				fontScale, color, thickness, cv2.LINE_AA)

image = cv2.putText(image, 'Saturn', (734,178), font,
				fontScale, color, thickness, cv2.LINE_AA)

image = cv2.putText(image, 'Uranus', (944,278), font,
				fontScale, color, thickness, cv2.LINE_AA)

image = cv2.putText(image, 'Neptune', (1100,178), font,
				fontScale, color, thickness, cv2.LINE_AA)

# Displaying the image
cv2.imshow(window_name, image)

cv2.waitKey(0)