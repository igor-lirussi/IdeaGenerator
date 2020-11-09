import os
import tkinter as tk

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

if len(data)==0:
    print("NO FILES FOUND.")
    exit()

print("\nLoaded correctly {} files ".format( len(data) ))
for x in range(len(data)):
    print( "-file {} has {} lines".format(x, len(data[x])))

#print(data)
#GUI
window = tk.Tk()
#array for the labels
labels=[]
#creates many frames as the number of files
for x in range(len(data)):
    frame = tk.Frame(master=window, relief=tk.RIDGE, borderwidth=5,  bg="black")
    frame.pack(fill=tk.BOTH, expand=True)
    label = tk.Label(
        master=frame,
        text="Idea "+str(x),
        fg="white",
        bg="black",
        height=5
    )
    label.pack()
    labels.append(label)

#random button
def rand_gen():
    print("The button was clicked!")
    #for all the groups
    for x in range(len(data)):
        #label of the group is a random on in the group
        labels[x]["text"] = data[x][0]

button = tk.Button(master=window, text="Random Generate!", command=rand_gen,
    width=20,
    height=2)
button.pack()

window.mainloop()
#count = 0
# Strips the newline character
#for line in Lines:
#    print("Line{}: {}".format(count, line.strip()))
