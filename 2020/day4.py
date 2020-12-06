#Solution for Day 4 of Advent of Code 2020 Part 2
#Prints out count of valid passports from file  'day4.csv'

import csv
import re
from collections import Counter


valid = 0 #count of valid passports
requiredFields = ["byr","iyr","eyr","hgt","hcl","ecl","pid"]
validECLs = ["amb","blu","brn","gry","grn","hzl","oth"]

#Takes a Passport as parameter and returns True if Valid
def passportValid(passport):
    passportkeys = []
    passdata = passport.split()
    for pair in passdata:
        key = pair.split(":")[0]
        passportkeys.append(key)
    
    #First check if the passport contains all the required fields
    if (all(x in passportkeys for x in requiredFields)):
        #Then check if each of the key value pairs is valid
        return all(validKeyValue(passport) for passport in passdata)
    else:
        return False
        
#Checks if the key value pair in the passport is valid
def validKeyValue(string):
    key = string.split(":")[0]
    value = string.split(":")[1]

    if key == "byr":
        return withinYears(value, 1920, 2002)
    elif key == "iyr":
        return withinYears(value, 2010, 2020)
    elif key == "eyr":
        return  withinYears(value, 2020, 2030)
    elif key == "hgt":
        return  validHGT(value)
    elif key == "hcl":
        return  validHCL(value)
    elif key == "ecl":
        return  validECL(value)
    elif key == "pid":
        return  validPID(value)
    elif key == "cid":
        return True
    else: return False
    
    

def withinYears(string, min, max):
    if len(string) != 4:
        return False
    else:
        year = int(string)
        return year >= min and year <= max  

def validHCL(string):
    match = re.search(r'^#(?:[0-9a-fA-F]{3}){1,2}$', string)
    return bool(match)

def validECL(string):
    return string in validECLs


def validPID(string):
    return len(string) == 9

def validHGT(string):
    match = re.match(r"([0-9]+)([a-z]+)", string, re.I)
    if match:
        items = match.groups()
        if items[1] == "cm":
            return int(items[0]) >= 150 and int(items[0]) <= 193
        elif items[1] == "in":
            return int(items[0]) >= 59 and int(items[0]) <= 76
        else: return False
    else: return False 


with open('2020/day4.csv') as csvfile:
    datapre = csvfile.read()
    data1 = datapre.replace("\n\n", "@")
    data2 = data1.replace("\n", " ")
    data3 = data2.replace("@", "\n")
    data =  data3.splitlines()
for passport in data:
    if passportValid(passport):
        valid +=1
    
print valid







