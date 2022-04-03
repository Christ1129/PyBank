import os
import csv
#start file
with open('election_data.csv') as csvfile:
    csvreader=csv.reader(csvfile, delimiter=',')
   #set variables
ballotid=[]
counties=[]
candidates=[]
canditatesname=[]
totaleachcan=[]
percentvotes=[]
#read data
for row in csvreader:
    ballotid=row[0]
    county=row[1]
    candidate=row[2]
    ballotid.append(ballotid)
    counties.append(county)
    candidates.append(candidate) 
    




