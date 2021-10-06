# =============================Exam Third =================================
# =====>Number One ==========
spell = True
text = "ABC"
count = 1
while spell:
    text += "D"
    if len(text) > 6:
        count += 1
    if (count == 5):
        spell = False
print(text)


# =====>Number Two ========
n1 = "HELLO"
n2 = "HELLI"
n3 = "HELLU"
print(n1 + "\n" + n2 + "\n" + n3)



# =======Number Three ======
text = input("Enter string please:")
for i in  range(len(text)):
    print("X")


# ======Number Four ======
score = int(input("Enter Number:"))
if score < 50:
    result = "bad!"
elif 50<=score<=80:
    result = "not bad, not good!"
elif 80<score<=100:
    result = "excellent!"
else:
    result = "are you crazy!"
print(result)


# ========Number Five ======
isTen = True
while  isTen:
    number = int(input("Enter Number: "))
    if number != 10:
        print("Try Again!")
        isTen = True
    elif number == 10:
        print("Win")   
        isTen = False
    

# ========Number Six ========
width = int(input("Enter Width: "))
height = int(input("Enter Hight: "))
text = ""
for h in range(height):
    for w in range(width):
        text += "X"
    text += "\n"
print(text)

# ================================================================
# =================================Exam Fourth ====================
# =========Number One =============
n1 = int(input("First Number:"))
n2 = int(input("Second Number:"))
n3 = int(input("Third Number:"))
moneyWin = 0
has100 = n1 == 100 or n2 == 100 or n3 == 100
has200 = n1 == 200 or n2 == 200 or n3 == 200
has300 = n1 == 300 or n3 == 300 or n3 == 300
if has100 and has200 and has300:
    moneyWin = 10
elif has100 and has200:
    moneyWin = 5
elif has100:
    moneyWin = 2
print(str(moneyWin)+ "dollars")


# ========Number Two =============
text = input("Enter Text: ")
newText = ""
isSignNotGet = True
for char in range(len(text)):
    if text[char] == "'" and isSignNotGet:
        isSignNotGet = False
    elif isSignNotGet:
        newText += text[char]
    elif text[char] == "'" and not isSignNotGet:
        isSignNotGet = True
print(newText)


# =========Number Three ===========
text = input("Enter Word Of a and b: ")
for index in range(len(text)):
    if index % 2 == 0 and text[index] == "a":
        result = "YES"
    elif index % 2 == 1 and text[index] == "b":
        result = "YES"
    else:
        result = "NO"
print(result)


# ========Number Four ===========
numberOfInput = int(input("Enter Those Number: "))
totalNumbers = 0
for n in range(numberOfInput):
    numbers = int(input("Enter each number"))
    totalNumbers += numbers
average = totalNumbers/numberOfInput
print(average)


# ===========================================================
# =========================Exam Fifth =======================
# ===========Number One ============
n = 5
for i in range(n):
    number = int(input("Enter the five number " + str(i) + ": "))
    if number >= 10 and number <=20:
        result = "WIN"
    else:
        result = "LOST"
print(result)
                    # Teacher 1
message = "WIN"
for i in range(5):
    number = int(input())
    if number < 10 or number > 20:
        message = "LOST"
print(message)


                    # One More
message = "WIN"
for i in range(5):
    number = int(input(""))
    if not(number >=10 and number <= 20):
        message = "LOST"
print(message)


# ======One More====
n1 = int(input())
n2 = int(input())
n3 = int(input())
n4 = int(input())
n5 = int(input())
right = n1 >= 10 and n2 >= 10 and n3>= 10 and n4 >=10 and n5 >=10
oneRight = n1 <= 20 and n2 <= 20 and n3 <= 20 and n4 <= 20 and n5 <= 20
if right and oneRight:
    print("WIN")
else:
    print("LOST")

# ===========Number Two ==============
word = input("Enter:")
nA = 0
nSign = 0
score = 0
for i in range(len(word)):
    if word[i] == "A":
        nA += 1
    if word[i] == "$":
        nSign += 1
if nA == 1:
    score = 30 
elif nSign == 2:
    score = 20
elif nSign == 1 and nA == 0:
    score += 10
print(score)

                    # Teacher Do

text = input()
countA = 0
CountDollar = 0
result = 0
for i in range(len(text)):
    if text[i] == "A":
        countA += 1
    if text[i] == "$":
        CountDollar += 1
if countA == 1:
    result = 30
elif CountDollar == 2:
    result = 20
elif CountDollar == 1 and countA == 0:
    result = 10
