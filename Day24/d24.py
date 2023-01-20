def dailyTemperature(Temp):
    answer = []
    step = 0

    def checkForNextBiggerTempIndex(list, value):
        if len(list) == 0:
            return 0
        for i, j in enumerate(list):
            if j > value:
                return i

        return 0

    while step < len(Temp):
        #print(Temp[step:], Temp[step])
        index = checkForNextBiggerTempIndex(Temp[step:], Temp[step])
        answer.append(index)
        step += 1

    return answer


temp1 = [73, 74, 75, 71, 69, 72, 76, 73]
temp = [30,40,50,60]
print(dailyTemperature(temp))

# print(checkForNextBiggerTempIndex(temp, 73))
