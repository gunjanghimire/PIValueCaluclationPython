#PI Value Calculation Using the Neelkantha Series
j = 3.0
k=1
for i in range(2, 400000, 2): #Change the Desired End Step to get a better nth value
    k = k+1
    if k % 2 ==0:
        j = j+ 4/(i*(i+1)*(i+2))
    else:
        j = j- 4/(i*(i+1)*(i+2))
a = repr(j)
from tkinter import *
top = Tk()
L1 = Label(top, text="The Value of PI: ")
L1.pack( side = TOP)
L2 = Label(top, text=a)
L2.pack( side = BOTTOM)
#print('The Value of PI up to nth digit: Limit of 150 iterations: ')
#print(j)
top.mainloop()