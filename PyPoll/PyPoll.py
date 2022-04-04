import os
import csv
#start csv file

with open ('election_data.csv') as csvfile:
    csvreader=csv.reader(csvfile, delimiter=',') 
    header=next(csvreader) 

        #Variables
    ballotids=[] 
    counties=[] 
    candidates=[] 
    candidatenames=[] 
    totalvote=[] 
    resultprintcan=[] 
    totalpercent=[] 

    #Conditions
    line_count=0
    winnervotes=0
    loservotes=0
    
    #Read in each row of data 
    for row in csvreader:
        ballotid=row[0] 
        county=row[1] 
        candidate=row[2] 
        ballotids.append(ballotid) 
        counties.append(county) 
        candidates.append(candidate) 
    
    line_count= len(ballotids) 
    
#Analyse data and loop through the list of candidate
candidatenames.append(candidates[0]) 

for loop1 in range (line_count-1):
    if candidates[loop1+1] != candidates[loop1] and candidates[loop1+1] not in candidatenames:
        candidatenames.append(candidates[loop1+1])

n=len(candidatenames)
for loop2 in range (n): 
    totalvote.append(candidates.count(candidatenames[loop2])) 

loservotes=line_count 

for loop3 in range(n): 
    totalpercent.append(f'{round((totalvote[loop3]/line_count*100), 4)}%') 
    if totalvote[loop3]>winnervotes: 
        winner=candidatenames[loop3]
        winnervotes=totalvote[loop3]
    if totalvote[loop3]<loservotes: 
        loser=candidatenames[loop3]
        loservotes=totalvote[loop3]

for loop4 in range(n):
    resultprintcan.append(f'{candidatenames[loop4]}: {totalpercent[loop4]} {totalvote[loop4]}') 

resultlines='\n'.join(resultprintcan) 

#Displaying analysis
analysis=f'\
Election Results\n\
----------------------------\n\
Total Votes: {line_count}\n\
----------------------------\n\
{resultlines}\n\
----------------------------\n\
Winner: {winner} :)\n\
Last: {loser} :(\n\
----------------------------\n'

print(analysis)

#Result text file name
file1=open("pypoll.txt","w") 
file1.writelines(analysis) 
file1.close() 
    



