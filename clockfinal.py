# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 17:08:57 2022

@author: Vansh Khandelwal
"""

import time
import math
import tkinter as tk
from PIL import Image, ImageTk, ImageDraw, ImageFont


def clock(img):
    
    img1 = ImageDraw.Draw(img)  

    # create circle 
    img1.ellipse((0, 0, 403, 403), outline=(250, 0, 0))


    # Circle radius = 400/2 = 200

    img1.text((200, 3), "12")
    img1.text((300, 35), "1")
    img1.text((365, 110), "2")
    img1.text((390, 200), "3")
    img1.text((365, 290), "4")
    img1.text((300, 355), "5")
    img1.text((200, 390), "6")
    img1.text((100, 355), "7")
    img1.text((35, 290), "8")
    img1.text((3, 200), "9")
    img1.text((35, 110), "10")
    img1.text((100, 35), "11")
    
    
    b = time.ctime()
    
    font = ImageFont.truetype("arial.ttf", 18)
    img1.text((100, 260), b, font = font)

    a = time.localtime()

    hour = a.tm_hour
    minutes = a.tm_min
    seconds = a.tm_sec

    angle_Minute = (6*minutes*math.pi)/180
    # We multipled by 6 because each minute in clock is equal to 6 degrees in a circle
    # since 60 min = 360 deg therefore 1 min = 360/60 = 6 deg
    
    angle_Hour = (((hour%12)*30+ (minutes/2))*math.pi)/180
    # we took remainder with 12 because hour is in 24 hour format
    # we multiplied by 30 since each hour is 30 deg in circle
    # added minutes to take cahnge the angle as the minute hand reaches 12
    
    angle_Seconds = (6*seconds*math.pi)/180

    # Hour
    
    # Condition to take the quadrant in consideration
    # 200 is added since the orgin is at the top left corner of the window

    if ((hour%12)*30)==90:
        x_hour = 400
        
    elif((hour%12)*30)==270:
        x_hour = 0
        
    else:
        x_hour = 200 + (200*(math.sin(angle_Hour)))
        

    y_hour = 200-(200*math.cos(angle_Hour))

    # Minute  

    if (6*minutes)==90:
        x_minute = 400
        
    elif(6*minutes)==270:
        x_minute = 0
        
    else:
        x_minute = 200 + (200*(math.sin(angle_Minute)))

    y_minute = 200-(200*math.cos(angle_Minute))
                
    # Seconds

    if (6*seconds)==90:
        x_seconds = 400
        
    elif(6*seconds)==270:
        x_seconds = 0
        
    else:
        x_seconds = 200 + (200*(math.sin(angle_Seconds)))
          
    y_seconds = 200-(200*math.cos(angle_Seconds))

    # Create line
    shape_hour = [(200, 200), (x_hour, y_hour)]
    shape_min = [(200, 200), (x_minute, y_minute)]
    shape_sec = [(200, 200), (x_seconds, y_seconds)]

    # Hour hand
    img1.line(shape_hour, fill="orange", width=15)
    
    # Minute hand
    img1.line(shape_min, fill ="green", width = 10)
    
    # Seconds hand
    img1.line(shape_sec, fill ="blue", width = 5)

    img1.text((100, 100), a)
    # image1.show()
    
    return img

# -----------------------------------------------------------------------------

def callback():
    
    img2 = ImageTk.PhotoImage(clock(Image.new("RGB", (w, h))))
    panel.configure(image=img2)
    panel.image = img2
    root.after(10, callback)
    # update after every 1 sec

# -----------------------------------------------------------------------------


root = tk.Tk()

w, h = 405, 405

image1 = Image.new("RGB", (w, h))

image1 = clock(image1)

img = ImageTk.PhotoImage(image1)
panel = tk.Label(root, image=img)
panel.pack(side="bottom", fill="both", expand="yes")



root.after(10, callback)

root.mainloop()



