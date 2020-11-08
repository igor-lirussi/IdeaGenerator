import os

#find txt files
print("\nFiles:")
files= []
for file in os.listdir("./files"):
    if file.endswith(".txt"):
        print("-found " + file)
        files.append(file)

#read lines for each file
data = []
for file in files:
    file_curr = open(os.path.join("./files", file), 'r')
    Lines = file_curr.readlines()
    data.append(Lines)
    #print lines
    #count = 0
    #for line in Lines:
    #    count += 1
    #    print("Line {}: {}".format(count, line.strip()))

print("\nLoaded correctly {} files ".format( len(data) ))
for x in range(len(data)):
    print( "-file {} has {} lines".format(x, len(data[x])))

#print(data)

#count = 0
# Strips the newline character
#for line in Lines:
#    print("Line{}: {}".format(count, line.strip()))