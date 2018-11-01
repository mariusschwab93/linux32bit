from Tkinter import *
import time
root = Tk()
l = Label( root, text=time.strftime( "%d/%m/%Y %A %H:%M:%S") )
l.pack()
root.update()
while True:
        time.sleep( 1 )
        l[ "text" ]=time.strftime( "%d/%m/%Y %A %H:%M:%S" )
        root.update()

mainloop()

