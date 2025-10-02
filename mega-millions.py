import random as rd

#Initialize empty lists
lottoNumbers = []

#Initialize variables
num = 0
megaBallNumber = 0
tickets = 0

#Business Logic
tickets = int(input("How many tickets would you like? ")) # query user on number of tickets

#Print Ticket Header Logic
if tickets < 1:                       #conditional statement based on ticket input
    print("You didn't buy any Mega Millions Tickets\n")
elif tickets == 1:
    print("My Mega Millions Ticket:\n")
else:
    print (f"My {tickets} Mega Millions Tickets:\n")

#Generate Tickets and Output
for t in range (tickets):             #using the number of tickets from the user, create a loop
    lottoNumbers = []                 #initialize the list back to 0
    while len(lottoNumbers) < 5:      #additional control value limiting to 5 numbers
        num = rd.randint(1,76)        #generate random number between 1 and 76
        if num not in lottoNumbers:   #check for duplicates
            lottoNumbers.append(num)  #append number to list
    lottoNumbers.sort()               #sort list
    megaBallNumber = rd.randint(1,25) #generate 2 digit random number

    #Output
    for num in lottoNumbers:          #for loop outputting numbers
        print(f"{num:02d}", end=" ")  # add 2-digit numbers with space between 
    print(f"Mega Ball: {megaBallNumber:02d}") #add megaball text and number