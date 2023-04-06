#miles per gallon
mpg = float(input())
#cost of gas per gallon
gas_cost = float(input())

#fuel cost for 20 miles
x = 20 / mpg * gas_cost
#fuel cost for 75 miles
y = 75 / mpg * gas_cost
#fuel cost for 500 miles
z = 500 / mpg * gas_cost

#output of fuel costs per mile range
print(f'{x:.2f} {y:.2f} {z:.2f}')
