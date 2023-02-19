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

while True:
    if(keyboard.is_pressed("q")):
        pix = pyautogui.pixel(1555, 655)
        if(pix == WHITE):
            keyboard.press("m")
