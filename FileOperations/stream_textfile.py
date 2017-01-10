def stream_textfile_1(path):
    '''This function takes in the path input. 
    It reads the entire file and returns each line in a list'''
    file_x = open(path,'rw+')
    lines = file_x.readlines()
    lines = [line.strip('\n') for line in lines]
    return lines

textfile_1=stream_textfile_1("../FileOperations/sampletext.txt")


def stream_textfile_2(path):
    '''This function takes in the path of the file. 
    It reads the entire file and 
    returns the generator object of all the lines of the file.'''
    lines =open(path, 'rw') 
    for line in lines:
        yield line


text_file_2 = stream_textfile_2("../FileOperations/sampletext.txt")
