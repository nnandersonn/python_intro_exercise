# from functools import total_ordering
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

invoices = open("Cupcakeinvoices.csv")
running_total = 0
chocolate_count = 0
vanilla_count = 0
strawberry_count = 0
categories = ['Chocolate', 'Vanilla', 'Strawberry']


for row in invoices:
    # print(row)
    x = row.split(',')
    print(x[2])
    if x[2] == 'Chocolate':
        chocolate_count += 1
    elif x[2] == 'Vanilla':
        vanilla_count += 1
    elif x[2] == 'Strawberry':
        strawberry_count += 1
    quantity = x[3]
    price = x[4]
    total_price = quantity + price
    print(format(float(total_price), '.2f'))
    running_total += float(total_price)

counts = [chocolate_count, vanilla_count, strawberry_count]
print('total is', running_total)
print(strawberry_count, chocolate_count, vanilla_count)
plt.bar(categories, counts, width=0.3, color = 'green')
plt.xlabel("Cupcake Types")
plt.ylabel("Cupcakes Sold")
plt.title("Cupcake Sales")
plt.show()