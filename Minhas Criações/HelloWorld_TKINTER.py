import tkinter

top = tkinter.Tk()


def hello_world():
    l = tkinter.Label(top,text="Hello world!")
    l.pack()


w = tkinter.Button(top,text="Clica em mim!", command=hello_world)
w.pack()

top.mainloop()