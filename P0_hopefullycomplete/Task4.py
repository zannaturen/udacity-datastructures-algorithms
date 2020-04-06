"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""
doesCall = set()
isCalled = set()
isTexted = set()
doesText = set()

for item in calls:
    isCalled.add(item[1])
    doesCall.add(item[0])

for item in texts:
    doesText.add(item[0])
    isTexted.add(item[1])

telemarketers = []

for number in doesCall:
    if number not in isCalled and number not in isTexted and number not in doesText:
        telemarketers.append(number)

telemarketers.sort()
print("These numbers could be telemarketers: ")
for number in telemarketers:
    print(number)