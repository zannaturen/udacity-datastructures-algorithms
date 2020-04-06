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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""
def isBangalore(num):
  if num[:5] == '(080)':
    return True
  return False

def testisBangalore():
  assert(isBangalore('(080)1456 789')==True)
  assert(isBangalore('080889')==False)
  assert(isBangalore('(075)990')==False)
  print("isBangalore is working as coded")

def getPrefix(num):
  #The prefix of a mobile number is its first four digits, and they always start with 7, 8 or 9. 
  if num[0]=='7' or num[0]=='8' or num[0]=='9':
    return num[:4]
  #Telemarketers' numbers have no parentheses or space & start with the area code 140.
  if num[:3] == '140':
    return '140'
  #Fixed lines start with an area code enclosed in brackets. The area codes vary in length but always begin with 0
  elif num[0]=='(':
    prefix = ''
    for string in num[:len(num)]:
      if string == ')':
        return prefix+')'
      prefix += string

def testgetPrefix():
  assert(getPrefix('(080)37913009')=='(080)')
  assert(getPrefix('90355 49499')=='9035')
  assert(getPrefix('1408672243')=='140')
  print('getPrefix is working as coded')

calledbyBangalore = []
count_cbB = float(0)
count_isBangalore = float(0)
for call in calls:
  if isBangalore(call[0]):
    count_cbB += 1
    prefix = getPrefix(call[1])
    if prefix not in calledbyBangalore:
       if isBangalore(prefix):
        count_isBangalore += 1
       calledbyBangalore.append(prefix)
    if isBangalore(prefix):
      count_isBangalore += 1

print('The numbers called by people in Bangalore have codes: ')
calledbyBangalore.sort()
for item in calledbyBangalore:
  print(item)
print(str(round((count_isBangalore/count_cbB)*100,2)) + ' percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.')