# # from PIL import ImageGrab, ImageOps
# # import pyautogui
# # import time
# # from numpy import *

# # class Cordinates:
# # 	replayBtn = (311,282)
# # 	dinosaur = ((76,282),(76,313))
# # 	# x = 240, y = 500 cordinate to check for tree

# # def restartGame():
# # 	# Cordinatnery vercnum e Cordinates class-i mejic
# # 	# (320,386) henc ays dirqum gtnvum e restart kochaky
# # 	pyautogui.click(Cordinates.replayBtn)

# # #catk-i heravoruteun

# # box_near_len = 70
# # box_away_len = 130

# # def pressSpace():
# # 	pyautogui.keyDown('space') # kocaky sexmac pahum e
# # 	time.sleep(0.05)
# # 	# print('Jump')
# # 	pyautogui.keyUp('space') # kochaky toghnum e
# # def imageGrab():
# # 	# amenamoty
# # 	box_near = (Cordinates.dinosaur[0][0],Cordinates.dinosaur[0][1],Cordinates.dinosaur[1][0]+box_near_len,Cordinates.dinosaur[1][1])
# # 	# amenaherun
# # 	box_away = (Cordinates.dinosaur[0][0]+box_away_len,Cordinates.dinosaur[0][1],Cordinates.dinosaur[1][0]+22+box_away_len,Cordinates.dinosaur[1][1])
# # 	# sa bavakanin herun e tesnum ev voroshelu e te dimacic inch e galis
# # 	# image = ImageGrab.grab(box).save("test.jpg") #ete petq e save e anum tvial hatvacy
# # 	image_away = ImageGrab.grab(box_away) # nkary vercnum e amenaherviny
# # 	image_near = ImageGrab.grab(box_near) # nkary vercnum e amenamotikiny

# # 	grayImage_away = ImageOps.grayscale(image_away) # nkary sev u spitak e dardznum
# # 	grayImage_near = ImageOps.grayscale(image_near) # nkary sev u spitak e dardznum

# # 	a_near = array(grayImage_near.getcolors()) # nkari meji gyuneri arjeknery e stanum ev bolor arjeknery mek array-i mej e dnum
# # 	a_away = array(grayImage_away.getcolors()) # nkari meji gyuneri arjeknery e stanum ev bolor arjeknery mek array-i mej e dnum
# # 	# veradardzneluc bolor arjeknery irar e gumarum vorpezsi unena mek yndanur tiv
# # 	return (a_near.sum(),a_away.sum())
# # df = 0
# # def main():
# # 	global df
# # 	restartGame()
# # 	while True:
# # 		box_near,box_away = imageGrab()
# # 		print(df)
# # 		if box_near != 2500 and box_near != 2755:
# # 			# pass
# # 			pressSpace() # catq
# # 			# time.sleep(0.1) # mi poqr spasum e
# # 		if box_away != 929:
# # 			pressSpace() # catq
# # 			# time.sleep(0.1) # mi poqr spasum e
# # 		df+=1

# # main()








# from PyQt5 import QtGui



#!/usr/bin/env python3
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QApplication
import sys






# screenshot = screen.grabWindow(0, 0, 0, 100, 100)

# screenshot.save('shot.jpg', 'jpg')


import cv2
from pyautogui import click,press
from time import sleep


class Cordinates:
	replayBtn = (311,282)
	dinosaur = ((78,282),(78,313))
	# x = 0, y = 31 cordinate to check for tree

def restartGame():
	# Cordinatnery vercnum e Cordinates class-i mejic
	# (320,386) henc ays dirqum gtnvum e restart kochaky
	click(Cordinates.replayBtn)





# #catk-i heravoruteun

box_away_len = 0
box_away_width = 125
box_away_len_counter = 0
def pressSpace():
	global box_away_len,box_away_width,box_away_len_counter
	if box_away_len_counter == 30:
		box_away_width+=5
		# box_away_len+=2
		box_away_len_counter=0

	press('space')
	# print('Jump')
	print(box_away_width)
	box_away_len_counter+=1
def imageGrab():

	app = QApplication(sys.argv)
	screen = QApplication.primaryScreen()

	image_away = screen.grabWindow(
		QApplication.desktop().winId(), 
		x = Cordinates.dinosaur[0][0]+box_away_len,
		y = Cordinates.dinosaur[0][1],
		width = box_away_width,
		height = 31).toImage()


	sum_pixel_away = 0
	for x in range(0,box_away_width):
		for y in range(0,31):
			sum_pixel_away += image_away.pixel(x,y)



	# image_away = screen.grabWindow(
	# 	QApplication.desktop().winId(), 
	# 	x = Cordinates.dinosaur[0][0]+box_away_len,
	# 	y = Cordinates.dinosaur[0][1],
	# 	width = 22,
	# 	height = 31).toImage()


	# sum_pixel_away = 0
	# sum_pixel_away_rgb = []
	# for x in range(0,22):
	# 	for y in range(0,31):
	# 		sum_pixel_away += image_away.pixel(x,y)
	# 		# sum_pixel_away_rgb.append(list(QColor(sum_pixel_away).getRgb()[:-1]))




	
	return sum_pixel_away


def main():

	restartGame()
	while True:
		box = imageGrab()
		# print(box)
		if (box // 133127669481) != box_away_width:
			pressSpace() # catq

		# if box != 2928808728582:
			# pressSpace() # catq

main()

# 1 = 133127669481
# 2 = 266255338962
# 120 = 15975320337720
# 121 = 16108448007201
# 122 = 16241575676682
# 123 = 163'747'033'461'63

