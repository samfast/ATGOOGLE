

def answer(s):
    sSet=set(s);
    check=0
    print(sSet)
    sDict={}
    for key in sSet:
        sDict[key]=s.count(key)
    minValue=1000000
    for k, v in sDict.items():
        if v < minValue and len(s)%v==0 and v!=1000000:
            minValue=v
    while minValue==  1000000:
        print('this cake can only be given to 1 minion')
        actualPeople=1
        return actualPeople
    maxPeople=minValue
    print(maxPeople,"are the max people")

    for actualPeople in range(maxPeople):
        actualPeople=maxPeople-actualPeople
        #print(actualPeople)
        print('the length of s is',len(s))
        checkSize=len(s)/maxPeople
        for test in range(0,len(s),checkSize):
            firstSlice=str(s[0:checkSize])
            print('the firstSlice is ',firstSlice)
            ntestsize=test+checkSize
            testbeg=test
            teststring=str(s[testbeg:ntestsize])
            print('the teststring is',teststring)
            if  firstSlice!=teststring:
                print('fail for division btn',test)
                break
            else:
                print ('s is divisible among',test)
                check=test
                print(check)

        print('this are the actualPeople',actualPeople)
        return actualPeople


answer("bababababa")



#Test.assert_equals(answer(list("babaababaa")), 2)
