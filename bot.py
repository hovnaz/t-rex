# from PIL import ImageGrab, ImageOps
# import pyautogui
# import time
# from numpy import *

# class Cordinates:
# 	replayBtn = (311,282)
# 	dinosaur = ((76,282),(76,313))
# 	# x = 240, y = 500 cordinate to check for tree

# def restartGame():
# 	# Cordinatnery vercnum e Cordinates class-i mejic
# 	# (320,386) henc ays dirqum gtnvum e restart kochaky
# 	pyautogui.click(Cordinates.replayBtn)

# #catk-i heravoruteun

# box_near_len = 70
# box_away_len = 130

# def pressSpace():
# 	pyautogui.keyDown('space') # kocaky sexmac pahum e
# 	time.sleep(0.05)
# 	# print('Jump')
# 	pyautogui.keyUp('space') # kochaky toghnum e
# def imageGrab():
# 	# amenamoty
# 	box_near = (Cordinates.dinosaur[0][0],Cordinates.dinosaur[0][1],Cordinates.dinosaur[1][0]+box_near_len,Cordinates.dinosaur[1][1])
# 	# amenaherun
# 	box_away = (Cordinates.dinosaur[0][0]+box_away_len,Cordinates.dinosaur[0][1],Cordinates.dinosaur[1][0]+22+box_away_len,Cordinates.dinosaur[1][1])
# 	# sa bavakanin herun e tesnum ev voroshelu e te dimacic inch e galis
# 	# image = ImageGrab.grab(box).save("test.jpg") #ete petq e save e anum tvial hatvacy
# 	image_away = ImageGrab.grab(box_away) # nkary vercnum e amenaherviny
# 	image_near = ImageGrab.grab(box_near) # nkary vercnum e amenamotikiny

# 	grayImage_away = ImageOps.grayscale(image_away) # nkary sev u spitak e dardznum
# 	grayImage_near = ImageOps.grayscale(image_near) # nkary sev u spitak e dardznum

# 	a_near = array(grayImage_near.getcolors()) # nkari meji gyuneri arjeknery e stanum ev bolor arjeknery mek array-i mej e dnum
# 	a_away = array(grayImage_away.getcolors()) # nkari meji gyuneri arjeknery e stanum ev bolor arjeknery mek array-i mej e dnum
# 	# veradardzneluc bolor arjeknery irar e gumarum vorpezsi unena mek yndanur tiv
# 	return (a_near.sum(),a_away.sum())
# df = 0
# def main():
# 	global df
# 	restartGame()
# 	while True:
# 		box_near,box_away = imageGrab()
# 		print(df)
# 		if box_near != 2500 and box_near != 2755:
# 			# pass
# 			pressSpace() # catq
# 			# time.sleep(0.1) # mi poqr spasum e
# 		if box_away != 929:
# 			pressSpace() # catq
# 			# time.sleep(0.1) # mi poqr spasum e
# 		df+=1

# main()























from PIL import ImageGrab, ImageOps

from pyautogui import click,keyDown,keyUp
from time import sleep
from numpy import array

class Cordinates:
	replayBtn = (311,282)
	dinosaur = ((76,282),(76,313))
	# x = 240, y = 500 cordinate to check for tree

def restartGame():
	# Cordinatnery vercnum e Cordinates class-i mejic
	# (320,386) henc ays dirqum gtnvum e restart kochaky
	click(Cordinates.replayBtn)

#catk-i heravoruteun

box_away_len = 70

def pressSpace():
	keyDown('space') # kocaky sexmac pahum e
	sleep(0.05)
	# print('Jump')
	keyUp('space') # kochaky toghnum e
def imageGrab():
	box_away = (Cordinates.dinosaur[0][0]+box_away_len,Cordinates.dinosaur[0][1],Cordinates.dinosaur[1][0]+22+box_away_len,Cordinates.dinosaur[1][1])
	# sa bavakanin herun e tesnum ev voroshelu e te dimacic inch e galis
	# image = ImageGrab.grab(box).save("test.jpg") #ete petq e save e anum tvial hatvacy
	image_away = ImageGrab.grab(box_away) # nkary vercnum e amenaherviny

	grayImage_away = ImageOps.grayscale(image_away) # nkary sev u spitak e dardznum

	a_away = array(grayImage_away.getcolors()) # nkari meji gyuneri arjeknery e stanum ev bolor arjeknery mek array-i mej e dnum
	# veradardzneluc bolor arjeknery irar e gumarum vorpezsi unena mek yndanur tiv
	return a_away.sum()
df = 0
def main():
	global df
	restartGame()
	while True:
		box_away = imageGrab()

		if box_away != 929:
			pressSpace() # catq
			# time.sleep(0.1) # mi poqr spasum e

main()