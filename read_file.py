try:
    file=open('simple.txt','r')
    read_file=file.read()
    print(read_file)
    file.close()
except FileNotFoundError:
    print('File Not Found')
