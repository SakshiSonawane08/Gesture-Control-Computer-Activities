# Import module
import os
from tkinter import *
from PIL import Image, ImageTk

# Create object
root = Tk()

# Adjust size
root.geometry("800x600")

# Add image file
image = ImageTk.PhotoImage(Image.open("C:\\Users\\Shree\\Desktop\\jpg_20230313_193958_0000.jpg"))
canvas1 = Canvas(root, width=1200, height=700)
canvas1.create_image(0, 0, anchor=NW, image=image)
canvas1.pack(fill="both", expand=True)

# Display image
canvas1.create_image(0, 0, image=image, anchor="nw")

# Add Text
#canvas1.create_text(700, 450, text="Welcome", font=('Ink Free', 40, 'bold'))

# Create Buttons
button1 = Button(root, text="MediaPlayer Controller")
button3 = Button(root, text="PPT Controller", )
button2 = Button(root, text="Keyboard Controller")
button4 = Button(root, text="Mouse Controller")


# Function for button 1
def media_player_controller(path):
   # print("Media Player Controller for path:", path)
 os.system('python3.10 PPT_1.py')

# Function for button 2
def keyboard_controller(root):
    # root.destroy()
    os.system('python3.10 Keyboard1.py')


# print("Keyboard Controller for path:", Keyboard1.py)


# Function for button 3
def ppt_controller():
    os.system('python3.10 PPT_1.py')
    # print("PPT Controller for path:", path)


# Function for button 4
def mouse_controller():
    os.system('python3.10 Mouse_1.py')


# print("Mouse Controller for path:", path)


# Display Buttons
button1_canvas = canvas1.create_window(40, 40, anchor="nw", window=button1)
button1.config(font=('Ink Free', 25, 'bold'))
button1.config(bg='#D06F5A')
button1.config(fg='#080200')
button1.config(activebackground='#F53207')
button1.config(activeforeground='#080200')
button1.config(command=lambda: ppt_controller())
# button = Button(root, text='Submit', bg='blue',active-background='red').pack()

button2_canvas = canvas1.create_window(1200, 40, anchor="nw", window=button2)
button2.config(font=('Ink Free', 25, 'bold'))
button2.config(bg='#D06F5A')
button2.config(fg='#080200')
button2.config(activebackground='#F53207')
button2.config(activebackground='#F53207')
button2.config(command=lambda: keyboard_controller(root))

button3_canvas = canvas1.create_window(40, 700, anchor="nw", window=button3)
button3.config(font=('Ink Free', 25, 'bold'))
button3.config(bg='#D06F5A')
button3.config(fg='#080200')
button3.config(activebackground='#F53207')
button3.config(activebackground='#F53207')
button3.config(command=lambda: ppt_controller())

button4_canvas = canvas1.create_window(1250, 700, anchor="nw", window=button4)
button4.config(font=('Ink Free', 25, 'bold'))
button4.config(bg='#D06F5A')
button4.config(fg='#080200')
button4.config(activebackground='#F53207')
button4.config(activebackground='#F53207')
button4.config(command=lambda: mouse_controller())
# Execute tkinter
root.mainloop()
