import random
def getAnswer(answerNumber):
    if answerNumber == 1:
        return "It is certain"
    elif answerNumber == 2:
        return "Yes"
    elif answerNumber == 3:
        return "No"

r = random.randint(1,3)
fortune = getAnswer(r)
print(fortune)
