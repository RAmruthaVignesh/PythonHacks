#common operating system support and path name manipulations
import os

#To get the current working directory
def cwd():
    '''This function returns the path of current working directory'''
    return os.getcwd()
#Testcases
current_directory = cwd()
print "The current working directory is" ,current_directory
print "**************************"


#Directory name and base name
def base_directory_name(path):
    '''This function takes the input of a path and 
    prints the basename and directory name'''
    base_name = os.path.basename(path)
    print "The base name is", base_name
    directory_name = os.path.dirname(path)
    print "The directory name is",directory_name
    dir_name_tuple = os.path.split(path)
    print "The directory name using split function is", dir_name_tuple
    print "**************************"

#Testcases
base_directory_name(os.getcwd())

#Joining Two paths
def join_paths(path1,path2):
    '''This function takes in 2 paths ,
    joins them and then returns it'''
    joined_path = os.path.join(path1,path2)
    return joined_path

#testcases
path = join_paths(os.getcwd(),'os_utils.py' )
print "The joined path of current directory and a file is ",path
print "**************************"




