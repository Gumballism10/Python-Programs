f1=open("D:/Python Programs/Myfile.txt")
print(f1.read())
f1.close()
f1=open("D:/Python Programs/Myfile1.txt","w")
f1.write("I like coding with my teacher")
f1.close()
f1=open("D:/Python Programs/Myfile1.txt","a")
f1.write("paul and hasham are nice")
f1.close()