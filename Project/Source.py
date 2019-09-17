import cv2

imageColor = cv2.imread('Resources/Untitled111.png', cv2.IMREAD_ANYCOLOR)
imageGrayScale = cv2.imread('Resources/Untitled111.png', cv2.IMREAD_GRAYSCALE)
threshold = cv2.adaptiveThreshold(imageGrayScale, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 5, 9)
_, contours, _ = cv2.findContours(threshold, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
# Finds the Contours of a binary image by [Suzuki85]#

for cnt in contours:
    approx = cv2.approxPolyDP(cnt, 0.010 * cv2.arcLength(cnt, True), True)
    #calculates the curves of specific shape with the contours Points and Specific epsilon that bpunded to the arc+
    if len(approx) == 3:
        cv2.drawContours(imageColor, [cnt], 0, (0, 0, 255), -1) #Red
    elif len(approx) == 4:
        cv2.drawContours(imageColor, [cnt], 0, (255, 0, 0), -1) #Blue
    elif len(approx) == 5:
        cv2.drawContours(imageColor, [cnt], 0, (100, 100, 30), -1)#Kahki-Green
    elif len(approx) == 6:
        cv2.drawContours(imageColor, [cnt], 0, (120, 10, 100), -1)#Purple
    elif len(approx) > 10:
        cv2.drawContours(imageColor, [cnt], 0, (0, 255, 0), -1) #Green


#cv2.imshow("Untitled", imageGrayScale)
#cv2.imshow("threshold", threshold)
cv2.imshow("imageColor", imageColor)
cv2.waitKey(0)
cv2.destroyAllWindows()
