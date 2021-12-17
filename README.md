# ComputerVision_OpenCV_Practice


본 프로젝트는 FASTCAMPUS의 강의 "OpenCV를 활용한 컴퓨터비전과 딥러닝 올인원 패키지 Online."을 통해 학습한 내용을 실습하는 프로젝트이다.  
개발 환경 OS는 macOS Big Sur 이며 평소에 활용하던 Colab 또는 Jupyter notebook으로 개발하려 했으나 openCV를 mac에서 활용할 때는 해당 환경에서 이미지 윈도우를 활용하기에 어려움이 있어 Pycharm으로 진행하였다.


--------------------------

## 1.chroma_key

### 결과영상
./practice_ouput/chroma_key.avi  
![chroma_key.avi](./practice_ouput/chroma_key.avi)

### 실습개요
초록색 배경을 가진 영상1과 배경으로 쓰일 영상2를 합성하여 크로마키를 구현하는 실습.  
openCV를 활용하여 영상을 읽고,  
hsv컬러 영상에서 초록색 배경을 마스크로 변경,  
영상1과 마스크, 영상2를 합성하여 크로마키 구현

### openCV 활용내역
- cv2.VideoCapture('./images/woman.mp4') : 영상을 읽음
- cap1.isOpened() : 영상을 잘 읽었는지 여부
- cap1.get(cv2.CAP_PROP_FRAME_WIDTH) : 영상의 너비 추출
- cap1.get(cv2.CAP_PROP_FRAME_HEIGHT) : 영상의 높이 추출
- cap1.get(cv2.CAP_PROP_FPS) : 영상의 fps 추출
- cv2.VideoWriter_fourcc(*'DIVX') : 영상 기록 설정
- cv2.VideoWriter('./practice_output/1.chroma_key.avi', fourcc, fps, (w,h)) : 영상 기록 설정
- cv2.resize(frame2, (w,h)) : 이미지 사이즈 변경
- cv2.cvtColor(frame1, cv2.COLOR_BGR2HSV) : 이미지 컬러 형식 변경
- cv2.inRange(hsv, (50, 150, 0), (70, 255, 255)) : 마스크 생성
- cv2.copyTo(frame2, mask, frame1) : 이미지 합성
- out.write(frame1) : 영상 기록
- cap1.release() : 이미지 메모리 해제
- cv2.destroyAllWindows() : 윈도우 종료

-------------------------------
