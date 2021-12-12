import matplotlib.pyplot as plt
import cv2

imgPath = "../images/restingplace.JPG"

# 컬러 영상 출력
imgBGR = cv2.imread(imgPath)
imgRGB = cv2.cvtColor(imgBGR, cv2.COLOR_BGR2RGB)

plt.axis('off')
plt.imshow(imgRGB)
plt.show()

# 그레이스케일 영상 출력
imgGray = cv2.imread(imgPath, cv2.IMREAD_GRAYSCALE)

plt.axis('off')
plt.imshow(imgGray, cmap='gray')
plt.show()

# 두 개의 영상을 함께 출력
plt.subplot(121), plt.axis('off'), plt.imshow(imgRGB)
plt.subplot(122), plt.axis('off'), plt.imshow(imgGray, cmap='gray')
plt.show()

# # 전체 화면으로 'image' 창 생성
cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.setWindowProperty('image', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
img = cv2.imread(imgPath)

if img is None:
    print('Image load failed!')

cv2.imshow('image', img)
cv2.waitKey()
cv2.destroyAllWindows()