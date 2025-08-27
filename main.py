from blessed import Terminal
import time

term = Terminal()
def printData(DataSet: list):


    
    TerminalWidth = term.width  # Terminal width
    
    # Calculate the space between each pillar
    LocationPillarOne = int(TerminalWidth / len(DataSet))
    
    # Calculate max value in DataSet for scaling purposes
    max_value = max(DataSet)
    
    # Loop through DataSet and print each "bar" in the terminal
    for i in range(len(DataSet)):
        # Scale the Y-coordinate so bars fit within terminal height
        bar_height = int((DataSet[i] / max_value) * (term.height - 2))  # Subtract 2 to avoid going out of bounds
        
        # Print each "bar" at the calculated position

        for z in range(bar_height):
            with term.location(LocationPillarOne * (i + 1), term.height - bar_height - 1 + z):  # Y: Start near the bottom
                print(term.blue("#"))








    


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

    Swapped: bool = True
    LastSwapped = 1
    LastSwappedIndex = len(DataSet) - 1
    while Swapped:
        Swapped = False
        LastSwapped = LastSwappedIndex
        LastSwappedIndex = 0


        for i in range(LastSwapped):

            Value1 = DataSet[i]
            Value2 = DataSet[i + 1]

            if Value1 >= Value2:

                DataSet[i] = Value2
                DataSet[i + 1] = Value1
                Swapped = True
                LastSwappedIndex = i
                #print(f"On loop {i}, Data set now: {DataSet} - Something changed")

            

            #else:
                #print(f"On loop {i}, Data set now: {DataSet} - Nothing changed")


            print(term.clear)
            printData(DataSet)
            #time.sleep(0.01)
                


StringDataSet = str(DataSet)  # Convert list to string
OutputData = [int(x.strip()) for x in StringDataSet[1:-1].split(',') if x.strip()]  # Strip brackets and split by commas

# Now join the OutputData into a comma-separated string
OutputDataString = ", ".join(map(str, OutputData))

print(OutputDataString)  # This will print: "1, 2, 3, 4, ..."

with open("output.txt", "w") as f:
  f.write(OutputDataString)


