#Read a file line by line store it into a variable

def file_read(fname):
        with open (fname, "r") as myfile:
                data=myfile.readlines()
                print(data)
file_read('python1.txt')