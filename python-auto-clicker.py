import pyautogui
import time
import keyboard

time.sleep(1)

print("Before going any further, it is recommened you use 'mouseloc.exe' to find the coordinates of your mouse")

mouse_position_x_input=input("please enter the x mouse location: ")
mouse_position_y_input=input("please enter the y mouse location: ")

mouse_position_x = int(mouse_position_x_input)
mouse_position_y = int(mouse_position_y_input)

wait_time_input=input("How long should each pause be between clicks? (in seconds): ")

wait_time = int(wait_time_input)

print("hold the letter 'L' to stop the loop")

while True:
    pyautogui.moveTo(mouse_position_x, mouse_position_y)
    pyautogui.click()
    time.sleep(wait_time)
    if keyboard.is_pressed("l"):
        break