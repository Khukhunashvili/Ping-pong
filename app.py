from tkinter import *

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

root.mainloop()