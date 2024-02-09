import csv

report = open('employee_data.csv','r')
employee_report = csv.reader(report)

next(employee_report)

print('Highly Effecient Individuals:')

for rec in employee_report:
    efficiency = float(rec[5])/float(rec[4])
    if efficiency > 2:
        print(f'{rec[1]}')

report.close()
report = open('employee_data.csv','r')
employee_report = csv.reader(report)

next(employee_report)


print(f"\nLow Efficiency Individuals:")

for rec in employee_report:
    efficiency1 = float(rec[5])/float(rec[4])
    if efficiency1 < 1:
        print(rec[1])

report.close()
report = open('employee_data.csv','r')
employee_report = csv.reader(report)

next(employee_report)

forty = 0
print(f'\nEmployees in their 40s')
for rec in employee_report:
    age = int(rec[2])
    if age >= 40:
        print(rec[1])
        forty += 1
print('total number of employees in their 40s:',forty)

report.close()
report = open('employee_data.csv','r')
employee_report = csv.reader(report)

next(employee_report)

thirty = 0
print(f'\nEmployees in their 30s')
for rec in employee_report:
    age = int(rec[2])
    if 40 > age >= 30:
        print(rec[1])
        thirty += 1
print('total number of employees in their 30s:',thirty)



report.close()
report = open('employee_data.csv','r')
employee_report = csv.reader(report)

next(employee_report)

twenty = 0
print(f'\nEmployees in their 20s')
for rec in employee_report:
    age = int(rec[2])
    if 30 > age >= 20:
        print(rec[1])
        twenty += 1
    
print('total number of employees in their 20s:',twenty)
