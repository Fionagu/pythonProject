# Illustration 7.4
# Write a program to ask the user to enter lines of text. The user should be able to enter any number of lines. 
# In order to stop, he must enter “\e.” 
# The lines should be appended to an empty list (say L). 
# This list should then be written to a file called lines.txt. 
# The program should then read the lines of lines.txt.

def i_7_4():
    print('Enter text, press \'\\e\' to exit')
    L = []
    i = 1
    line=input('Line number'+str(i)+'\t:')
    while (line!= '\e'):
        L.append(line)
        i+=1
        line=input('Line number'+str(i)+'\t:')
    print(L)

    f=open('lines.txt','w')
    f.writelines(L)
    f.close()

    f=open('lines.txt','r')
    for l in f.readline():
        print(l, end='')
    f.close()


# Illustration 7.5
# Open a file TextFile.txt and write a few lines in it. 
# Now open the file in the read mode and read the first 15 characters from the file. 
# Then read the next five characters. In each step show the position of the cursor in the file. 
# Now, go back to the first position in the file and read 20 characters from the file.

def i_7_5():
    f = open('i_7_5.txt','w')
    f.writelines(['Hi there how are you how old and what do you want', 'how are you'])
    f.close()

    f=open('i_7_5.txt','r')
    str = f.read(15)
    # pos = 
    print('String str\t:'+str)
    print(f.tell())
    str = f.read(5)
    print('String str\t:'+str)
    print(f.tell())

    f.seek(0,0)
    str = f.read(20)
    print('String str\t:'+str)
    print(f.tell())


if __name__ == '__main__':
    # i_7_4()
    i_7_5()

