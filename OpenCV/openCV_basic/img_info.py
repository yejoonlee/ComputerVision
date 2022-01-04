import sys
import cv2


# 영상 불러오기
img_path = "../images/restingplace.JPG"
img1 = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread(img_path, cv2.IMREAD_COLOR)

if img1 is None or img2 is None:
    print('Image load failed!')
    sys.exit()

# 영상의 속성 참조
print('type(img1):', type(img1))
print('img1.shape:', img1.shape)
print('img2.shape:', img2.shape)
print('img1.dtype:', img1.dtype)

# 영상의 크기 참조
h, w = img2.shape[:2]
print(f'img2 size: {w} x {h}')

if len(img1.shape) == 2:
    print('img1 is a grayscale image')
elif len(img1.shape) == 3:
    print('img1 is a truecolor image')

cv2.imshow('img1', img1)
cv2.waitKey()
cv2.imshow('img2', img2)
cv2.waitKey()

# 영상의 픽셀 값 참조
for y in range(h):
    for x in range(w):
        img1[y, x] = 255
        img2[y, x] = (255, 0, 255)

# img1[:,:] = 255
# img2[:,:] = (0, 0, 255)

cv2.imshow('img1', img1)
cv2.waitKey()
cv2.imshow('img2', img2)
cv2.waitKey()

cv2.destroyAllWindows()
