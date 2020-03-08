sleepTime = []

while(True):

    time = input()

    splitedTime = time.split(" ")

    numbZeros = 0
    for i in range(len(splitedTime)):

        splitedTime[i] = int(splitedTime[i])

        if splitedTime[i] == 0:
            numbZeros += 1

        if i % 2 == 0:

            if splitedTime[i] == 0:
                splitedTime[i] = 24 
        
    if numbZeros >= 4:
        break

    startTime = splitedTime[0]*60 + splitedTime[1]
    endTime = splitedTime[2]*60 + splitedTime[3]

    if endTime <= startTime:
        endTime += 24*60


    sleepTime.append(abs(endTime - startTime))


for i in sleepTime:
    print(i)