print(result) 


                # My FRINED DO

word=input()
timeOfWordA=0
timeOfsignDollar=0
points=0
for i in range(len(word)):
    if word[i]=="A":
        timeOfWordA+=1
    elif word[i]=="$":
        timeOfsignDollar+=1
if timeOfWordA==1 and timeOfsignDollar==0:
    points=30
elif timeOfsignDollar==2 and (timeOfWordA==0 or timeOfWordA>1):
    points=20
elif timeOfsignDollar==1 and timeOfWordA==0:
    points=10
print(points)


# ===========Number Three =============
isTwenty = True 
sumOfNumber = 0
while isTwenty:
    number = int(input())
    if number != 10 and number != 12:
        sumOfNumber += number 
    while sumOfNumber >= 20 and isTwenty:
        isTwenty = False
if sumOfNumber == 20:
    result = "WIN"
elif sumOfNumber > 20:
    result = "LOST"
print(result)


                    # MY FRIEND DO
boolean=True
sum=0
while boolean:
    numberinput=int(input())
    if numberinput!=10 and numberinput!=12:
        sum+=numberinput
        if sum>=20:
            boolean=False
if sum==20:
    result="WIN"
elif sum>20:
    result="LOST"
print(result) 




# =============Number Four ==========
isSeventyTwo = True
numberOfEnter = 0
while isSeventyTwo and numberOfEnter < 3:
    number= int(input())
    numberOfEnter += 1
    if number != 72 and numberOfEnter < 3:
        result = "AGAIN"
    if number != 72 and numberOfEnter == 3:
        result = "LOST"
    if number == 72 :
        result = "WIN"
        isSeventyTwo = False
    print(result)

#===========My firend Do =========

notfound=True
theTimeOfInput=0
while notfound:
    enternumber=int(input())
    if enternumber!=72:
        theTimeOfInput+=1
        if theTimeOfInput!=3:
            print("AGAIN")
        else:
            notfound=False
    elif enternumber==72:
        notfound=False
if theTimeOfInput==3:
    result="LOST"
else:
    result="WIN"
print(result)


#=============================================
# =========================Exam Sixth =========
#==============Number One =========
def contains(word,character):
    isCharactersNoInWord = False
    for char in word:
        if char.upper() == character.upper():
            isCharactersNoInWord = True
    return isCharactersNoInWord
word = input("Enter word: ")
character1 = input("Enter Leter: ")
character2 = input("Enter One More Letter: ")
if contains(word,character1) and contains(word,character2):
    message= "VALID"
else:
    message = "NOT VALID"
print(message)


# ===========Number Two ============
def reverse(string):
    reversedString = ""
    for value in string:
        reversedString = value + reversedString
    return reversedString
string = input("Enter String: ")
print(reverse(string))


#============Number Three =========
def multiplyWithinRange(start,end):
    multiplyNumber = start
    for value in range(start+1,end+1):
        multiplyNumber *= value
    return multiplyNumber
start = int(input("Enter Start Num: "))
end = int(input("Enter End Num: "))
if start > end:
    multiplyNumber = 0
else:
    result = multiplyWithinRange(start,end)
    print(result)


#===========Number Four =============
def countChar(word,char):
    timeOfChar = 0
    for value in word:
        for character in value:
            if character == char:
                timeOfChar += 1
    return timeOfChar
word = eval(input("Enter Word In Array: "))
char = input("Enter Character: ")
result = countChar(word,char)
print(result)


#==========Number Five ============
def average(scores):
    totalOfNumbers = 0
    for number in scores:
        totalOfNumbers += number
    return totalOfNumbers/len(scores)
numberOfStudents = int(input("Enter Amount Of Stus: "))
totalAverageOfStudents = 0
finalAverage = 0
for num in range(numberOfStudents):
    scores = eval(input("Enter Score: "))
    totalAverageOfStudents += average(scores)
finalAverage = totalAverageOfStudents/numberOfStudents
print(finalAverage)

#==========One More ===================
def sumScore(list):
    totalScore = 0
    for value in range(len(list)):
        totalScore += list[value]
        resultOfEachStudentAverage = totalScore/len(list)
    return resultOfEachStudentAverage

def average(numberOfStudent):
    totalAverage = 0
    for i in range(numberOfStudents):
        list = eval(input("Enter score to list"))
        totalAverage += sumScore(list)
    return int(totalAverage/numberOfStudents)
numberOfStudents = int(input("enter number: "))
print(average(numberOfStudents))
