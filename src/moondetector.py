import cv2
import numpy as np
import os

# Read image.
directory_name = 'test_images'
for file_name in os.listdir(directory_name):
    print(file_name)
    img = cv2.imread(directory_name+'/'+ file_name, cv2.IMREAD_COLOR)

    # Convert to grayscale.
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Blur using 3 * 3 kernel.
    gray_blurred = cv2.blur(gray, (3, 3))

    # Apply Hough transform on the blurred image.
    detected_circles = cv2.HoughCircles(gray_blurred,
                    cv2.HOUGH_GRADIENT, 1, 20, param1 = 50,
                param2 = 30, minRadius = 1, maxRadius = 500)
    # Draw circles that are detected.
    image_center_x, image_center_y = int(img.shape[1]/2), int(img.shape[0]/2)
    if detected_circles is not None:

        # Convert the circle parameters a, b and r to integers.
        detected_circles = np.uint16(np.around(detected_circles))
        
        for pt in detected_circles[0, :][:1]:
            a, b, r = pt[0], pt[1], pt[2]

            # Draw the circumference of the circle.
            cv2.circle(img, (a, b), r, (0, 255, 0), 2)
            print(r)

            # Draw a small circle (of radius 1) to show the center.
            cv2.circle(img, (a, b), 1, (0, 0, 255), 3)
            cv2.circle(img, (image_center_x, image_center_y), 1, (0, 0, 255), 3)
            cv2.line(img,(a,b),(image_center_x, image_center_y),(155, 0, ),1)
            cv2.imshow("Detected Circle", img)
            cv2.waitKey(0)
