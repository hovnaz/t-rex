




# # from matplotlib import pyplot as plt
# img_rgb = array(screenshot(region=(12,229, 611, 100)))
# # img_rgb = imread('img/mario/map_mario.jpg')
# img_gray = cvtColor(img_rgb, COLOR_BGR2GRAY)
# template = imread('img/dino/1_mec.jpg',0)
	
# res = matchTemplate(img_gray,template,TM_CCOEFF_NORMED)
# threshold = 0.8
# # in modul numpy	
# loc = where( res >= threshold)


# print(loc[1][0],loc[0][0])































from cv2 import imread,cvtColor,matchTemplate,TM_CCOEFF_NORMED,COLOR_BGR2GRAY

from numpy import where,array


from pyautogui import click,press,keyDown,keyUp,screenshot
from time import sleep

class Cordinates:
	dinosaur = ((78,282),(78,313))
	replayBtn = (311,282)
	# _map_ = (50,282, 600, 317)
	_map_ = (55,250, 540, 92)




def restartGame():

	click(Cordinates.replayBtn)

default_distance = [70,100,125,80,110,123]

template = []
distance_W = [0,0,0,0,0,0]
	
template.append(imread('img/dino/3_poqr.jpg',0)) # 0
template.append(imread('img/dino/2_poqr.jpg',0)) # 1
template.append(imread('img/dino/1_poqr.jpg',0)) # 2

template.append(imread('img/dino/4_mec.jpg',0)) # 3
template.append(imread('img/dino/2_mec.jpg',0)) # 4
template.append(imread('img/dino/1_mec.jpg',0)) # 5

template.append(imread('img/dino/trchun.jpg',0)) # 6

# game over
template.append(imread('img/dino/game_over.jpg',0)) # 7

fghfh = False

def imageGrab():
	global fghfh
	# from matplotlib import pyplot as plt
	img_rgb = array(screenshot(region=Cordinates._map_))
	# img_rgb = imread('img/mario/map_mario.jpg')
	img_gray = cvtColor(img_rgb, COLOR_BGR2GRAY)
	select_item_list = []
	for template_i in range(len(template)):
		res = matchTemplate(img_gray,template[template_i],TM_CCOEFF_NORMED)
		threshold = 0.8
		# in modul numpy	
		loc = where( res >= threshold)
		if len(loc[0]) >= 1:
			print('mtav')
			x = loc[1][0]
			y = loc[0][0]
			distance = x-Cordinates.dinosaur[0][0]
			if template_i <= 5:
				
				if fghfh == True:
					fghfh = False
					keyUp('down')
				select_item_list.append(template_i)
				if distance <= default_distance[select_item_list[0]]+distance_W[select_item_list[0]]:
					print('evs mek ankam mtav')
					print(distance)
					return True

			elif template_i == 6:
				if y == 45:
					return True

				elif y == 20:

					fghfh = True
					keyDown('down')

			elif template_i == 7:
				return '_'

	
# fps = 0
distance_W_counter = 0
def main():
	global distance_W_counter,distance_W
	restartGame()
	while True:
		# print(fps)
		box = imageGrab()
		if box == True:
			press('space')
			break

			if distance_W_counter == 15:
				distance_W_counter = 0

				# 3_poqr = 0 
				# 2_poqr = 1
				# 1_poqr = 2
				# 4_mec = 3
				# 2_mec = 4
				# 1_mec = 5


				distance_W[0]+=8
				distance_W[1]+=9
				distance_W[2]+=12
				distance_W[3]+=6
				distance_W[4]+=7
				distance_W[5]+=9

			distance_W_counter+=1
			# print(distance_W)
			continue
		elif box == '_':
			print('Game Over')
			break
		# fps+=1
		# break

main()
