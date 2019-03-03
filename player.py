import turtle
from turtle import*
import random
import math
import time










direction= up



def space():
	direction = up
	
def left():
	direction = left



def right():
	direction = right

# func = partial(up, running)
# turtle.onkeypress(up, UP_ARROW) 
turtle.onkeypress(left,"Left")
turtle.onkeypress(space, "space")
turtle.onkeypress(right,"Right")
turtle.listen()


class Player(Turtle):
	def __init__(self, x, y, dx, dy):
		Turtle.__init__(self)
		self.pu()
		turtle.ht()
		self.goto(x,y)
		self.dx = dx
		self.dy = dy
		self.shape("square")#players shape
		self.shapesize(50/10)
		self.height = 25
		self.width= 25

	def move(self):
		old_x = self.xcor()
		old_y = self.ycor()

		global direction
		if direction==right:
			self.goto(old_x + self.dx , old_y)
			#print("You moved right!")
		elif direction==left:
			self.goto(old_x - self.dx , old_y)
			#print("You moved left!")
		elif direction==up :
			self.goto(old_x , old_y + self.dy)

		old_x = self.xcor()
		old_y = self.ycor()
		new_x = old_x + self.dx
		new_y = old_y + self.dy
	
	def falling_down(self):
		old_x = self.xcor()
		old_y = self.ycor()
		new_y = max(old_x, old_y - 1)
		self.goto(old_x,new_y)

		if new_x > screen_width:
			self.goto(-screen_width, self.ycor())
		if new_x < -screen_width:
			self.goto(-screen_width, self.ycor())
		if new_y <= -screen_height:
			running=False

'''
pl= Player(0,0, 1, 2)
while True:
	pl.move()
	turtle.listen()
turtle.mainloop()
'''