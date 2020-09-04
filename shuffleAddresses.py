# addresses-text2.txt
# addresses-text.txt

import os.path
import os
import time

helper = 0

def file_read_and_writeUpdatedFiles(fname):
        content_array = []
        counter = 0
        totheend = ''
        with open(fname) as f:
                #Content_list is the list that contains the read lines.     
                for line in f:
                        if counter == 0:
                                counter = counter + 1
                                totheend = line.rstrip('\n')
                        else:
                                content_array.append(line.rstrip('\n'))
                content_array.append(totheend)
                print(content_array)
                counter = 0

        with open("addresses-text2.txt", "w") as txt_file2:
                for line2 in content_array:
                        txt_file2.write(line2 + "\n") # works with any number of elements in a line
				
        with open("addresses-text.txt", "w") as txt_file:
                for line in content_array:
                        if counter == 0:
                                counter = counter + 1
                                #txt_file.write(line + "\n") # works with any number of elements in a line
                                txt_file.write(line) # works with any number of elements in a line

while True:
    #helper = 0
    if os.path.exists(".\shuffleAddresses.yes.txt") and helper ==0 :
        # Creates a new file 
        with open(".\shuffleAddresses.TRY.AGAIN.LATER.txt", "w") as fp: 
            pass
            # To write data to new file uncomment 
            # this fp.write("New file created") 
        #os.mknod(".\shuffleAddresses.TRY.AGAIN.LATER.txt")
        file_read_and_writeUpdatedFiles("addresses-text2.txt")
        helper = helper + 1
    if not os.path.exists(".\shuffleAddresses.yes.txt"):
        helper = 0
    time.sleep(1)
        