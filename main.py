from blessed import Terminal
import time#
import os

from algo import bubbleSort

term = Terminal()

default_data_string = "52, 75, 34, 98, 41, 12, 64, 56, 87, 90, 13, 61, 47, 24, 76, 18, 33, 56, 89, 49, 26, 63, 58, 35, 73, 81, 65, 70, 22, 11, 28,"




print("1 For file input in data.txt, 2 for term input")
DataInput = input()

if DataInput == "1":

    if not os.path.exists("data.txt"):
        with open("data.txt", 'w') as f:
            f.write(default_data_string)

    Data = open("data.txt").read()


elif DataInput == "2":
    print("Whats ur data")
    Data = input()
 
else:
    print("No corresponding value entered")


DataSet = [int(x.strip()) for x in Data.split(',') if x.strip()]


print(f"Your data is: {DataSet}")

print("Which algorithm do you want, Bubble sort: 1; ")
Algorithm = input()



if Algorithm == "1":
    
    bubbleSort(DataSet, term)

else:
    print("No valid algorithm chosen, abord")
    print("!!! Output will be the same as input !!!")

time.sleep(1)
                


StringDataSet = str(DataSet)  # Convert list to string
OutputData = [int(x.strip()) for x in StringDataSet[1:-1].split(',') if x.strip()]  # Strip brackets and split by commas

# Now join the OutputData into a comma-separated string
OutputDataString = ", ".join(map(str, OutputData))

print(OutputDataString)  # This will print: "1, 2, 3, 4, ..."

with open("output.txt", "w") as f:
  f.write(OutputDataString)


