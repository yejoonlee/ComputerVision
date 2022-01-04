import numpy as np
import cv2

# 가로 세로 400 크기인 컬러 화면을 흰색으로 체워서 생성
img = np.full((400, 400, 3), 255, np.uint8)

# 선을 그릴 때: 그릴 이미지, 시작점, 끝점, 색상, 두께
cv2.line(img, (50, 50), (200, 50), (0, 0, 255), 5)
cv2.line(img, (50, 60), (150, 160), (0, 0, 128), 3)

# 사각형을 그릴 때: 그릴 이미지, (좌상단 점과 해당 점부터 우하단의 상대위치) 또는 (좌상단 점, 우하단 점), 색상, 두께(음수면 속을 체움)
cv2.rectangle(img, (50, 200, 150, 100), (0, 255, 0), 2)
cv2.rectangle(img, (70, 220), (180, 280), (0, 128, 0), -2)

# 원을 그릴 때: 그릴 이미지, 중심, 반지름, 색상, 두께(음수면 속을 체움), 선 종류
cv2.circle(img, (300, 100), 30, (255, 255, 0), -1, cv2.LINE_AA)
cv2.circle(img, (300, 100), 60, (255, 0, 0), 3, cv2.LINE_AA)

# 원하는 다각형을 그리고자 할 때: 그릴 이미지, 모든 점을 정의한 리스트, True(?), 색상, 두께(음수 넣으면 에러)
pts = np.array([[250, 200], [300, 200], [350, 300], [250, 300], [350, 350]])
cv2.polylines(img, [pts], True, (255, 0, 255), 3)

# 글자를 넣을 때: 그릴 이미지, 쓸 문자열, 좌상단 좌표, 폰트, 크기, 색상, 두께, 선 종류
text = 'Hello? OpenCV ' + cv2.__version__
cv2.putText(img, text, (50, 350), cv2.FONT_HERSHEY_SIMPLEX, 0.8,
            (0, 0, 255), 1, cv2.LINE_AA)

cv2.imshow("img", img)
cv2.waitKey()
cv2.destroyAllWindows()