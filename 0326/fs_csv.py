import csv

data = [
    ['apple','banana','mango','peach','pineapple'],
    ['apple2','banana2','mango2','peach2','pineapple2']
]

with open('0326.csv','w',encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerows(data)
    # writer.writerow(data)
    # csv.writer(f).writerow(data)
