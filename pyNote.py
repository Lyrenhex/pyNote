import tkinter
from tkinter import *
import tkinter.scrolledtext as ScrolledText
import tkinter.filedialog as tkFileDialog
import tkinter.messagebox as tkMessageBox

"""
    pyNote basic text editor
    Copyright (c) 2015  Adonis Megalos

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""
 
root = tkinter.Tk(className=" pyNote Text Editor")
textPad = ScrolledText.ScrolledText(root, width=100000, height=40000)
root.geometry("670x660")
 
# create a menu & define functions for each menu item
 
def open_command():
        file = tkFileDialog.askopenfile(parent=root,mode='rb',title='Select a file')
        if file != None:
            contents = file.read()
            textPad.insert('1.0',contents)
            file.close()
 
def save_command():
    file = tkFileDialog.asksaveasfile(mode='w')
    if file != None:
    # slice off the last character from get, as an extra return is added
        data = textPad.get('1.0', END+'-1c')
        file.write(data)
        file.close()
         
def exit_command():
    if tkMessageBox.askokcancel("Quit", "Do you really want to quit?"):
        root.destroy()
 
def about_command():
    label = tkMessageBox.showinfo("About", "pyNote basic text editor by Adonis Megalos.\nContact: scratso@yahoo.com")

def license_command():
    label = tkMessageBox.showinfo("License", """pyNote  Copyright (c) 2015  Adonis Megalos
This program comes with ABSOLUTELY NO WARRANTY.
This is free software, and you are welcome to redistribute it
under certain conditions.
This software is distributed under the GNU GPL v3.""")

menu = Menu(root)
root.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="Open...", command=open_command)
filemenu.add_command(label="Save", command=save_command)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=exit_command)
helpmenu = Menu(menu)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About...", command=about_command)
helpmenu.add_command(label="License", command=license_command)
 
#
textPad.pack()
root.mainloop()

