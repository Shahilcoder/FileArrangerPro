import os
import shutil
import tkinter
from tkinter import filedialog
from tkinter import *
from PIL import ImageTk, Image

def movethem(old_path, new_path):
    """
    move the file from old path to new path
    """
    shutil.move(old_path, new_path)


def createnewfolder(folder_name):
    """
    creates new folder if the folder does not exists already
    """
    if os.path.isdir(folder_name) is False: #if the folder does not exist
        os.mkdir(folder_name)
    return folder_name

def generateextension(file_type):
    """
    generate tuple of extensions according to file type
    """
    if file_type == 'image':
        return ('.jpeg', '.jpg', '.bmp', '.png', '.jpe', '.tif', '.tiff', '.gif', '.dib', '.JPEG', '.JPG', '.BMP', '.PNG', '.JPE', '.TIF', '.TIFF', '.GIF', '.DIB')
    
    if file_type == 'doc':
        return ('.doc', '.docx', '.DOC', '.DOCX')
    
    if file_type == 'excel':
        return ('.xlsx', '.XLSX')
    
    if file_type == 'ppt':
        return ('.ppt', '.pptx', '.PPT', '.PPTX', '.pot', '.POT')
    
    if file_type == 'pdf':
        return ('.pdf', '.PDF', '.odt', '.ODT')

    if file_type == 'html':
        return ('.html', '.htm', '.HTML', '.HTM')

    if file_type == 'C++':
        return ('.cpp', '.CPP')

    if file_type == 'text':
        return ('.txt', '.TXT')


def searchandmovefiles(extensions, parent_folder, new_folder_name):
    """
    extensions: tuple of all extensions relating to a file type
    parent_folder: the folder from where you want to arrange the files
    new_folder_name: the name of the folder where a type of file will be moved
    """
    for root, dirs, files in os.walk(parent_folder):
        for file in files:
            #for each file in the files 'list'
            for extension in extensions:
                #for each file having desired extionsion
                if file.endswith(extension):
                    old_path = os.path.join(root,file)

                    #create folder where the file will be moved
                    folder = createnewfolder(new_folder_name)
                    new_path = os.path.join(folder, file)

                    movethem(old_path, new_path)

def browse_folder():
	"""
	this function opens a choose folder dialog box and sets the address
	of folder to the folder_entry
	"""
	folder_path = filedialog.askdirectory()
	folder_entry.insert(0,folder_path)

def arrange():
	"""
	moves the file of same type with the help of functions of 
	filehandling module
	"""
	file_type = file_type_var.get()
	extensions = generateextension(file_type)
	parent_folder = folder_entry.get()
	new_folder_name = file_type_var.get()
	searchandmovefiles(extensions, parent_folder, new_folder_name)


#creating window

master = Tk()

#window configuration

master.title("File Arranger Pro")
#master.minsize(550, 500)
master.config(bg="#FFF8DC")

#The tile

Title = Message(master, text="choose a type of file and the folder containing that type of file\n"
	"the program will arrange all files of that type into\n"
	"new folder with same name as type", bg="#F0F00F")
Title.grid(row=0, column=1, pady=20)

#attaching main image
"""
main_image = Image.open('image.jpg')
logo = ImageTk.PhotoImage(main_image)

panel = Label(master, image=logo)
panel.grid(row=1, column=1)
"""
#the file type selection dropdown menu

file_type_var = StringVar(master)
file_type_var.set("text")

file_label = Label(master, text="file type : ", bg="#FFF8DC")
file_label.grid(row=2, column=0)
file_type_drop_box = OptionMenu(master, file_type_var, "text", "image", "pdf", "doc", "excel", "ppt", "html", "C++")
file_type_drop_box.grid(row=2, column=1, sticky='W')

#choose folder section

choose_folder_label = Label(master, text="choose folder ", bg="#FFF8DC")
choose_folder_label.grid(row=3, column=0)
folder_entry = Entry(master, width=60, bg="#FFB6C1")
folder_entry.grid(row=3, column=1, sticky='W')
#the browse button
browse_button = Button(master, text="browse", bg = "#0FF4FF", command=browse_folder)
browse_button.grid(row=3, column=2, sticky='W', pady=10, padx=20)

#the move button
arrange_button = Button(master, text="arrange", bg = "#00F4FF", command=arrange)
arrange_button.grid(row=4, column=0, columnspan=2, pady=10, padx=20)

#the close button
close_button = Button(master, text="close", bg = "#00F4FF", command=master.destroy)
close_button.grid(row=5, column=0, columnspan=2, pady=10, padx=20)


#developer's sign
sign_label =  Label(master, text="Made by Shahil Hussain", bg="#FFF8DC")
sign_label.grid(row=5, column=2, pady=10)

#running the loop of window
master.mainloop()
