import Tkinter as tk
import os
button_flag = True

def open():
	os.startfile("final.py")
root = tk.Tk()
frame1 = tk.Frame(root)					# create a frame and pack it
frame1.pack(side=tk.TOP, fill=tk.X) 
photo1 = tk.PhotoImage(file="C:\Users\CLi NinJa\Desktop\Python Project\quickc.gif")   # my image file
button1 = tk.Button(frame1, compound=tk.TOP, image=photo1,
    text="", bg='green', command=open)				# create the image button, image is above (top) the optional text
button1.pack(side=tk.LEFT, padx=2, pady=2)
button1.image = photo1		
root.mainloop()				# start the event loop