import os
import re

def promptForOutputFile():
    pattern = "^[a-zA-Z0-9]{1,50}.txt$";
    outputFileName = input("Enter an ouput file that ends in `.txt` ")
    
    # TODO - Check that oututfilename is not inputfilename. 
    if(re.search(pattern, outputFileName)):
        print("You entered: " + outputFileName)
        # TODO - Change input.txt to a variable/function call.
        if not os.path.exists("input.txt"):
            # TODO - Remove line below and Re-Prompt for input file.
            pass
        else:
            with open("input.txt", "r") as file:
                inputFileData = file.read()
        # TODO - Include variables to write.
        try:
            writeToFile(outputFileName, "x", inputFileData)
            return
        except FileExistsError:
            writeToFile(outputFileName, "w", inputFileData)
            # If input file not exists then prompt for a new input file.
            return
    return promptForOutputFile()

def writeToFile(outputFileName, action, inputFileData):
    with open(outputFileName, action) as file:
        file.write("First Name: " + "\n") #+ fN)
        file.write("Last Name: " + "\n") #+ lN)
        file.write("First Integer: " + "\n") #+ fI)
        file.write("Second Integer: " + "\n") #+ sI)
        file.write("Sum of Integers: " + "\n") #+ sumI)
        file.write("Product of Integers: " + "\n") #+ pI)
        # TODO - Use variable to represent name of input file.
        file.write("Input File Name Contents: " + inputFileData)

    if(action == "w"):
        print("Wrote to: " + outputFileName)
    else:
        print("Created and Wrote to: " + outputFileName)
promptForOutputFile()