# CTI-110
# P4HW1
# Name: Clint Roberts
# Date: 04/26/2023
#

# Ask user for number of test scores to enter
num_scores = int(input("How many scores do you want to enter? "))
print()

# Create a list to store the scores
scores = []

# Collect scores
for i in range(num_scores):
    score = -1
    while score < 0 or score > 100:
        score = float(input(f"Enter score #{i+1}: "))
        if score < 0 or score > 100:
            print("Invalid score entered!!!!")
            print("Score should be between 0 and 100")
            score = float(input(f"Enter score #{i+1} again: "))

    scores.append(score)


dots = "-" * 12    
print("\n\n" + dots + "Results" + dots)

# Display lowest score
lowest_score = min(scores)
print(f'Lowest score  : {lowest_score:<10}')

# Remove lowest score and display modified score list
modified_scores = scores.copy()
modified_scores.remove(lowest_score)
print(f'Modified List : {modified_scores}')

# Calculate and display average of modified score list
average_score = sum(modified_scores) / len(modified_scores)
print(f'Scores Average: {average_score:<10.2f}')

# Determine letter grade for average score and display it to user
if average_score >= 90:
    letter_grade = "A"
elif average_score >= 80:
    letter_grade = "B"
elif average_score >= 70:
    letter_grade = "C"
elif average_score >= 60:
    letter_grade = "D"
else:
    letter_grade = "F"

print(f'Grade         : {letter_grade:<10}')
print("-" * 33)

