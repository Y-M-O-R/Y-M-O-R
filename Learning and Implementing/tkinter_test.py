import tkinter
import csv
display = tkinter.Tk()
display.geometry('605x454')
masterr = tkinter.Frame(
    master= display,
    relief = tkinter.FLAT,
    borderwidth= 5
)
my_string = tkinter.StringVar()
my_string.set('hablo no espanio')
def one():
    my_string.set('come one number 1')

def three():
    my_string.set('screw number 3')
bttn_test = tkinter.Button(
    master= masterr,
    text='button one',
    foreground= 'white',
    bg = 'black',
    width = 10,
    height = 10,

    command= one
)
bttn_test.grid(row=0, column=0)
bttn_test_two = tkinter.Button(
    master= masterr,
    text='button none',
    foreground= 'white',
    bg = 'black',
    width = 10,
    height = 10
)
bttn_test_two.grid(row=0,  column=1)

bttn_test_three = tkinter.Button(
    master= masterr,
    text='button three',
    foreground= 'white',
    bg = 'black',
    width = 10,
    height = 10,
    command= three
)
bttn_test_three.grid(row=0,  column=2)


lbl = tkinter.Label(masterr, textvariable=  my_string)
lbl.grid(row=1, column=1)
masterr.grid(row=0,column=0)
class test:
    def __init__(self):
        self.master_frame = tkinter.Frame(display)
        self.lbl_str = tkinter.StringVar()
        self.lbl_str.set('text')
        self.lbl_name = tkinter.Label(self.master_frame, textvariable=self.lbl_str).grid(row=3,column=0)
        self.master_frame.grid(row=4,column=2)

        self.bttn_str = tkinter.Button(self.master_frame, text='click me', fg='pink', bg='green', width=10, height=10,
                                       command=self.change_str, ).grid(row=4, column=1)
        self.bttn_str = tkinter.Button(self.master_frame, text='click me', fg='pink', bg='green', width=10, height=10,
                                       command=self.change_str).grid(row=4, column=2)
        self.bttn_str = tkinter.Button(self.master_frame, text='click me', fg='pink', bg='green', width=10, height=10,
                                       command=lambda : self.fresh_str(1) ).grid(row=4, column=3)
    def change_str(self):
        self.lbl_str.set('dont click')
    def fresh_str(self, x):
        self.lbl_str.set(str(x))

#frameb = tkinter.Frame(master=display, width = 100, height= 400, highlightbackground="blue", highlightthickness=2)
#frameb.grid(row=1, column=0)
#frameb.grid_propagate(0)
#var_str = 'help me please!!!'
#labelb= tkinter.Label(master=frameb, text='var_str)')
#labelb.grid(row=0,column=0)


tk_test = test()
display.mainloop()
print('executed')


