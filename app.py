from tkinter import *
from pad import Pad
import random

w = 700
h = 400

root = Tk()
root.resizable(False, False)
root.geometry("{}x{}".format(w, h))
root.title("Ping-Pong")


# Add canvas to screen
c = Canvas(root, width=w, height=h, bg="#1050b7")
c.pack()


# Add stadium layout
c.create_rectangle(0, 0, 15, h, fill="#fff", outline="#fff")
c.create_rectangle(w-15, 0, w, h, fill="#fff", outline="#fff")
c.create_rectangle(w//2-5, 0, w//2+5, h, fill="#fff", outline="#fff")

ball = c.create_oval(w//2-20, h//2-20, w//2+20, h//2+20, fill="#EA9111", outline="#EA9111")
ball_R = (c.coords(ball)[2]-c.coords(ball)[0]) / 2
print(ball_R)
d = ball_R - (Pad.pad_width*(2*ball_R-Pad.pad_width))**0.5

# Define pads
left_pad = Pad(0, 0, c)
right_pad = Pad(w-Pad.pad_width, 0, c)


# V for balls
vx, vy = random.choice([-3, 3]), random.choice([4, -4])



def keypress(event):
	key = event.keysym
	
	if key.lower() == "w":
		left_pad.active = True
		left_pad.speed = -10

	if key.lower() == "s":
		left_pad.active = True
		left_pad.speed = 10

	if key == "Up":
		right_pad.active = True
		right_pad.speed = -10

	if key == "Down":
		right_pad.active = True
		right_pad.speed = 10

def keyrelease(event):
	key = event.keysym

	if key.lower() == "w" or key.lower() == "s":
		left_pad.active = False

	if key == "Up" or key == "Down":
		right_pad.active = False

def move_ball():
	global vx, vy

	ball_coords = c.coords(ball)

	# if ball touches on top change it's y vector 
	if ball_coords[1] == 0 or ball_coords[3] == h:
		vy = -vy

	# check if pad touched the ball
	left_pad_coords = c.coords(left_pad.pad)
	right_pad_coords = c.coords(right_pad.pad)

	touch_on_left = (left_pad_coords[0] <= ball_coords[0] <= left_pad_coords[2]) and ((left_pad_coords[1] <= ball_coords[3]-d <= left_pad_coords[3]) or (left_pad_coords[1] <= ball_coords[1]+d <= left_pad_coords[3]))
	touch_on_right = (right_pad_coords[0] <= ball_coords[2] <= right_pad_coords[2]) and ((right_pad_coords[1] <= ball_coords[3]-d <= right_pad_coords[3]) or (right_pad_coords[1] <= ball_coords[1]+d <= right_pad_coords[3]))

	if touch_on_right or touch_on_left:
		vx = -vx
		right_pad.speed = right_pad.speed + 3
		left_pad.speed = left_pad.speed + 3

		

	# ball touched on left wall (1st player lost)
	if ball_coords[0] <= 0:
		pass
	# ball touched on right wall (2nd player lost)
	if ball_coords[2] >= w:
		pass


	c.move(ball, vx, vy)


def main():
	left_pad.move()
	right_pad.move()
	move_ball()
	root.after(30, main)

c.bind("<KeyPress>",keypress)
c.bind("<KeyRelease>",keyrelease)
c.focus_set()

main()
root.mainloop()