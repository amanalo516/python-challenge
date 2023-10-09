import os
import csv


with open("Resources/election_data.csv", 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ',')

    #list variables for calculations

    total_votes = 0
    candidate_dict = {}
    current_winner = ''
    winner_percent = 0

    next(csvreader)
    for row in csvreader:
        current_name = row[2]

        total_votes += 1
        # Create dictionary to identify candidates and count votes
        if current_name in candidate_dict:
            candidate_dict[current_name] += 1
        else:
            candidate_dict[current_name] = 1 
 
    #print(candidate_dict) to verify candidates and continue with calculations
 
    f = open('results.txt',"w")
    
    #Use output to put calculations together for text file

    output="Election Results\n" 
    output+= "------------------------------\n"
    
    output+= "Total Votes: " + str(total_votes) 
    output += '\n'
    output+= "------------------------------\n"

  
    for name in candidate_dict:
        name_votes = candidate_dict[name]
        name_percent = round(100 * (name_votes/total_votes), 3) 

    #use if to pull winner of election
        if name_percent > winner_percent:
            current_winner = name
            winner_percent = name_percent
   
        output += str(name + ': ')
        output += str(name_percent) 
        output += str("% ")
        output += str("(")
        output += str(name_votes)
        output += str(")")
        output += '\n'
    

    output+= "------------------------------\n"
    output += str('Winner: '+ current_winner)
    output+= "\n------------------------------\n"   
           
  
print(output)
f.write(output)
f.close()