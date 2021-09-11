#-------------------------------------------------------------------------
# AUTHOR: Nathaniel McDorman
# FILENAME: find_s.py
# SPECIFICATION: This program reads in 'contact_lens.csv' file and determines the max hypothesis from it
# FOR: CS 4200- Assignment #1
# TIME SPENT: About 30 minutes
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard vectors and arrays

#importing some Python libraries
import csv

num_attributes = 4
db = []
print("\n The Given Training Data Set \n")

#reading the data in a csv file
with open('contact_lens.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  for i, row in enumerate(reader):
      if i > 0: #skipping the header
         db.append (row)
         print(row)

print("\n The initial value of hypothesis: ")
hypothesis = ['0'] * num_attributes #representing the most specific possible hypothesis
print(hypothesis)

#find the first positive training data in db and assign it to the vector hypothesis
for row in range(len(db)):
    if db[row][4] == 'Yes':
        hypothesis = db[row]
        break

#find the maximally specific hypothesis according to your training data in db and assign it to the vector hypothesis (special characters allowed: "0" and "?")
for row in range(len(db)):
    if db[row][4] == 'Yes':
        for feature in range(0, num_attributes):
            if db[row][feature] != hypothesis[feature]:
                hypothesis[feature] = "?"

print("\n The Maximally Specific Hypothesis for the given training examples found by Find-S algorithm:\n")
print(hypothesis)