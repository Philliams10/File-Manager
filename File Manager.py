

import os
import easygui
from tkinter import messagebox as mb
import tkinter as tk
import shutil


# open a file box, called whenever we need to select a file
def openWindow():
    # .fileopenbox returns the path of the chosen file as a string
    read = easygui.fileopenbox()
    return read

# openFile function
def openFile():
    # call openWindow
    string = openWindow()
    try:
        os.startfile(string)
    except:
        mb.showinfo('confirmation', "File Not Found!")

# copyFile function
def copyFile():
    # call openWindow, store path in source1
    source1 = openWindow()
    # destination for the file copy
    destination1 = tk.filedialog.askdirectory()
    # copies the file
    shutil.copy(source1, destination1)
    mb.showinfo('confirmation', "File Copied!")

# deleteFile function
def deleteFile():
    # calls openWindow, store path in d_file
    d_file = openWindow()
    # if the file exists, delete it
    if os.path.exists(d_file):
        os.remove(d_file)
    else:
        mb.showinfo('confirmation', "File Not Found!")

# renameFile function
def renameFile():
    # calls openWindow, store path in file
    file = openWindow()
    # store path of the directory of the chosen file
    path1 = os.path.dirname(file)
    # split the path into root and extension
    extension = os.path.splitext(file)[1]
    print("Enter a new name for the file: ")
    newName = input()
    # combine the newName, extension and the directory path
    path = os.path.join(path1, newName+extension)
    print(path)
    # rename file with what's stored in path
    os.rename(file, path)
    mb.showinfo('confirmation', "File Renamed!")

# moveFile function
def moveFile():
    # calls openWindow, store path in source
    source = openWindow()
    # destination directory for the file
    destination = tk.filedialog.askdirectory()
    # if the source is the destination, notify the user
    # if not, move the file
    if(source==destination):
        mb.showinfo('confirmation', "Source and Destination are the same!")
    else:
        shutil.move(source, destination)
        mb.showinfo('confirmation', "File Moved!")

# make a folder function
def makeFolder():
    # chose a path for the new folder
    newFolderPath = tk.filedialog.askdirectory()
    print("Enter name for new folder: ")
    newFolder = input()
    # add the newFolder to the given path with one directory seperator
    path = os.path.join(newFolderPath, newFolder)
    # create directory
    os.mkdir(path)
    mb.showinfo('confirmation', "Folder Created!")

# remove a folder function
def removeFolder():
    # select and store the path of the to-be deleted folder
    delete_folder = tk.filedialog.askdirectory()
    # delete the folder
    os.rmdir(delete_folder)
    mb.showinfo('confirmation', "Folder Removed!")

# list all files in a folder function
def listFiles():
    # select the folder and store the path
    folder = tk.filedialog.askdirectory()
    # sort the files
    sort_folder = sorted(os.listdir(folder))
    # while loop; print sorted files
    i = 0
    print("Files in ", folder, " folder are: ")
    while(i<len(sort_folder)):
        print(sort_folder[i]+"\n")
        i += 1



root = tk.Tk()

# creating labels and buttons for the GUI
# label
tk.Label(root, text = "File Manager #1", font = (("Arial"), 18), fg = "Purple").grid(row = 5, column = 2)

# open file button
tk.Button(root, text = "Open File", command = openFile).grid(row = 15, column = 2)

# copy file button
tk.Button(root, text = "Copy File", command = copyFile).grid(row = 25, column = 2)

# delete file button
tk.Button(root, text = "Delete File", command = deleteFile).grid(row = 35, column = 2)

# rename file button
tk.Button(root, text = "Rename File", command = renameFile).grid(row = 45, column = 2)

# move file button
tk.Button(root, text = "Move File", command = moveFile).grid(row = 55, column = 2)

# make folder button
tk.Button(root, text = "Make Folder", command = makeFolder).grid(row = 65, column = 2)

# remove folder button
tk.Button(root, text = "Remove Folder", command = removeFolder).grid(row = 75, column = 2)

# list all files in folder button
tk.Button(root, text = "List all Files in Folder", command = listFiles).grid(row = 85, column = 2)


root.mainloop()