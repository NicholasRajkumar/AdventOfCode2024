data = []
with open("day2/input.txt") as f:
    for line in f:
        numLine = [int(level) for level in line.split(" ")]
        data.append(numLine)
answer = []

#part1
for rep in data:
    increasingLevels = rep[0] < rep[1]
    increaseDecreaseFlag = True
    adjacentDiff = True

    for i in range(len(rep)):
        if increasingLevels:
            if rep[i-1] >= rep[i]:
                increaseDecreaseFlag = False
            if 1 > rep[i] - rep[i-1] or rep[i] - rep[i-1] > 3:
                adjacentDiff = False
        else:
            if rep[i-1] <= rep[i]:
                increaseDecreaseFlag = False
            if 1 > rep[i-1] - rep[i] or rep[i-1] - rep[i] > 3:
                adjacentDiff = False
    if increaseDecreaseFlag and adjacentDiff:
        answer.append(True)


with open('day2/solution.txt', "w") as f:
    f.write("\n" + "Part 1 Answer: " + str(len(answer)))

#part2
for rep in data:
    increasingLevels = sum(rep[:(len(rep)//2)-1]) < sum(rep[len(rep)//2:])
    print(increasingLevels)
    if not increasingLevels:
        print(rep)
    increaseDecreaseFlag = True
    adjacentDiff = True
    dampener = True



    for i in range(len(rep)):
        if increasingLevels:
            if i is not len(rep)-1:
                if rep[i] >= rep[i+1]:
                    if dampener:
                        dampener = False
                    else:
                        increaseDecreaseFlag = False

        # do the adjacent code

        else:

        if increaseDecreaseFlag and adjacentDiff:
            answer.append(True)

with open('day2/solution.txt', "w") as f:
    f.write("\n" + "Part 2 Answer: " + str(len(answer)))
