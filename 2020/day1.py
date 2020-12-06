import csv

#Get numbers as a list
numbers = []
with open('2020/day1.csv') as csvfile:
    data = list(csv.reader(csvfile))
for i in data:
    numbers.append(int(i[0]))

for num in numbers :
    correctSum = False
    for num2 in numbers:
        for num3 in numbers :
            if num + num2 + num3 == 2020 :
                print str(num * num2 * num3)
                correctSum = True
                break
        if correctSum == True :
            break
    if correctSum == True :
            break

        
    




