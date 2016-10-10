import math

#clients-per-day expectation
CONST_EXPECT = 1.6

#collect number of shifts in the week, number of hours in the week, calculate float clients per day
numShifts = input("Please enter the number of shifts you plan to work this week\n")
numHours = input("Please enter the number of hours you plan to work this week\n")
clientsPerDay = ((numHours*CONST_EXPECT)/numShifts)
print "You need to take", int(numHours*CONST_EXPECT), " clients through the week, or", clientsPerDay, "per day.\n"
print "Since you can only take whole numbers of clients, here is a possible breakdown per day of your week:\n"

#determine remainder of clients, rounded up
remainder = math.ceil(clientsPerDay%numShifts)

#build week list, starting on Sunday --- #enum challenging in 2.7?
weekList = []
for count in range(0, 7):
    weekList.insert(count, math.floor(clientsPerDay))
#for count in range(0, numShifts):
#    weeklist[count] += 1
for count in range(0, 7):
    print weekList[count]
    