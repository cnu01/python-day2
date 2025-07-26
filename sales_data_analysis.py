sales_data = [
    ('Q1',[('Jan',1000),('Feb',1200),('Mar',1100)]),
    ('Q2',[('Apr',1000),('May',1200),('Jun',1100)]),
    ('Q3',[('Jul',1000),('Aug',1200),('Sep',1100)])
]


for quarter,month in sales_data:
    print(f"{quarter}")
    for month,sales in month :
        print(f"{month} - {sales}")


max_month = None
max_sales = float('-inf') 

for _, months in sales_data:
    for month, amount in months:
        if amount > max_sales:
            max_sales = amount
            max_month = month

print(f"{max_month} ({max_sales})")

newlist = []

for _, months in sales_data:
    for month, amount in months:
        newlist.append((month,amount))

print(newlist)


for quarter,months in sales_data:
    for month,amount in months:
        print(f'Sales : {quarter} - {month} - {amount}')