import turtle
from turtle import*
import random
import math
import time
from platform import Platform
from player import *
import tkinter as tk

turtle.setup(1200,800)
turtle.tracer(0,0)
turtle.hideturtle()
running= True
sleep = 0.0077	
turtle.pu()
screen_width = turtle.getcanvas().winfo_width()//2
screen_height = turtle.getcanvas().winfo_height()//2

number_of_platforms= 5
platforms= []

plat_width= 110
plat_height=25
plat_dy=5
x_pos = [-350,150,-50,-250,-450]

def randomize_platform(platform):
	y=platform.ycor()
	x= random.randint(-screen_width+platform.width, screen_width+platform.width)
	platform.goto(x,y)


def collide(platform):
	player_bottom= player.ycor() - player.height
	player_top= player.ycor() + player.height                      
	player_right= player.xcor() + player.width          
	player_left= player.xcor() -player.width


	platform_bottom= platform.ycor()-platform.height
	platform_top= platform.ycor()+platform.height
	platform_right= platfogrm.xcor()+platform.width
	platform_left= platform.xcor()- platform.width

	if platform_top>= player_bottom and platform_bottom<=player_top and platform_right>=player_left and platform_left<=player_right:
		return True
	return False


def move_platforms_down():
	for new_platforms in PLATFORMS:
		new_platforms.move()

player= Player(0,-340, 2, 2)

turtle.onkeypress(left,"Left")
turtle.onkeypress(space, "space")
turtle.onkeypress(right,"Right")
turtle.listen()

def playgame():
	for i in range(number_of_platforms):
		new_plat= Platform(x_pos[i-1], screen_height,plat_width, plat_height, plat_dy)
		platforms.append(new_plat)
	
	while running:
		turtle.listen()
		screen.ontimer(move_platforms_down(), 3*1000)
		player.move()
		for platform in platforms:
			if not player.ycor()==platform.ycor()+ plat_height+player.height:
				screen.ontimer(player.fallingdown(), 7*1000)
			running=collide(platform)

		if screen_width!= int(turtle.getcanvas().winfo_width()/2) or screen_height != int(turtle.getcanvas().winfo_height()/2):
			screen_width= int(turtle.getcanvas().winfo_width()/2)
			screen_height= int(turtle.getcanvas().winfo_height()/2)
		turtle.update()
		time.sleep(sleep)

playgame()