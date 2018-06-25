class Pad:
	pad_width = 15
	pad_height = 100

	def __init__(self, x, y, c):
		self.pad = c.create_rectangle(x, y, x+self.pad_width, y+self.pad_height, fill="#000")
		self.active = False
		self.canvas = c
		self.speed = 5

	def move(self):
		if self.active:
			self.canvas.move(self.pad, 0, self.speed)