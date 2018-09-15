from xlrd import open_workbook
from Essay import Essay
from sklearn import tree
import matplotlib.pyplot as plt

wb = open_workbook('training_set_rel3.xlsx')
essayMasterList = []

for sheet in wb.sheets():
    numOfRows = sheet.nrows
    for row in range(1700):
        essayID = (sheet.cell(row+1,0).value)
        essaySet = (sheet.cell(row+1,1).value)
        plainData = (sheet.cell(row+1,2).value)
        score1 = (sheet.cell(row+1,3).value)
        score2 = (sheet.cell(row+1,4).value)
        essayMasterList.append(Essay(essayID, essaySet, plainData, score1, score2))


Features = []
Scores = []
for i in range(len(essayMasterList)-100):#1701-100 = 1601
    featureList = []
    featureList.append(essayMasterList[i].wordCount)
    featureList.append(essayMasterList[i].sentenceCount)
    featureList.append(essayMasterList[i].numOfNouns)
    featureList.append(essayMasterList[i].numOfAdverbs)
    featureList.append(essayMasterList[i].numOfAdjectives)
    featureList.append(essayMasterList[i].numOfVerbs)
    Features.append(featureList)
    Scores.append(essayMasterList[i].scores[0] + essayMasterList[i].scores[1])

clf = tree.DecisionTreeClassifier()
clf = clf.fit(Features, Scores)
"""
testFeatures = []
testScores = []
temp = []
temp.append(essayMasterList[-1].wordCount)
temp.append(essayMasterList[-1].sentenceCount)
temp.append(essayMasterList[-1].numOfNouns)
temp.append(essayMasterList[-1].numOfAdverbs)
temp.append(essayMasterList[-1].numOfAdjectives)
temp.append(essayMasterList[-1].numOfVerbs)
testFeatures.append(temp)
testScores.append(essayMasterList[-1].scores[0] + essayMasterList[-1].scores[1])
"""



#print(essayMasterList[-1].plainText)
#print("Atual Score: " + str(testScores[0]))
#print("Predicted Score: ")


actualScores = []
predictedScores = []

for i in range(100):
    testFeatures = []
    temp = []
    temp.append(essayMasterList[-i-1].wordCount)
    temp.append(essayMasterList[-i-1].sentenceCount)
    temp.append(essayMasterList[-i-1].numOfNouns)
    temp.append(essayMasterList[-i-1].numOfAdverbs)
    temp.append(essayMasterList[-i-1].numOfAdjectives)
    temp.append(essayMasterList[-i-1].numOfVerbs)
    testFeatures.append(temp)
    actualScores.append(essayMasterList[-i-1].scores[0] + essayMasterList[-i-1].scores[1])
    predictedScores.append(clf.predict(testFeatures)[0])

plt.plot(actualScores, label='Actual Scores')
plt.plot(predictedScores, label='Predicted Scores')
plt.legend()
plt.show()

