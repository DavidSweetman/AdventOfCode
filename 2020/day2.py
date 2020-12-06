#Solution for Day 2 of Advent of Code 2020
#Prints out count of valid passwords from file  'day3.csv'

#Get passwords as a list
import csv
from collections import Counter
results = []
with open('2020/day2.csv') as csvfile:
    data = list(csv.reader(csvfile))

#Function to check validity for Part 1
def passwordMatch(password):
    count = Counter(password[3])
    countResult = count[password[2]]
    if countResult >= password[0] and countResult <= password[1] :
        return True
    else:
        return False

#Function to check validity for Part 2
def passwordMatch2(password):
    string = password[3]
    index1 = password[0] - 1
    index2 = password[1] - 1
    letter = password[2]

    if string[index1] == letter and string[index2] == letter :
        return False
    elif string[index1] == letter or string[index2] == letter :
        return True
    else:
        return False

options = []

for d in data:
    x = d[0].split()
    newItem = []
    n1 = x[0].split('-')
    newItem.append(int(n1[0]))
    newItem.append(int(n1[1]))
    newItem.append(x[1].replace(':',''))
    newItem.append(x[2])
    options.append(newItem)

answer = filter(passwordMatch, options)
print len(answer)

answer2 = filter(passwordMatch2, options)
print len(answer2)




