import os

def full_path_extension(extension):
    extension = "."+str(extension)
    for root, dirs, files in os.walk('.'):
        for file in files:
            if file.endswith(extension):
                full_path_file = os.path.join(root,file)
                return full_path_file
            
def full_path_file(name):
    for root, dirs, files in os.walk('.'):
        for file in files:
            if file == name :
                full_path_file = os.path.join(root,file)
                return full_path_file       
            
