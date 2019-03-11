"""
Computer Vision Course.
Example 1: Read and show an image.

Author: Cristiano Fraga G. Nunes
E-mail: <cfgnunes@gmail.com>
"""

import cv2

# Read an image
img1 = cv2.imread("lena.jpg")

# Show the image in a window
cv2.imshow("Window title", img1)

# Pause the application until any key is pressed
cv2.waitKey(0)

# Close all windows
cv2.destroyAllWindows()
