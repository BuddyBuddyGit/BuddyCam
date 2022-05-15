import cv2

cap = cv2.VideoCapture(1, cv2.CAP_DSHOW)
num_gray = 0
num_edge = 0
num_color = 0

print('width :%d, height : %d' % (cap.get(3), cap.get(4)))

# fourcc = cv2.VideoWriter_fourcc(*'DIVX')    # 코덱을 넘겨줌
# out = cv2.VideoWriter('save.avi', fourcc, 25.0, (640, 480))

while(cap.isOpened() == True):
    success, frame = cap.read()    # Read 결과와 frame

    if(success) :
        gray = cv2.cvtColor(frame,  cv2.COLOR_BGR2GRAY)    # 입력 받은 화면 Gray로 변환
        edge = cv2. Canny(frame, 50, 150)

        cv2.imshow('frame_color', frame)    # 컬러 화면 출력
        cv2.imshow('frame_gray', gray)    # Gray 화면 출력
        cv2.imshow('frame_edge', edge)  # 윤곽선 화면 출력

        # out.write(edge) edge 영상 저장

        num_color = num_color + 1
        cv2.imwrite('D:\BuddyBuddy\CaptureColor\cap_' + str(num_color) + '.jpg', frame, params=[cv2.IMWRITE_JPEG_QUALITY, 95])

        num_gray = num_gray + 1
        cv2.imwrite('D:\BuddyBuddy\CaptureGray\cap_' + str(num_gray) + '.jpg', gray, params=[cv2.IMWRITE_JPEG_QUALITY, 95])

        num_edge = num_edge + 1
        cv2.imwrite('D:\BuddyBuddy\CaptureEdge\cap_' + str(num_edge) + '.jpg', edge, params=[cv2.IMWRITE_JPEG_QUALITY, 95])

        if num_color >= 100 :
            num_color = 0

        if num_gray >= 100 :
            num_gray = 0

        if num_edge >= 100 :
            num_edge = 0

        key = cv2.waitKey(30) & 0xff

        if (key == 27):
            break

    else :
        break

cap.release()
cv2.destroyAllWindows()