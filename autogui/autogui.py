# -*- coding:utf-8 -*-
import pyautogui
screenWidth, screenHeight = pyautogui.size()
currentMouseX, currentMouseY = pyautogui.position()
pyautogui.PAUSE = 1.5
pyautogui.moveTo(100, 150)
pyautogui.hotkey('command', 'space')
pyautogui.press('esc')