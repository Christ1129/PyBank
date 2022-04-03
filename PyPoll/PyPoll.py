import os
import csv
#start file
with open ('election_data.csv') as csvfile:
    csvreader=csv.reader(csvfile, delimiter=',') 
    header=next(csvreader) 
    voterids=[] 
    counties=[] 
    candidates=[] 
    candidatenames=[] 
    totaleachcan=[] 
    resultprintcan=[] 
    totaleachcanperc=[] 
    #Set start conditions
    line_count=0
    winnervotes=0
    loservotes=0
    loop1=0
    loop2=0
    loop3=0
    loop4=0



    