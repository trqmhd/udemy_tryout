from tkinter  import *

window = Tk()

def output_dis():
    #print (e1_value.get())
    mile = float(e1_value.get())*1.605
    t1.insert(END,mile)
    #print (t1)



def output_wght():
    #print (e2_value.get())
    weight = e2_value.get()*1000
    t2.insert(END,weight)
    #print (t1)


b1 = Button(window,text="execute_distance", command=output_dis)
b1.grid(row=0, column=0)


b2 = Button(window,text="execute_weight", command=output_wght)
b2.grid(row=1, column=0)


e1_value= StringVar()
e1 = Entry(window,textvariable=e1_value)
e1.grid(row=0, column=1)


e2_value= DoubleVar()
e2 = Entry(window,textvariable=e2_value)
e2.grid(row=1, column=1)

t1 = Text(window, height= 1, width = 5)
t1.grid(row=0, column=2)


t2 = Text(window, height= 1, width = 5)
t2.grid(row=1, column=2)

window.mainloop()
