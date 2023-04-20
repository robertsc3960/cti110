# CTI-110
# P3HW2 - Salary
# Clint Roberts
# 4/20/2023
#

# ask the user to enter the name of the employee
name = input("Enter employee's name: ")

# ask the user to enter the number of hours the employee worked this week
hours_worked = float(input("Enter number of hours worked: "))

# ask the user to enter the employee's pay rate
pay_rate = float(input("Enter employee's pay rate: "))

print("-" * 36)

# check if the employee worked overtime (more than 40 hours)
if hours_worked > 40:
    # calculate the amount owed to employee for overtime hours
    overtime_hours = hours_worked - 40
    overtime_pay = overtime_hours * pay_rate * 1.5
    regular_pay = 40 * pay_rate
    gross_pay = regular_pay + overtime_pay
else:
    regular_pay = hours_worked * pay_rate
    overtime_hours = 0
    overtime_pay = 0
    gross_pay = regular_pay

# display the employee's name, pay rate, number of hours worked, overtime hours, overtime pay, pay for regular hours, and gross pay
print (f'{"Employee name:":<18}{name}', "\n")

print(f'{"Hours Worked":<15}{"Pay Rate":<15}{"Overtime":<15}{"Overtime Pay":<15}{"RegHour Pay":<15}{"Gross Pay":<15}')
print("-" * 90)
print(f'{hours_worked:<15.2f}{pay_rate:<15.2f}{overtime_hours:<15.2f}{overtime_pay:<15.2f}{regular_pay:<15.2f}{gross_pay:<15.2f}')
