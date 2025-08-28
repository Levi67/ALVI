from blessed import Terminal
import time

from algo import bubbleSort

term = Terminal()





print("1 For file input in data.txt, 2 for term input")
DataInput = input()

if DataInput == "1":
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

print("--------------------------")



if Algorithm == "1":

    bubbleSort(DataSet, term)

time.sleep(1)
                


StringDataSet = str(DataSet)  # Convert list to string
OutputData = [int(x.strip()) for x in StringDataSet[1:-1].split(',') if x.strip()]  # Strip brackets and split by commas

# Now join the OutputData into a comma-separated string
OutputDataString = ", ".join(map(str, OutputData))

print(OutputDataString)  # This will print: "1, 2, 3, 4, ..."

with open("output.txt", "w") as f:
  f.write(OutputDataString)


