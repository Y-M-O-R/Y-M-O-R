# understanding tkinters grid func
# if n items in a frame you get a n^2 grid
from cProfile import label
import tkinter
root = tkinter.Tk()
root.geometry('700x700')

display_frame = tkinter.Frame(master=root, borderwidth=1, relief='solid')
display_frame.grid(row=0, column=0)
label_2  = tkinter.Label(master=display_frame, text='Label 212')
label_1  = tkinter.Label(master=display_frame, text='Label 21')
label_3  = tkinter.Label(master=display_frame, text='Label 212222')


label_2.grid(row=0, column=1, rowspan=2)
label_3.grid(row=3, column=3)
label_1.grid(row=2, column=0)

table_frame = tkinter.Frame(master=root,  borderwidth=1, relief='solid')
table_frame.grid(row=1, column=0)
for row_grid in range(10):
    for col_grid in range(10):
        tkinter.Label(master=table_frame, text = f'row:{row_grid}, column:{col_grid}', borderwidth=1, relief='solid').grid(row=row_grid, column=col_grid)
        

root.mainloop()