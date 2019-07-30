#we are using open(), built in functionality from pythin to open file

def open_and_print(file_to_open):
    try: #tries to run blcok of code
        file = open(file_to_open,'r') #'r is for readin the file'
        file_line_list = file.readlines() # reads the line of file order.txt


        for line in file_line_list:
            print(line.rstrip('\n'))

        file.close()
    except FileNotFoundError as errmsg:
        print("Hi File could be open, please see below")#if it fails it runs this block of code
        print(errmsg)

open_and_print('order.txt')


