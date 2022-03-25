from re import L
import tkinter
import time
from PIL import Image, ImageTk

window = tkinter.Tk()
window.geometry("900x600")
window.title("Baghchal")

# label = tkinter.Label(window, text="\n\n\n\n\n       Welcome to AI Baghchal         \n\n\n\n\n").pack()

l1 = tkinter.Label(window,text="AI Baghchal", font=("Arial Bold",20)).place(x=150,y=20)
canvas = tkinter.Canvas(window, width=500, height=500,bg="skyblue")
canvas.place(x=20,y=60)
canvas.create_line(20,20,480,480, fill="green", width=3)
canvas.create_line(20,480,480,20, fill="green", width=3)
canvas.create_line(19,20,482,20, fill="green", width=3)
canvas.create_line(20,20,20,480, fill="green", width=3)
canvas.create_line(19,480,482,480, fill="green", width=3)
canvas.create_line(480,20,480,480, fill="green", width=3)
canvas.create_line(20,250,480,250, fill="green", width=3)
canvas.create_line(250,20,250,480, fill="green", width=3)
canvas.create_line(20,135,480,135, fill="green", width=3)
canvas.create_line(20,365,480,365, fill="green", width=3)
canvas.create_line(135,20,135,480, fill="green", width=3)
canvas.create_line(365,20,365,480, fill="green", width=3)
canvas.create_line(20,250,250,20, fill="green", width=3)
canvas.create_line(250,20,480,250, fill="green", width=3)
canvas.create_line(480,250,250,480, fill="green", width=3)
canvas.create_line(250,480,20,250, fill="green", width=3)

# img = Image.open("tiger.png")
# img = img.resize((40,40))
# photoimage = ImageTk.PhotoImage(img)
# img = canvas.create_image(150,150,image=photoimage)
# arr=[0]
# def display(event):
#     arr[-1]=ImageTk.PhotoImage(img)
#     img2 = canvas.create_image(event.x,event.y,image=arr[-1])
#     arr.append(0)

# canvas.bind('<Button-1>',display)

# img = Image.open("tiger.png")
# img = img.resize((40,40))
# arr=[0]

arr=[0]

def draw(coordinates,type):
    img = Image.open(type)
    img = img.resize((40,40))
    arr[-1]=ImageTk.PhotoImage(img)
    canvas.create_image(coordinates[0],coordinates[1],image=arr[-1])
    arr.append(0)

arr2=[['T','_','_','_','_'],['G','G','G','G','T'],['_','_','T','_','_'],['G','G','T','G','G'],['G','G','G','G','G']]
graph=[[[20,20],[135,20],[250,20],[365,20],[480,20]],[[20,135],[135,135],[250,135],[365,135],[480,135]],[[20,250],[135,250],[250,250],[365,250],[480,250]],[[20,365],[135,365],[250,365],[365,365],[480,365]],[[20,480],[135,480],[250,480],[365,480],[480,480]]]

for i in range(5):
    for j in range(5):
        if arr2[i][j]=="T":
            # button = tkinter.Button(window,text="Enter",command = lambda: window.after(1000,draw(graph[i][j],"tiger.png")))
            # button.place(x=10,y=10)
            draw(graph[i][j],"tiger.png")
        elif arr2[i][j]=="G":
            draw(graph[i][j],"goat.png")

# time.sleep(4000)
# arr2=[['T','T','T','T','T'],['G','G','G','G','T'],['_','_','T','_','_'],['G','G','T','G','G'],['G','G','G','G','G']]
# for i in range(5):
#     for j in range(5):
#         if arr2[i][j]=="T":
#             # button = tkinter.Button(window,text="Enter",command = lambda: window.after(1000,draw(graph[i][j],"tiger.png")))
#             # button.place(x=10,y=10)
#             draw(graph[i][j],"tiger.png")
#         elif arr2[i][j]=="G":
#             draw(graph[i][j],"goat.png")

window.mainloop()










# img = Image.open("tiger.png")
# img = img.resize((40,40))
# img = ImageTk.PhotoImage(img)
# label = tkinter.Label(window,image=img)
# label.place(x=400,y=100)