import tkinter
import tkinter.filedialog

def load_text():
    typ = [("Text", "*.txt"), ("Python", "*.py")]
    fn = tkinter.filedialog.askopenfilename(filetypes=typ)
    if fn != "":
        f = None
        try:
            f = open(fn, 'r', encoding="utf-8")
            te.delete("1.0", "end")
            te.insert("1.0", f.read())
        except:
            f = open(fn, 'r', encoding="shift-jis")
            te.delete("1.0", "end")
            te.delete("1.0", f.read())
        finally:
            if f != None:
                f.close()

def save_text():
    typ = [("Text", "*.txt")]
    fn = tkinter.filedialog.asksaveasfilename(filetypes=typ)
    if fn != "":
        if fn[-4:] != ".txt":
            fn = fn + ".txt"
        with open(fn, 'w', encoding="utf-8") as f:
            f.write(te.get("1.0", "end-1c"))

def col_black():
    te.configure(bg="black", fg="white", insertbackground="white")

def col_white():
    te.configure(bg="white", fg="black", insertbackground="black")


root = tkinter.Tk()
root.title("テキストエディタ")
fr = tkinter.Frame()
fr.pack(expand=True, fill=tkinter.BOTH)
te = tkinter.Text(fr, width=80, height=30)
sc = tkinter.Scrollbar(fr, orient=tkinter.VERTICAL, command=te.yview)
te.pack(expand=True, fill=tkinter.BOTH)
te["yscrollcommand"] = sc.set
mbar = tkinter.Menu()
mcom = tkinter.Menu(mbar, tearoff=0)
mcom.add_command(label="読み込み", command=load_text)
mcom.add_separator()
mcom.add_command(label="書き込み", command=save_text)
mbar.add_cascade(label="ファイル", menu=mcom)
mcom2 = tkinter.Menu(mbar, tearoff=0)
mcom2.add_command(label='黒', command=col_black)
mcom2.add_command(label='白', command=col_white)
mbar.add_cascade(label="背景色", menu=mcom2)
root["menu"] = mbar
root.mainloop()


