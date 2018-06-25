def LongestWord(sen):
    newString = sen
    print(newString)
def numFizzBuzz():
    maxNum = 100
    for i in range(1, maxNum + 1):
        if(i % 3 == 0 and i % 5 == 0):
            print("ThreeFive")
        elif(i % 3 == 0):
            print("Three")
        elif(i % 5 == 0 ):
            print("Five")
        else:
            print(i)
#numFizzBuzz()
def primeFinder(num):
   newNum = num
   i = 1
   output = True
   while num > 1:
       i += 1
       if num % i == 0:
           if 1 < i < newNum:
                output = False
                print(output)
                return 0
           num //= i
   print(output)
#primeFinder(17)
def palindromeFinder(aString):
    aString = aString.replace(" ","")
    #print(aString)
    if aString == aString[::-1]:
        output = True
    else:
        output = False
    print(output)
#palindromeFinder("race car")
def manualMultiplication(firstInt, secondInt):
    k = 0
    output = 0
    for i in range(1, secondInt + 1):
        k += 1
        output += firstInt
        #print(k)
        print(output)
#manualMultiplication(3, 7)
def thousandsWithCommas(number):
    stringNum = str(number)[::-1]
    tempStringNum = ""
    k = 1
    comma_groups = 0

    last_group_reverse = False
    if len(stringNum) % 3 == 0:
            last_group_reverse = True

    for i in stringNum:

        if k % 3 == 0:
            tempStringNum = stringNum[k-3:k] + ',' + tempStringNum
            comma_groups += 1
        k += 1

    rest_index = (comma_groups * 3)
    stringNum = ((tempStringNum) + stringNum[rest_index:])[::-1]

    if last_group_reverse:
        stringNum = tempStringNum[:3][::-1] + tempStringNum[3:(len(tempStringNum)-1)]

    print(stringNum)
thousandsWithCommas(30000000)
#def thousandsWithCommas2ElectricBoogaloo:
