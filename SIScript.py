import pyautogui, sys
import keyboard


# --- Координаты пикселя под курсором ---
# try:
#     while True:
#         x, y = pyautogui.position()
#         positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
#         print(positionStr),
#         print('\b' * (len(positionStr) + 2)),
#         sys.stdout.flush()
# except KeyboardInterrupt:
#     print('\n')

# --- цвет в RGB на определенном пикселе ---
# while True:
#     pix = pyautogui.pixel(1555, 655)
#     print(pix)

WHITE = (255, 255, 255)

# Когда нужно ответить как можно быстрее, необходимо зажать кнопку "q" на клавиатуре и как только появится белая рамка
# нажмется автоматически кнопка "m" (Перед этим всем, необходимо перебиндить в настройках кнопку "Right Ctrl" на "m" для ответа)
while True:
    if(keyboard.is_pressed("q")):
        pix = pyautogui.pixel(1555, 655)
        if(pix == WHITE):
            keyboard.press("m")
