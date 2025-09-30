# Import the random package.
import random as rd

# Create an empty list called lottoNumbers.
#####
#lists
#####
lottoNumbers = []                        # create an empty list of integers
uniquelottoNumbers = []                  # create a unique list of integers
formatteduniquelottoNumbers = []         # create a formatted unique list of integers

#####
#variables#
#####
lottoNumber = 0                          # lotto number variable
loopCount = 0                            # initalize a loop count variable

#####
#functions
#####
#formatteduniquelottoNumbers():
#megaBallNumber():

#####################
#BUSINESS LOGIC
#####################

#####
#A
#####

# Use a for loop to iterate exactly 5 times.
    
    # Each time through the loop:
    # Generate a lotto number in the form of a random integer from 1 to 76.
    # Store this value in a variable called lottoNumber.
        
    # Add lottoNumber to lottoNumbers.
    # Don't worry right now about duplicate numbers.

lloopCountt = 0
for _ range(5):                          # loop eactly five times
    lottoNumber = rd.randint(1,76)       # generate a random integer
    lottoNumbers.append(lottoNumber)     # add (append) random integer to the list
#   loopCount = loopCount + 1            # increment on the loop count each time
    
# Generate one Mega Ball random integer from 1 to 25.
# Store in a variable called megaBallNumber.

def megaBallNumber():
    return rd.randint(1,26)              # generate a random integer as function

# Sort the lotto numbers from least to greatest (persist the changes).

lottoNumbers = sorted(lottoNumbers)      # sort lotto numbers persistently

#####
#B
#####

# Use a for UNIQUE loop to iterate exactly 5 times.
    
    # Each time through the loop:
    # Generate a unique lotto number in the form of a random integer from 1 to 76.
    # Store this value in a variable called lottoNumber.
        
    # Add lottoNumber to uniquelottoNumbers.
    # Worry about duplicate numbers.

while len(uniquelottoNumbers) < 5:       # loop eactly five times
    uniquelottoNumber = rd.randint(1,77) # generate a random integer
    uniquelottoNumbers.append(uniquelottoNumber)     # add (append) random integer to the list
    if uniquelottoNumber not in uniquelottoNumbers:   # check uniqueness
        uniquelottoNumbers.append(uniquelottoNumber) #add omnly if unique
        
# Sort the lotto numbers from least to greatest (persist the changes).

uniquelottoNumbers = sorted(uniquelottoNumbers)     # sort lotto numbers persistently

#####
#C
#####
# Use a for FORMATTED unique loop to iterate exactly 5 times.
    
    # Each time through the loop:
    # Generate a unique lotto number in the form of a random integer from 1 to 76.
    # Store this value in a variable called lottoNumber.
        
    # Add lottoNumber to uniquelottoNumbers.
    # Worry about duplicate numbers.
    # Sort the lotto numbers from least to greatest (persist the changes).

def formatteduniquelottoNumbers():
    return sorted(rd.sample(range(1,77),5))     # generate 5 unique random integers


#####
#D
#####
# ITERATE a loop within a loop
    
iterations = int(input("How many tickets would you like?"))

# Generate the example output.
#####################
#DISPLAY OUTPUT
#####################

#####
#Part A Answer
#####
print("A - Generate a Mega Millions Ticket\n")
print(f"My Mega Millions Ticket\n")      # print lotto numbers each on a separate line
for num in lottoNumbers:
    print(num)
print()
print(f"Mega Ball: {megaBallNumber()}\n")  #print function
print("==========================================")
#####
#Part B Answer
#####

print("B - Generate A UNIQUE Mega Millions Ticket\n")
print(f"My Mega Millions Ticket\n")      
for num in uniquelottoNumbers:
    print(num, end=" ")         # print lotto numbers on a single line
print(f"Mega Ball: {megaBallNumber()}")
print("==========================================")
print()

#####
#Part C Answer
#####

print("C - Generate a FORMATTED Unique Mega Millions Ticket\n")
print(f"My Mega Millions Ticket\n")      # print lotto numbers each on the same line
for num in formatteduniquelottoNumbers():
    print(f"{num:02d}", end=" ")
print(f"Mega Ball: {megaBallNumber()}")
print("==========================================")
print()

# Use a loop to iterate over the numbers in lottoNumbers.

print(f"D - Iterate {iterations} times through a loop of loops\n")
print(f"My {iterations} Mega Millions Ticket\n")      # print lotto numbers each on the same line
for i in range (iterations):                          # print for number of iterations
    for num in formatteduniquelottoNumbers():         # print formatted, unique lottery numbers
        print(f"{num:02d}", end= " ")      
    print(f"Mega Ball: {megaBallNumber()}")           # print Mega Ball number
    print()
