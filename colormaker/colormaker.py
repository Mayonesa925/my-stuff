from tkinter import *

def createSquare(bgColor, x, y):
    #print("Creating square: " + str(bgColor))
    square = Canvas(width=16, height=16, bg=bgColor, cursor='hand2')
    square.place(x=x, y=y)

#Declare window
#print("Building window")
window = Tk()
window.title("colormaker.exe")
window.configure(width = 430, height = 150)
window.configure(bg='lightgray')
window.resizable(False, False)

colorLabel = Label(text="Colores", bg='lightgray', cursor='xterm')
colorLabel.place(x=5, y=5)

colorPreviewLabel = Label(text="Vista previa", bg='lightgray', cursor='xterm')
colorPreviewLabel.place(x=340, y=5)

colorPreview = Canvas(width=64, height=64, bg='black', cursor='hand2')
colorPreview.place(x=340, y=30)

createButton = Button(text="Crear", cursor='hand2')
createButton.place(x=340, y=110, width=68)

createSquare('red', 5, 30)
createSquare('orange', 30, 30)
createSquare('yellow', 56, 30)
createSquare('green', 83, 30)
createSquare('blue', 110, 30)
createSquare('lightblue', 138, 30)
createSquare('purple', 165, 30)
createSquare('magenta', 192, 30)
createSquare('black', 219, 30)
createSquare('gray', 248, 30)
createSquare('lightgray', 277, 30)
createSquare('white', 306, 30)

winWidth = window.winfo_reqwidth()
winHeight = window.winfo_reqheight()
posX = int(window.winfo_screenwidth() / 2 - winWidth / 2)
posY = int(window.winfo_screenheight() / 2 - winHeight / 2)
window.geometry("+{}+{}".format(posX, posY))

#print("Loaded!")
window.mainloop()

