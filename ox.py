#important variable
x="O"
winn=[['a11','a12','a13'],['a21','a22','a23'],['a31','a32','a33'],['a11','a21','a31'],['a12','a22','a32'],['a13','a23','a33'],['a11','a22','a33'],['a13','a22','a31']]
result_sheet=dict()

#importing library used (tkinter)
import tkinter as t

#creating a window
win=t.Tk()

#title
win.title("O_X")

#changing background color of window by configuration method (black=="#000000")
win.config(bg="#000000")

#playing function
def check():
    for i in winn:
        try:
            if result_sheet[i[0]]==result_sheet[i[1]]==result_sheet[i[2]]:
                k=result_sheet[i[0]]
                win.destroy()
                win2=t.Tk()
                label=t.Label(win2,text="WIN"+" "+k,font=("Arial", 20))
                label.pack()
                quit_=t.Button(win2,text="exit",command=lambda: win2.destroy())
                quit_.pack()
                win2.mainloop()
            else:
                pass
        except Exception as e:
            pass
def play(n):
    global x
    def nun():
        pass
    if x=="O":
        n.config(text="O",command=nun)
        var="a"+str(n.grid_info()["row"])+str(n.grid_info()["column"])
        result_sheet[var]="O"
        x="X"
    else:
        n.config(text="X",command=nun)
        var="a"+str(n.grid_info()["row"])+str(n.grid_info()["column"])
        result_sheet[var]="X"
        x="O"
    if len(result_sheet)>=5:
        check()
    else:
        pass
    
    
#making button grid
for i in range(1,4):
    for j in range(1,4):
        exec(f"a{i}{j}=t.Button(win,width=10,height=5,command=lambda: play(a{i}{j}));a{i}{j}.grid(row={i},column={j})")
#setting window on loop 
win.mainloop()
