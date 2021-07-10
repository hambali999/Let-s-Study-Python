f = open("demofile1.txt", "a")
f.write("\nNow the file has more content!")
f.close()

#open and read the file after the appending:
f = open("demofile1.txt", "r")
print(f.read())