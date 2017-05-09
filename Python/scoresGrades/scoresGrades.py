'''SCORES AND GRADES'''
import random

def scoresGrades(num):
    score = 0
    grade = ""
    for i in range(num):
        randNum = random.randint(0,100)
        score = randNum
        if randNum >= 90:
            grade = "A"
        elif randNum >= 80:
            grade = "B"
        elif randNum >= 70:
            grade = "C"
        elif randNum >= 60:
            grade = "D"
        else:
            grade = "F"

        print "Score: ", randNum, "; Your grade is " + grade

scoresGrades(10)
