import tkinter.messagebox
import tkinter.colorchooser
 
print(tkinter.colorchooser.askcolor())
# (None, None) 点击取消或关闭
# ((0, 0, 0), '#000000') 格式: (颜色元组, RGB码)
return_value = tkinter.messagebox.showerror('error','encounter uknow virus')

print(type(return_value),return_value)

