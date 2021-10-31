import tkinter as tk
import os
from tkinter.constants import YES     # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilename
from rich import print
import rich
import ctypes, os
import sys

def isAdmin():
    try:
        is_admin = (os.getuid() == 0)
    except AttributeError:
        is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
    return is_admin
if isAdmin():
    print("Program succesfully running as admin, ready to commence (Unlock/Lock)")
else:
    print("Program is not running as admin, Please run program as admin next time")
    quit()


def qiut():
    print("ill be bac' when you need to lock and unlock more files (sus)")
    quit()

def lock():
    PathToFIle = askopenfilename() # show an "Open" dialog box and return the path to the selected file
    if PathToFIle == "":
        print("Restart the script, You selected nothing")
        os.execl(sys.executable, sys.executable, *sys.argv)

    print("Answer ""Yes"" If you want to")
    Asked = input("Are you sure you want to lock " + PathToFIle + ' ')


    FormatedPath = str('cacls') + ' ' + PathToFIle + ' ' + str("/P everyone:n")
    print(FormatedPath) 

    if Asked == 'Yes':
        print("Opening hidden cmd")
        os.system("start /wait cmd /c" + FormatedPath)

    else:
        print("Please only type Yes If you want to nothing else")
    
def unlock():
    PathToFIle = askopenfilename() # show an "Open" dialog box and return the path to the selected file
    if PathToFIle == "":
        print("restart the script, You selected nothing")
        os.execl(sys.executable, sys.executable, *sys.argv)
        
    print("Answer ""Yes"" If you want to")
    Asked = input("Are you sure you want to lock " + PathToFIle + ' ')


    FormatedPath = str('cacls') + ' ' + PathToFIle + ' ' + str("/P everyone:f")
    print(FormatedPath) 

    if Asked == 'Yes':
        print("Opening hidden cmd")
        os.system("start /wait cmd /c" + FormatedPath)

    else:
        print("Please only type Yes If you want to nothing else")

def gui():
    root = tk.Tk()
    root.eval('tk::PlaceWindow . center')
    root.attributes('-topmost', True)
    root.overrideredirect(True) # removes title bar
    frame = tk.Frame(root, bg='#00CED1')
    frame.pack()

    button = tk.Button(frame, 
                   text="QUIT", 
                   fg="red",
                   command=qiut)#spelled wrong on purpose
    button.pack(side=tk.LEFT)
    
    slogan = tk.Button(frame,
                    text="Lock",
                    command=lock)
    slogan.pack(side=tk.LEFT)

    big = tk.Button(frame,
                    text="Unlock",
                    command=unlock)
    big.pack(side=tk.LEFT)

    root.mainloop()
    
gui()