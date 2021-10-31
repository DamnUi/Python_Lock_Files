from tkinter import Tk
import os
from tkinter.constants import YES     # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilename
from rich import print
import rich
import ctypes, os
 
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

FirstAsk = input("Do you want to lock or unlock file? (Lock/Unlock)" + ' ')

if FirstAsk == 'Lock':
    PathToFIle = askopenfilename() # show an "Open" dialog box and return the path to the selected file
    if PathToFIle == "":
        print("Restart the script, You selected nothing")
        quit()

    print("Answer ""Yes"" If you want to")
    Asked = input("Are you sure you want to lock " + PathToFIle + ' ')


    FormatedPath = str('cacls') + ' ' + PathToFIle + ' ' + str("/P everyone:n")
    print(FormatedPath) 

    if Asked == 'Yes':
        print("Opening hidden cmd")
        os.system("start /wait cmd /c" + FormatedPath)

    else:
        print("Please only type Yes If you want to nothing else")
        
#----------------------------------------------------------------------------------------------------------------------------------------------------
        
if FirstAsk == 'Unlock':
    PathToFIle = askopenfilename() # show an "Open" dialog box and return the path to the selected file
    if PathToFIle == "":
        print("Restart the script, You selected nothing")
        quit()
        
    print("Answer ""Yes"" If you want to")
    Asked = input("Are you sure you want to lock " + PathToFIle + ' ')


    FormatedPath = str('cacls') + ' ' + PathToFIle + ' ' + str("/P everyone:f")
    print(FormatedPath) 

    if Asked == 'Yes':
        print("Opening hidden cmd")
        os.system("start /wait cmd /c" + FormatedPath)

    else:
        print("Please only type Yes If you want to nothing else")
