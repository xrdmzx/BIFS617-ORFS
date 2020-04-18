import re
import os
from os import path

### INPUT PROCESS PRIMARILY CODED BY RONALD ZAMBRANO ###

# function to validate file exists
def  input_validation():
    for i in range(5):
        file_input = input("Enter name of Fasta File: ")
        if path.isfile(file_input) == False:
            if i == 4:
                print("you did not enter a valid file name. tries exceeded. manually verify file path and restart module. ")
            else:
                print("you did not enter a valid file name. try again. ")
        else:
            return(file_input)
        
# ask for input and validate it       
file_input = input_validation()

# create dictionary for fasta headers and sequences
fasta_dictionary = {}

# seperate fasta file headers from sequences
with open(file_input) as fasta:
    header = None
    sequence = ""

    for line in fasta:
        # find header
        if line.startswith(">"):
            if header and sequence:
                fasta_dictionary [header] = sequence
            sequence = ""
            # strip new line char
            header = line.rstrip()
        else:
            # strip new line char and remove spaces and make every char uppercase
            sequence += line.rstrip().replace(" ", "").upper()
            
# separate special case for last header and sequence
    if header and sequence:
        fasta_dictionary [header] = sequence
        sequence.replace(" ", "")

# ask user for the minimum orf to search for.
orf_search = input("Enter the minimum ORF to search (default is 50 bases): ")
# if no entry = 50
if orf_search == "":
    orf_search = 50

### ---------------------- DELETE FROM FINAL CODE  --------------------- ###
# test print to show headers and corresponding sequences are in dictionary
for header, sequence in fasta_dictionary.items():
    print("{}: {}".format(header, sequence))

# print orf search min
print(orf_search)
    
### ----------------------------------------- --------------------------------------------  ###
    

