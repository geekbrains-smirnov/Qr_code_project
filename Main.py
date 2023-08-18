import cv2
import numpy as np
import pyzbar.pyzbar as nn

# Создание объекта VideoCapture для захвата видеопотока
cam = cv2.VideoCapture('rtsp://admin:313363zxc@192.168.1.14/:554/ISAPI/Streaming/Channels/101')

# Создание пустого изображения для вывода QR-кода и текста
image = np.zeros((200, 1800, 3), np.uint8)  # Исправлено на 3 канала (цветное изображение)
text = ''
cv2.namedWindow('QR code', cv2.WINDOW_NORMAL)

while True:
    image = np.zeros((200, 1800, 1), np.uint8)
    ret, frame = cam.read()
    if ret == True:
        if frame is not None:
            try:
                decode = nn.decode(frame)
                for i in decode:
                    text = "QR code cam: " + i.data.decode('utf-8') + '\n'
            except BaseException:
                continue

        font = cv2.FONT_HERSHEY_COMPLEX
        cv2.putText(image, text, (50, 100), font, 1, (255, 500, 255), 1)
        cv2.imshow('Qr code', image)
        cv2.setWindowProperty('Qr code', cv2.WND_PROP_TOPMOST, 1)  # Установка окна поверх всех

    if cv2.waitKey(1) == ord('q'):
        break
cam.release()
cv2.destroyAllWindows()

