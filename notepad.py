from tkinter import*
from tkinter import filedialog

root=Tk()
root.geometry('600x600')
root.title('notepad')
root.config(bg='light pink')
root.resizable(False,False)

def save_file():
    open_file=filedialog.asksaveasfile(mode='w',defaultextension='txt')
    if open_file is None:
        return
    text=str(entry.get(1.0,END))
    open_file.write(text)
    open_file.close()

#functions

def open_file():
    file=filedialog.askopenfile(mode='r',filetype=[('text files','*.txt')])
    if file is not None:
        content=file.read()
        entry.delete(1.0,END)
        entry.insert(INSERT,content)


def cut_text():
    try:
        entry.event_generate('<<Cut>>')
    except:
        pass

def copy_text():
    try:
        entry.event_generate('<<Copy>>')
    except:
        pass

def paste_text():
    try:
        entry.event_generate('<<Paste>>')
    except:
        pass



#widgets
entry=Text(root,undo=True)
entry.pack(expand=True,fill=BOTH)

#menu bar
menu_bar =Menu(root)
root.config(menu=menu_bar)

#file menu
file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

#edit menu
edit_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_separator()
edit_menu.add_command(label="Cut", command=cut_text)
edit_menu.add_command(label="Copy", command=copy_text)
edit_menu.add_command(label="Paste", command=paste_text)

b1=Button(root,width='20',height='2',bg='pink',text='save file',command=save_file).place(x=100,y=5)
b2=Button(root,width='20',height='2',bg='pink',text='open file',command=open_file).place(x=300,y=5)

entry=Text(root,height='33',width='72',wrap=WORD)
entry.place(x=10,y=60)

root.mainloop()


