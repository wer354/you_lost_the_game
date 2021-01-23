from tkinter import *
root = Tk()
root.title("Test")
root.geometry("300x50")
myLabel = Label(root, text="")
myLabel.pack()
count = 0
def clicked():
    global count
    count+=1
    myLabel.configure(text=f'Look! You lost the game {count} times!')
myButton = Button(root, text="Click me!", command=clicked)
myButton.pack()
root.mainloop()
