from tkinter import *
from pad import Pad

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

# Define pads
left_pad = Pad(0, 0, c)
right_pad = Pad(w-Pad.pad_width, 0, c)






def keypress(event):
	key = event.keysym
	
	if(key.lower() == "w"):
		left_pad.active = True
		left_pad.speed = -10

	if(key.lower() == "s"):
		left_pad.active = True
		left_pad.speed = 10

	if(key == "Up"):
		right_pad.active = True
		right_pad.speed = -10

	if(key == "Down"):
		right_pad.active = True
		right_pad.speed = 10

def keyrelease(event):
	key = event.keysym

	if(key.lower() == "w" or key.lower() == "s"):
		left_pad.active = False

	if(key == "Up" or key == "Down"):
		right_pad.active = False

	print(key)

def main():
	left_pad.move()
	right_pad.move()
	root.after(60, main)

c.bind("<KeyPress>",keypress)
c.bind("<KeyRelease>",keyrelease)
c.focus_set()

main()
root.mainloop()