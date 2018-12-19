import pyautogui as pg
import time
import urllib3
import pyperclip as pc

pg.PAUSE = 0.5

h, w = pg.size()

a = 0
if a:
	while True:
		print(pg.position())


def get_answers_page():
	pg.moveTo(250, 300)
	pg.click()
	pg.scroll(-10000)
	pg.click(557, 868)
	time.sleep(3)
	pg.click(550, 410)
	time.sleep(3)
	pg.click(345, 58)
	pg.hotkey('ctrl', 'c')
	pg.click(843, 12)
	pg.click(493, 339, 2)
	pg.hotkey('ctrl', 'v')
	pg.hotkey('ctrl', 's')
	pg.click(933, 102)


get_answers_page()
