import sys
sys.path.append('../FileOperations/')
from stream_textfile import *

def get_mini_batch(gen_file,batch_size):
    '''This function takes the input of the generator object and batch size.
    It reads the generator object and returns 1 batch'''
    try:
        mini_batch = [next(gen_file).strip('\n') for i in range(batch_size)]
        return mini_batch
    except:
        return None


def disp_in_batch(path,batch_size):
    '''This function takes in the path of the input file and batch size. This function reads the file and gives the entire file in batches'''
    #Store the entire file in a generator object
    text_file=stream_textfile_2(path)
    flag = []
    #Receive batches of the text file
    while flag !=None:
        flag= get_mini_batch(text_file,batch_size)
        if flag !=None:
            print flag


disp_in_batch("../FileOperations/sampletext.txt",2)
