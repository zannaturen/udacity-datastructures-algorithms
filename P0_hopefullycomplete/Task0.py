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
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""
index_last_call = len(calls) -1
print("First record of texts, " + texts[0][0] + " texts " + texts[0][1])
print("Last record of calls, " + calls[index_last_call][0] + " calls "+ \
        calls[index_last_call][1]+ " at time "+ calls[index_last_call][2]+ \
        " lasting "+ calls[index_last_call][3]+ " seconds")