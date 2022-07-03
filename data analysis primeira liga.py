import pandas as pd
import re
import sys
import operator

csv_filepath = ""

def expected(A,B):
    return 1 / (1 + 10 ** ((B-A) / 400))

def elo(old, exp, score, k=32):
    return old + k * (score - exp)

df = pd.read_csv(csv_filepath, encoding='iso-8859-1')

resultForHomeTeam = []
for row in df['Score']:
    if row.split("-")[0] == row.split("-")[1] :    resultForHomeTeam.append('DRAW')
    elif row.split("-")[0] > row.split("-")[1]:   resultForHomeTeam.append('WIN')
    elif row.split("-")[0] < row.split("-")[1]:   resultForHomeTeam.append('DEFEAT')
    else:           resultForHomeTeam.append('lol?')

week = []
for row in df['Week']:
    week.append("{:02d}".format(int(row.replace("J",""))))
    
df["resultForHomeTeam"] = resultForHomeTeam
df["Week"] = week

df["timeslot"] = df["Season"] + df["Week"]
timeslot = []
for row in df['timeslot']:
    timeslot.append(re.sub("[0-9]{4}\-","",row))

df["timeslot"] = timeslot
#pd.set_option('max_columns', None)

date = []
for row in df['Date']:
    date.append(row.split("/")[2] + "-" + row.split("/")[1] + "-" + row.split("/")[0])

df["Date"] = date
df = df.sort_values(by=['Date'])
#print(df)


bigDict = {}

expectedHome = []
expectedAway = []
outcomeHome = []
outcomeAway = []

for index, row in df.iterrows():
    if row['HomeTeam'] not in bigDict:
        bigDict[row['HomeTeam']] = 1000

    if row['AwayTeam'] not in bigDict:
        bigDict[row['AwayTeam']] = 1000

    expectHomeVal = expected(bigDict[row['AwayTeam']] , bigDict[row['HomeTeam']])
    expectAwayVal = expected(bigDict[row['HomeTeam']] , bigDict[row['AwayTeam']])
    expectedHome.append(expectHomeVal)
    expectedAway.append(expectAwayVal)

    if row['resultForHomeTeam'] == "WIN":
        bigDict[row['HomeTeam']] = max(elo(bigDict[row['HomeTeam']],expectHomeVal, 1, k=32),100)
        outcomeHome.append(bigDict[row['HomeTeam']])
        bigDict[row['AwayTeam']] = max(elo(bigDict[row['AwayTeam']],expectHomeVal, 0, k=32),100)
        outcomeAway.append(bigDict[row['AwayTeam']])

    if row['resultForHomeTeam'] == "DEFEAT":
        bigDict[row['HomeTeam']] = max(elo(bigDict[row['HomeTeam']],expectHomeVal, 0, k=32),100)
        outcomeHome.append(bigDict[row['HomeTeam']])
        bigDict[row['AwayTeam']] = max(elo(bigDict[row['AwayTeam']],expectHomeVal, 1, k=32),100)
        outcomeAway.append(bigDict[row['AwayTeam']])
    
    if row['resultForHomeTeam'] == "DRAW":
        bigDict[row['HomeTeam']] = max(elo(bigDict[row['HomeTeam']],expectHomeVal, 0.5, k=32),100)
        outcomeHome.append(bigDict[row['HomeTeam']])
        bigDict[row['AwayTeam']] = max(elo(bigDict[row['AwayTeam']],expectHomeVal, 0.5, k=32),100)
        outcomeAway.append(bigDict[row['AwayTeam']])

df["expectedHome"] = expectedHome
df["expectedAway"] = expectedAway
df["outcomeHome"] = outcomeHome
df["outcomeAway"] = outcomeAway
#print(df)
#print(bigDict)

sorted_x = sorted(bigDict.items(), key=operator.itemgetter(1))
print(sorted_x)