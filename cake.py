import Test

def answer(cake):
    cakeSet=set(cake);
    print(cakeSet)
    cakeDict={}
    for key in cakeSet:
        cakeDict[key]=cake.count(key)
    minValue=1000000
    for k, v in cakeDict.items():
        if v < minValue:
            minValue=v
    maxPeople=minValue
    print(maxPeople,"\n")

    for actualPeople in range(maxPeople):
        actualPeople=maxPeople-actualPeople
        print(actualPeople)

        checkSize=len(cake)/maxPeople

        for test in range(0,len(size),checkSize):
            firstSlice=cake[0:checkSize]
            if  firstSlice!=cake([test:test+checkSize])
                






print("bacdaabacdaa"[0:3])


#Test.assert_equals(answer(list("babaababaa")), 2)
