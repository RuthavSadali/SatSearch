import json


class Scores():

    def most_tests(self):
        json_obj = json.load('data.json')

        numtests = 0
        nameSchool = ''

        for thing in json_obj:
            if thing == 'data':
                temp = json_obj[thing]
                if int(temp(10)) > numtests:
                    numtests = temp(10)
                    nameschool = temp(9)
        return (nameSchool, numtests)

    def best_score(self):
        json_obj = json.load('data.json')

        score = 0
        nameSchool = ''

        for thing in json_obj:
            if thing == 'data':
                temp = json_obj[thing]
                totScore = int(temp(11)) + int(temp(12)) + int(temp(13))
                if totScore > score:
                    score = totScore
                    nameSchool = temp(9)
        return (nameSchool, score)

    def best_score_small(self):
        json_obj = json.load('data.json')

        score = 0
        nameSchool = ''

        for thing in json_obj:
            if thing == 'data':
                temp = json_obj[thing]
                if temp(10) < 51:
                    score = int(temp(11)) + int(temp(12)) + int(temp(13))
                    nameSchool = temp(9)
        return (nameSchool, score)

    def x_most_tests(self, x):
        json_obj = json.load('data.json')

        arr = []
        prevTestScores = []
        highTests = 0
        schoolname = ''
        isOG = True

        for x in range (0, 10):
            for thing in json_obj:
                if thing == 'data':
                    temp = json_obj[thing]
                    numtests = int(temp(10))
                    if numtests > highTests:
                        for t in prevTestScores:
                            if t == numtests:
                                isOG = False
                        if isOG == True:
                            highTests = numtests
                            schoolname = temp(9)
            prevTestScores[x] = highTests
            arr[x] = (schoolname, highTests)
            highTests = 0
            schoolname = ''
            isOG = True

        return prevTestScores

    def x_highest_scores(self, x):
        json_obj = json.load('data.json')

        arr = []
        prevTestScores = []
        scorebeingtested = 0
        schoolname = ''
        isOG = True

        for x in range (0, 10):
            for thing in json_obj:
                if thing == 'data':
                    temp = json_obj[thing]
                    score = int(temp(11)) + int(temp(12)) + int(temp(13))
                    if score > scorebeingtested:
                        for t in prevTestScores:
                            if t == score:
                                isOG = False
                        if isOG == True:
                            scorebeingtested = score
                            schoolname = temp(9)
            prevTestScores[x] = scorebeingtested
            arr[x] = (schoolname, scorebeingtested)
            scorebeingtested = 0
            schoolname = ''
            isOG = True

        return prevTestScores
