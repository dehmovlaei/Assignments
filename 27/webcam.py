import cv2

cap = cv2.VideoCapture(0)
_, frame = cap.read()
rows = frame.shape[0]
cols = frame.shape[1]

writer = cv2.VideoWriter('mywebcam.MP4v', cv2.VideoWriter_fourcc(*'MJPG'), 30, (cols, rows))
while True:
    _, frame = cap.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    _, frame = cv2.threshold(frame, 75, 255, cv2.THRESH_BINARY)
    writer.write(frame)
    cv2.imshow("result", frame)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

writer.release()