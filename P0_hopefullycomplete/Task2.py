"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""
#Looking for the phone number with the longest amount of time spent on the phone in calls 
#Do we also need to include time for texts? 
#dictionary w/phone numbers as keys and corresponding call times as values
calltime = {}
#iterates over calls & adds calltime to each phone number entry in dictionary. 
for number in calls:
    if number[0] in calltime.keys() and number[1] in calltime.keys():
        calltime[number[0]] += int(number[3])
        calltime[number[1]] += int(number[3])
    elif number[0] in calltime.keys():
        calltime[number[0]] += int(number[3])
        calltime[number[1]] = int(number[3])
    elif number[1] in calltime.keys():
        calltime[number[0]] = int(number[3])
        calltime[number[1]] += int(number[3])
    else:
        calltime[number[0]] = int(number[3])
        calltime[number[1]] = int(number[3])
#finds max value in dictionary and returns key & value
times = list(calltime.values())
numbers = list(calltime.keys()) 
max_time = max(times)
max_number = numbers[times.index(max_time)]
print(max_number + " spent the longest time, "+ str(max_time) +" seconds, on the phone during September 2016")
