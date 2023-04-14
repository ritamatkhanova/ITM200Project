import csv
import pandas as pd
import matplotlib.pyplot as plt
years=[]
yearlysales=[]
half2021=[]
half2022=[]
with open('Data.csv') as sd:
    read = csv.reader(sd)
    next(read)

    total_sales = {}
    for i in read:
        year = int(i[0])
        if year < 2012 or year > 2021:
            continue
        years.append(year)
        sales_data = []
        for x in i[1:]:
            if x != '':
                sales_data.append(int(x))
        total_sales[year] = sum(sales_data)
        yearlysales.append(sum(sales_data))


with open('stats.txt', mode='w') as file:
    file.write('Total Sales from 2012-2021:\n')
    for year, sales in total_sales.items():
        file.write(str(year) + ': ' + str(sales) + '\n')
# bar plot 2012-2021

plt.figure(1)

plt.bar(years, yearlysales)

plt.title('Total Sales Per Year')
plt.xlabel('Year')
plt.ylabel('Total Sales')

plt.show()

# sales estimation
'''
with open('Data.csv') as excel:
    read = csv.reader(excel)
    next(read)
    for row in read:
        year = int(row[0])
        if year == 2021:
            half2021.append([int(x) for x in row[1:7]])
        elif year == 2022:
            half2022.append([int(x) for x in row[1:7]])
'''
half2021= [110903, 114510, 153722, 154105, 152141, 162549]
half2022 = [36922, 39082, 55611, 57110, 56991, 66514]
total_sales_2021 = sum(half2021)
total_sales_2022 = sum(half2022)

sgr = (total_sales_2022 - total_sales_2021) / total_sales_2022

with open('stats.txt', mode='a') as file:
    file.write('The Sales Growth Rate is: ' + str(round(sgr, 2)))

num_sales2022 = []

for month in range(7, 13):
    month_year_21 = half2021[month - 7]
    num_sale = month_year_21 * (1 + sgr)
    num_sales2022.append(num_sale)

with open('stats.txt', 'a') as file:
    file.write('\nThe Estimated Sales For The Last Six Months of 2022:\n')
    file.write('July 2022: ' + str(round(-num_sales2022[0])) + '\n')
    file.write('Aug 2022: ' + str(round(-num_sales2022[1])) + '\n')
    file.write('Sept 2022: ' + str(round(-num_sales2022[2])) + '\n')
    file.write('Oct 2022: ' + str(round(-num_sales2022[3])) + '\n')
    file.write('Nov 2022: ' + str(round(-num_sales2022[4])) + '\n')
    file.write('Dec 2022: ' + str(round(-num_sales2022[5])) + '\n')

# horizontal bar plot
sales_months = ['July', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec']
num_sales2022 = [-num_sales2022[0], -num_sales2022[1], -num_sales2022[2], -num_sales2022[3], -num_sales2022[4],
                 -num_sales2022[5]]

plt.figure(2)
plt.barh(sales_months, num_sales2022)

plt.title('The Estimated Sales For The Last Six Months of 2022')
plt.ylabel('Sales')
plt.xlabel('Months')

plt.show()
