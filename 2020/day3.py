#Solution for Day 3 of Advent of Code 2020
#Prints out product of the number of trees encounterd on the map in 'day4.csv' when traversed for different slopes

#Get Map as a list with each row of trees and spaces as an element string
import csv
from collections import Counter
results = []
with open('2020/day3.csv') as csvfile:
    data = list(csv.reader(csvfile))

#Slope Values
slopes = [[1,1],[3,1],[5,1],[7,1],[1,2]]



string = data[0]
#Width of the map
width = len(string[0])
#Height of the map
height = len(data)


def treeCount (slope):
    x = 0
    y = 0
    #Running total of trees encountered
    trees = 0
    while y < height - 1 :
        y += slope[1]
        x += slope[0]
        x = x % width #Modulo as repeating Map along X Axis

        line = data[y]
        string = line[0]
        char = string[x]
        if char == '#' :
            trees = trees + 1

    return trees

total = 1
for s in slopes:
    countTree = treeCount(s)
    total = total * countTree

print total







