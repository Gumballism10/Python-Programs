file = open('D:/Python Programs/Myfile.txt','r')
print(file.read())
file.close()
file = open('D:/Python Programs/Myfile.txt','r')
print("/n Read in parts /n")
print(file.read(8))
print(file.readline())
file.close()
file = open('D:/Python Programs/Myfile.txt','a')
file.write("Hi! I am Penguin and I am 1 yr old.")
file.close()
file_write = open('D:/Python Programs/Myfilenew.txt', 'w')
file_write.write( "File in write mode ...")
file_write.write("Hi! I am Penguin. I am 1 yr. old ")
file_write.close()
