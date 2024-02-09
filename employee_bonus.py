import csv

employee = open('employee_data.csv','r')
employee_file = csv.reader(employee)
next(employee_file)

for rec in employee_file:
    bonus = float(rec[3])*float(rec[7])
    pay = float(rec[3])+bonus
    print(f'Name: {rec[1]}')
    print(f'Salary: $ {float(rec[3]):10,.2f}')
    print(f'Bonus:  $ {bonus:10,.2f}')
    print(f'Pay:    $ {pay:10,.2f}')
    input()