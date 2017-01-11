#To read a file
def read_file(spath):
    '''This function takes a file input and reads the file'''
    try:
        with open(spath , 'rw+') as f:
            return f.read()
    except:
        return "No such file exists"

file = read_file("sampletext.txt")
print file




