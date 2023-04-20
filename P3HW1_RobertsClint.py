# P3HW1 
# RobertsClint

# This program takes a number grade, determines the average, and displays the letter grade for the average.

# User enters grades for six modules
mod_1 = float(input('Enter grade for Module 1: '))
mod_2 = float(input('Enter grade for Module 2: '))
mod_3 = float(input('Enter grade for Module 3: '))
mod_4 = float(input('Enter grade for Module 4: '))
mod_5 = float(input('Enter grade for Module 5: '))
mod_6 = float(input('Enter grade for Module 6: '))

# Lists inputed module grades
grades = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]

# Determines lowest, highest, sum, and average for grades
dots = '-' * 12
print ('\n'+ dots+ "Results" +dots)
#Display the lowest grade
score_min = min (grades)
print (f'{"Lowest Grade:":<20}{score_min}')

#Display the highest grade
score_max = max (grades)
print (f'{"Highest Grade:":<20}{score_max}')

#Display sum of grades
score_sum = sum (grades)
print (f'{"Sum of Grades:":<20}{score_sum}')

#Display grade average
score_ave = sum (grades) / 6
print (f'{"Average:":<20}{score_ave:.2f}')

dots = '-' * 31
print (dots)

# Determines letter grade for average
if score_ave >= 90:
    print('Your grade is: A')
elif score_ave >= 80:
    print('Your grade is: B')
elif score_ave >= 70:
    print('Your grade is: C')
elif score_ave >= 60:
    print('Your grade is: D')
else:
    print('Your grade is: F') 
