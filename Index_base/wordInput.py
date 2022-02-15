import pyautogui
import time
def nextpage():
	pyautogui.hotkey('ctrl', 'enter')
	time.sleep(0.5)
def openWord():
	pyautogui.moveTo(1183, 1074)
	pyautogui.click()
	time.sleep(0.5)
	pyautogui.hotkey('alt', '=')
	pyautogui.hotkey('ctrl', 'l')
	pyautogui.hotkey('alt', '=')
	time.sleep(10)
def addEquation(equation, count):
	pyautogui.hotkey('alt', '=')
	pyautogui.write(equation)
	pyautogui.press('enter')
	time.sleep(count)
def addLine():
	pyautogui.press('enter')