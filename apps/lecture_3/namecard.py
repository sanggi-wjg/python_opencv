import sys
import numpy as np
import cv2


def reorderPts(pts):
    idx = np.lexsort((pts[:, 1], pts[:, 0]))  # 칼럼0 -> 칼럼1 순으로 정렬한 인덱스를 반환
    pts = pts[idx]  # x좌표로 정렬

    if pts[0, 1] > pts[1, 1]:
        pts[[0, 1]] = pts[[1, 0]]

    if pts[2, 1] < pts[3, 1]:
        pts[[2, 3]] = pts[[3, 2]]

    return pts


# 영상 불러오기
src = cv2.imread(filename = 'files/namecard1.jpg')
if src is None:
    print('Image load failed')

    sys.exit()

# 입력 영상 전처리
src_gray = cv2.cvtColor(src = src, code = cv2.COLOR_BGR2GRAY)
# _, src_bin = cv2.threshold(src, thresh = 130, maxval = 255, type = cv2.THRESH_BINARY)
ths, src_bin = cv2.threshold(src = src_gray, thresh = 0, maxval = 255, type = cv2.THRESH_BINARY | cv2.THRESH_OTSU)
print('Threshold:', ths)

# 외곽선 검출 및 명함 검출
contours, hierarchy = cv2.findContours(image = src_bin, mode = cv2.RETR_EXTERNAL, method = cv2.CHAIN_APPROX_NONE)

for pts in contours:
    # 작은 객체는 제외
    if cv2.contourArea(contour = pts) < 10:
        continue

    # 외곽선 근사화
    approx = cv2.approxPolyDP(curve = pts, epsilon = cv2.arcLength(pts, True) * 0.02, closed = True)
    if len(approx) != 4:
        continue

    cv2.polylines(img = src, pts = pts, isClosed = True, color = (0, 0, 255))
    src_quad = reorderPts(approx.reshape(4, 2).astype(np.float32))

    pers = cv2.getPerspectiveTransform(src_quad, dst_quad)

# Show
cv2.imshow(winname = 'src', mat = src)
cv2.imshow(winname = 'src_gray', mat = src_gray)
cv2.imshow(winname = 'src_bin', mat = src_bin)

while True:
    if cv2.waitKey(delay = 1) == 27:
        break

cv2.destroyAllWindows()
