f = open("demofile1.txt", "w")
f.write("Hey this is the first line! \n")
f.write("Hey this is the second line! \n")
f.write("Hey this is the third line!")

f.close()

#open and read the file after the appending:
f = open("demofile1.txt", "r")
print(f.read())