from tkinter import *

root = Tk()

root.title('主窗口')
root.geometry('960x480+150+100')

root.wm_attributes('-alpha',0.7)
root.resizable(0,0) 
root.resizable(0,0)#窗口大小不可更改

# toplevel = Toplevel(root)
# toplevel.title('子窗口')
# toplevel.wm_attributes('-alpha',0.7)
label = Label(root,text='这是一个标签',bg='grey',fg='#f0f0f0',font=('中华行楷',15),bd=5,relief='groove')
label.pack() # set lable

root.mainloop()