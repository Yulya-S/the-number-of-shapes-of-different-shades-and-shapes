from skimage.measure import label, regionprops
import cv2

img = cv2.imread("balls_and_rects.png")
img2 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img3 = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

_, thresh = cv2.threshold(img2, 128, 192, cv2.THRESH_OTSU)
img2 = label(thresh)
regions = regionprops(img2)

rects = 0
circles = 0
colors = {}

for i in regions:
    if img3[int(i.centroid[0]), int(i.centroid[1])][0] not in colors.keys():
        colors[img3[int(i.centroid[0]), int(i.centroid[1])][0]] = [0, 0]
    if i.image.mean() == 1:
        rects += 1
        colors[img3[int(i.centroid[0]), int(i.centroid[1])][0]][0] += 1
    else:
        circles += 1
        colors[img3[int(i.centroid[0]), int(i.centroid[1])][0]][1] += 1

print(f"rects: {rects}")
print(f"circles: {circles}")
print()
for i in colors.keys():
    print(f"{i}\t-> rects: {colors[i][0]}, circles: {colors[i][1]}")

