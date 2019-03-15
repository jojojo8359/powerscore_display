import tkinter as tk
from PIL import Image, ImageTk


class Main(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        self.image = Image.open("background-final.jpg")
        self.image = self.image.resize((960, 540), Image.ANTIALIAS)
        self.real_image = ImageTk.PhotoImage(self.image)
        self.background = tk.Label(self, image=self.real_image)
        self.background.place(x=0, y=0, relwidth=1, relheight=1)
        self.background.image = self.real_image

        self.blue1autolandstate = tk.IntVar()
        self.blue1autolandstate.set(0)
        self.blue1autoland = tk.Checkbutton(self, var=self.blue1autolandstate, bd=0, onvalue=30, offvalue=0, bg="#335650", highlightthickness=0, activebackground="#427068", padx=1, pady=1, command=self.updatebluescore)
        self.blue1autoland.place(x=132, y=80)

        self.blue2autolandstate = tk.IntVar()
        self.blue2autolandstate.set(0)
        self.blue2autoland = tk.Checkbutton(self, var=self.blue2autolandstate, bd=0, onvalue=30, offvalue=0, bg="#335650", highlightthickness=0, activebackground="#427068", padx=1, pady=1, command=self.updatebluescore)
        self.blue2autoland.place(x=180, y=80)

        self.blue1endhangstate = tk.IntVar()
        self.blue1endhangstate.set(0)
        self.blue1endhang = tk.Checkbutton(self, var=self.blue1endhangstate, bd=0, onvalue=50, offvalue=0, bg="#335650", highlightthickness=0, activebackground="#427068", padx=1, pady=1, command=self.updatebluescore)
        self.blue1endhang.place(x=317, y=80)

        self.blue2endhangstate = tk.IntVar()
        self.blue2endhangstate.set(0)
        self.blue2endhang = tk.Checkbutton(self, var=self.blue2endhangstate, bd=0, onvalue=50, offvalue=0, bg="#335650", highlightthickness=0, activebackground="#427068", padx=1, pady=1, command=self.updatebluescore)
        self.blue2endhang.place(x=367, y=80)

        self.blue1silver1 = tk.IntVar()
        self.blue1silver1.set(0)
        self.blue1silver1box = tk.Checkbutton(self, var=self.blue1silver1, bd=0, onvalue=1, offvalue=0, bg="white", highlightthickness=0, padx=0, pady=0, command=self.updatebluescore)
        self.blue1silver1box.toggle()
        self.blue1silver1box.place(x=126, y=123)

        self.blue1silver2 = tk.IntVar()
        self.blue1silver2.set(0)
        self.blue1silver2box = tk.Checkbutton(self, var=self.blue1silver2, bd=0, onvalue=1, offvalue=0, bg="white", highlightthickness=0, padx=0, pady=0, command=self.updatebluescore)
        self.blue1silver2box.toggle()
        self.blue1silver2box.place(x=188, y=123)

        self.blue1gold = tk.IntVar()
        self.blue1gold.set(0)
        self.blue1goldbox = tk.Checkbutton(self, var=self.blue1gold, bd=0, onvalue=1, offvalue=0, bg="gold", highlightthickness=0, activebackground="#dbb800", padx=0, pady=0, command=self.updatebluescore)
        self.blue1goldbox.toggle()
        self.blue1goldbox.place(x=158, y=123)

        self.blue1flag = tk.IntVar()
        self.blue1flag.set(0)
        self.blue1flagbox = tk.Checkbutton(self, var=self.blue1flag, bd=0, onvalue=15, offvalue=0, bg="#335650", highlightthickness=0, activebackground="#427068", padx=5, pady=5, command=self.updatebluescore)
        self.blue1flagbox.place(x=152, y=230)

        self.blue1parkauto = tk.IntVar()
        self.blue1parkauto.set(0)
        self.blue1parkautobox = tk.Checkbutton(self, var=self.blue1parkauto, bd=0, onvalue=10, offvalue=0, bg="#335650", highlightthickness=0, activebackground="#427068", padx=0, pady=0, command=self.updatebluescore)
        self.blue1parkautobox.place(x=90, y=280)

        self.blue2parkauto = tk.IntVar()
        self.blue2parkauto.set(0)
        self.blue2parkautobox = tk.Checkbutton(self, var=self.blue2parkauto, bd=0, onvalue=10, offvalue=0, bg="#335650", highlightthickness=0, activebackground="#427068", padx=0, pady=0, command=self.updatebluescore)
        self.blue2parkautobox.place(x=196, y=280)

        self.blue2silver1 = tk.IntVar()
        self.blue2silver1.set(0)
        self.blue2silver1box = tk.Checkbutton(self, var=self.blue2silver1, bd=0, onvalue=1, offvalue=0, bg="white", highlightthickness=0, padx=0, pady=0, command=self.updatebluescore)
        self.blue2silver1box.toggle()
        self.blue2silver1box.place(x=313, y=123)

        self.blue2silver2 = tk.IntVar()
        self.blue2silver2.set(0)
        self.blue2silver2box = tk.Checkbutton(self, var=self.blue2silver2, bd=0, onvalue=1, offvalue=0, bg="white", highlightthickness=0, padx=0, pady=0, command=self.updatebluescore)
        self.blue2silver2box.toggle()
        self.blue2silver2box.place(x=374, y=123)

        self.blue2gold = tk.IntVar()
        self.blue2gold.set(0)
        self.blue2goldbox = tk.Checkbutton(self, var=self.blue2gold, bd=0, onvalue=1, offvalue=0, bg="gold", highlightthickness=0, activebackground="#dbb800", padx=0, pady=0, command=self.updatebluescore)
        self.blue2goldbox.toggle()
        self.blue2goldbox.place(x=344, y=123)

        self.blue2flag = tk.IntVar()
        self.blue2flag.set(0)
        self.blue2flagbox = tk.Checkbutton(self, var=self.blue2flag, bd=0, onvalue=15, offvalue=0, bg="#335650", highlightthickness=0, activebackground="#427068", padx=5, pady=5, command=self.updatebluescore)
        self.blue2flagbox.place(x=339, y=230)

        self.bluesilverminerals = tk.StringVar()
        self.bluesilverminerals.set("0")
        self.bluesilvermineralsspinbox = tk.Spinbox(self, from_=0, to=100, width=2, bg="#335650", bd=0, state="readonly", readonlybackground="#335650", relief="solid", highlightthickness=0, font=("Arial", 16, "bold"), fg="white", textvariable=self.bluesilverminerals, command=self.updatebluescore)
        self.bluesilvermineralsspinbox.place(x=140, y=340)

        self.bluegoldminerals = tk.StringVar()
        self.bluegoldminerals.set("0")
        self.bluegoldmineralsspinbox = tk.Spinbox(self, from_=0, to=100, width=2, bg="#335650", bd=0, state="readonly", readonlybackground="#335650", relief="solid", highlightthickness=0, font=("Arial", 16, "bold"), fg="white", textvariable=self.bluegoldminerals, command=self.updatebluescore)
        self.bluegoldmineralsspinbox.place(x=253, y=340)

        self.bluedepotminerals = tk.StringVar()
        self.bluedepotminerals.set("0")
        self.bluedepotmineralsspinbox = tk.Spinbox(self, from_=0, to=100, width=2, bg="#335650", bd=0, state="readonly", readonlybackground="#335650", relief="solid", highlightthickness=0, font=("Arial", 16, "bold"), fg="white", textvariable=self.bluedepotminerals, command=self.updatebluescore)
        self.bluedepotmineralsspinbox.place(x=366, y=340)

        self.bluescore = tk.StringVar()
        self.bluescore.set("0")
        self.bluescorelabel = tk.Label(self, textvariable=self.bluescore, font=("Arial", 30, "bold"), width=3, bg="#0b24fb", fg="white")
        self.bluescorelabel.place(x=324, y=472)

        self.redscore = tk.StringVar()
        self.redscore.set("0")
        self.redscorelabel = tk.Label(self, textvariable=self.redscore, font=("Arial", 30, "bold"), width=3, bg="#fc0d1b", fg="white")
        self.redscorelabel.place(x=570, y=472)

    def updatebluescore(self):
        self.bluescore.set(str(self.blue1autolandstate.get() + self.blue2autolandstate.get() + self.blue1endhangstate.get() + self.blue2endhangstate.get() + (int(self.bluesilverminerals.get()) * 5) + \
                               (int(self.bluegoldminerals.get()) * 5) + (int(self.bluedepotminerals.get()) * 2) + (25 if (self.blue1gold.get() == 0 and self.blue1silver1.get() == 1 and self.blue1silver2.get() == 1) else 0)\
                               + self.blue1flag.get() + self.blue1parkauto.get() + self.blue2parkauto.get() + (25 if (self.blue2gold.get() == 0 and self.blue2silver1.get() == 1 and self.blue2silver2.get() == 1) else 0)\
                           + self.blue2flag.get()))


class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.parent.title("Rover Ruckus Scoring Application")
        self.main = Main(self)

        self.main.pack(side="top", fill="both", expand=True)

    def quitapp(self):
        quit(0)


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry('960x540')
    MainApplication(root).pack(side="top", fill="both", expand=True)
    root.mainloop()
