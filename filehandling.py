#-------------------------------------------------------------------------------------------------------------------------------------------------
import os
import shutil

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
        return ('.jpeg', '.jpg', '.bmp', '.png', '.jpe', '.tif', '.tiff', '.gif', '.dib')
    
    if file_type == 'doc':
        return ('.doc', '.docx')
    
    if file_type == 'excel':
        return ('.xlsx')
    
    if file_type == 'ppt':
        return ('.ppt', '.pptx')
    
    if file_type == 'pdf':
        return ('.pdf')

    if file_type == 'html':
        return ('.html', '.htm')

    if file_type == 'C++':
        return ('.cpp', '.CPP')

    if file_type == 'text':
        return ('.txt')


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

if __name__ == '__main__':
    searchandmovefiles(generateextension('html'), os.getcwd(), 'new folder')
