from time import *
from Tkinter import *
import thread


class Uhr:
    def __init__(self):
        self.fenster = Tk()
        self.zeit = StringVar()
        self.anzeige = Label(self.fenster,
                             textvariable=self.zeit,
                             font=("Arial",70))
        self.anzeige.pack()
        thread.start_new_thread(self.aktualisieren, ())
        self.fenster.mainloop()

    def aktualisieren(self):
        while True:
            self.zeit.set(strftime("%d/%m/%Y %A %H:%M:%S"))
            sleep(1)

uhr = Uhr()
