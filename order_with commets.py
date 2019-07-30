#we are using open(), built in functionality from pythin to open file

# try: #tries to run blcok of code
#     file = open('orders.tex')
#
# except: #if it fails it runs this block of code
#     print('File could not open!')

try: #tries to run blcok of code
    file = open('order.txt','r') #'r is for readin the file'
    file_line_list = file.readlines() # reads the line of file order.txt
    # print(type(file_line_list))
    for line in file_line_list:
        print(line.rstrip('\n'))

    file.close() #if you don't close it you can cause a lock in the file -
    # such as sending email which has a doc open cant do it

except FileNotFoundError as errmsg:
    print("Hi File could be open, please see below")#if it fails it runs this block of code
    print(errmsg)
    #raise #sends the default error and stops the code HERE line 16 and after will not run
    print('hey')

