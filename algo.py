from blessed import Terminal
import time

def printData(DataSetOld: list, DataSetNew: list, term, first: bool = False):
    TerminalWidth = term.width
    LocationPillarOne = int(TerminalWidth / len(DataSetNew))
    max_value = max(max(DataSetOld), max(DataSetNew))  # max of both datasets to scale consistently

    if first:
        print(term.clear)
        for i in range(len(DataSetNew)):
            bar_height = int((DataSetNew[i] / max_value) * (term.height - 2))
            for z in range(bar_height):
                with term.location(LocationPillarOne * (i + 1), term.height - bar_height - 1 + z):
                    print(term.blue("#"))
    else:
        for i in range(len(DataSetNew)):
            old_height = int((DataSetOld[i] / max_value) * (term.height - 2))
            new_height = int((DataSetNew[i] / max_value) * (term.height - 2))

            if old_height != new_height:
                # Clear old bar
                for z in range(old_height):
                    with term.location(LocationPillarOne * (i + 1), term.height - old_height - 1 + z):
                        print(' ')

                # Draw new bar
                for z in range(new_height):
                    with term.location(LocationPillarOne * (i + 1), term.height - new_height - 1 + z):
                        print(term.blue("#"))



def bubbleSort(DataSet: list, term):



    first = True

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
            DataSetOld = DataSet.copy()


            if Value1 >= Value2:

                DataSet[i] = Value2
                DataSet[i + 1] = Value1
                DataSetNew = DataSet
                Swapped = True
                LastSwappedIndex = i
                


                #print(term.clear)
                printData(DataSetOld, DataSetNew, term, first)
                first = False



            time.sleep(0.02)

        time.sleep(0.2) 
