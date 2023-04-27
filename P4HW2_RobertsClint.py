# CTI-110
# P4HW2 - Salary Calculator
# Clint Roberts
# 4/26/2023

# initialize variables
overtime_total = 0
regular_pay_total = 0
gross_pay_total = 0
num_employees = 0

# loop until the user enters "Done" for the employee name
while True:
    # ask the user for the employee name
    name = input("Enter employee's name or \"Done\" to terminate: ")
    
    # if the user enters "Done", break out of the loop
    if name.lower() == 'done':
        break

    
    # ask the user for the pay rate and hours worked
    hours_worked = float(input(f"How many hours did {name} work? "))
    pay_rate = float(input(f"What is {name}'s pay rate? "))
    print()

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
    print()

    # calculate the gross pay and add to the totals
    gross_pay = regular_pay + overtime_pay
    overtime_total += overtime_pay
    regular_pay_total += regular_pay
    gross_pay_total += gross_pay
    num_employees += 1     

# display the totals
print()
print(f"Total number of employees entered: {num_employees}")
print(f"Total amount paid for overtime: ${overtime_total:.2f}")
print(f"Total amount paid for regular hours: ${regular_pay_total:.2f}")
print(f"Total amount paid in gross: ${gross_pay_total:.2f}")
