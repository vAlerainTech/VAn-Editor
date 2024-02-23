import  tkinter  as  tk   #导入Tkinter
import  tkinter.ttk  as  ttk   #导入Tkinter.ttk
from  tkinter.scrolledtext  import ScrolledText  #导入ScrolledText
from tkinter.filedialog import *
from tkinter import messagebox

mytitle='vAlerianPython编辑器'

#建立主窗口
root=tk.Tk()
root.title(mytitle)
root.geometry('{}x{}+{}+{}'.format(1200, 600, 100, 100))

#放几个按钮
frame=tk.Frame(root)
button1=tk.Button(frame,text='新文件')
button2=tk.Button(frame,text='读取文件')
button3=tk.Button(frame,text='另存文件')
button4=tk.Button(frame,text='关于')
button1.pack(side=tk.LEFT)
button2.pack(side=tk.LEFT)
button3.pack(side=tk.LEFT)
button4.pack(side=tk.LEFT)
frame.pack(side=tk.TOP,fill=tk.BOTH)

#放置一个文本框
textPad= ScrolledText(bg='white', height=10)
textPad.pack(fill=tk.BOTH, expand=1)
textPad.focus_set()

default_text = "vAlerian基于Python编辑器，一个简易编辑器，如果您能使用万分感谢！"
textPad.insert("1.0", default_text)  # 在文本框中插入默认文本
textPad.bind("<FocusIn>", lambda event: textPad.delete("1.0", "end") if textPad.get("1.0", "end-1c") == default_text else None)
textPad.focus_set()
#实现按钮功能
def btnfunc01():  #新文件
    textPad.delete(1.0,tk.END)

def btnfunc02(): #读取文件
    filename = askopenfilename(defaultextension='.py')
    if filename != '':
        textPad.delete(1.0,tk.END)#delete all
        f = open(filename,'r',encoding='utf-8',errors='ignore')
        textPad.insert(1.0,f.read())
        f.close()


def btnfunc03(): #另存文件
    filename = asksaveasfilename(initialfile = 'newfile',defaultextension ='.py')
    if filename != '':
        fh = open(filename,'w',encoding='utf-8',errors='ignore')
        msg = textPad.get(1.0,tk.END)
        fh.write(msg)
        fh.close()

def about(): #关于
    messagebox.showinfo('about', '作者为:vAlerian！\n版权vAlerian所有！')

#为按钮设置功能
button1['command']=lambda:btnfunc01()
button2['command']=lambda:btnfunc02()
button3['command']=lambda:btnfunc03()
button4['command']=lambda:about()

root.mainloop()  	#进入Tkinter消息循环
