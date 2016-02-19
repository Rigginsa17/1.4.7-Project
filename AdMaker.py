from Tkinter import *

#GUI Code
root = Tk()
root.title("Ad Maker") #GUI title
root.geometry("250x250") #GUI size
app = Frame(root)
app.grid()
button1 = Button(app, text = "Logo")
button1.grid() #sets button for the logo function
button2 = Button(app, text = "Frame")
button2.grid() #sets button for the frame function
root.mainloop()