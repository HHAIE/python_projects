import glob
import csv
import gspread
import time

gc = gspread.service_account()

sh = gc.open("Finances")

# print(sh.sheet1.get('A1'))

bank_files = glob.glob('OversiktKonti-*.csv')


with open(bank_files[0], mode='r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    next(csv_reader, None)
    for row in csv_reader:
        date = row[0]
        name = row[1]
        expense = float(row[4].replace(',','.')) if row[4] != '' else 0
        transaction = (date, name, expense)
        sh.sheet1.insert_row(transaction)
        time.sleep(2)