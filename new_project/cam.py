import cv2
import time
# ------------------ 선언, 초기화 ------------#
cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
fps = 20.0
frame_size = (640, 480)
start_time = time.time()
file_count = 1
out = cv2.VideoWriter(f'output_{file_count}.avi', fourcc, fps, frame_size)

while True:
    ret, frame = cap.read()
    if not ret:
        print("nono")
        break
        
    current_time = time.time()
    
    if current_time - start_time >= 600: # 녹화시간이 600초를 넘기면 파일 넘버를 올리고 저장, 영상이 파일 넘버로 구분되도록
        out.release()
        file_count += 1
        out = cv2.VideoWriter(f'output_{file_count}.avi', fourcc, fps, frame_size) 
        start_time = current_time
    cv2.imshow("Camera", frame)
    out.write(frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
        
cap.release()
out.release()
cv2.destroyAllwindows()

