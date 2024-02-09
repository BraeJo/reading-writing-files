import csv

customers = open('customers.csv','r')

customer_country = open('customer_country.csv','w')

csv_file = csv.reader(customers)

#this will skip the first record which is the header
next(csv_file)
customer_country.write(f'Full Name, Country\n')

for rec in csv_file:
    #print(rec)
    print(f'Full Name: {rec[1]} {rec[2]}, Country: {rec[4]}')
    customer_country.write(f'{rec[1]} {rec[2]}, {rec[4]}\n')

customer_country.close()
