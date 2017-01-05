import os

def files_in_directory(spath):
    '''
    This function takes the name of a directory 
    and prints out the files within that 
    directory as well as any files contained in 
    contained directories.'''
    for schild in os.listdir(spath):
        print schild
        schild_path = os.path.join(spath , schild)
        if os.path.isdir(schild_path):
            files_in_directory(schild_path)



files_in_directory("../../../github")

