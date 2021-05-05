"""
This file takes in a stock.csv (pre-produced) stock-file and derives from this stockfile
four new files for our supermarket.

In the folder INITIAL_FILES the following CSV files are filled with STOCK.CSV information:
INVENTORY.CSV, PURCHASE.CSV, EXPIRES_DATES.CSV and SALES.CSV.

Every item in these new files have unique ID's. The files will be used to alter fields if
required and will be used for reporting.
"""
import os
import csv
from create_directory import create_directory
from decimal import Decimal
import math
from unique_id import unique_id

class StockStart():
    def __init__(self):
        dir_path = create_directory("initial_files")                                   # external routine
        id = 0
        self.dir_path = dir_path
        stock_file = os.path.join(dir_path, "stock.csv")                               # external information file
        inventory_file = os.path.join(dir_path, "inventory.csv")
        expire_file = os.path.join(dir_path, "expires_dates.csv")
        purchase_file = os.path.join(dir_path, "purchase.csv")
        sales_file = os.path.join(dir_path, "sales.csv")
# Stock building
        if os.path.isfile(stock_file):
            with open(stock_file, newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    id = row['id']
                    product_name = row['product_name']
                    purchase_date = row["purchase_date"]
                    amount = float(row['purchase_amount'])
                    amount_round = round(amount,0)
                    amount_round = math.ceil(amount_round)
                    purchase_price = float(row["purchase_price"])
                    expiration_date = row["expiration_date"]
                    cool_storage = row["cool_storage"]
                    sold_date = row["sold_date"]
                    sold_price = float(row["sold_price"])
                    exit_satus = row["exit_status"]
                    id = unique_id(amount_round, expiration_date, purchase_date)        # external rountine

# subfile inventory building
                    if os.path.isfile(inventory_file):
                        with open(inventory_file, 'a', newline='') as csvfile:
                            headers = ("id", "product_name", "purchase_date", "purchase_amount", "purchase_price", "expiration_date",
                                       "cool_storage", "sold_date", "sold_price", "exit_status")
                            writer = csv.DictWriter(csvfile, fieldnames=headers)
                            writer.writerow({"id": id, "product_name": product_name, "purchase_date": purchase_date,
                                             "purchase_amount":amount, "purchase_price": purchase_price,
                                             "expiration_date":expiration_date, "cool_storage":cool_storage, "sold_date": sold_date,
                                             "sold_price": sold_price, "exit_status": exit_satus})
                    else:
                        with open(inventory_file, 'w', newline='') as csvfile:
                            headers = ("id", "product_name", "purchase_date", "purchase_amount", "purchase_price", "expiration_date",
                                       "cool_storage", "sold_date", "sold_price", "exit_status")
                            writer = csv.DictWriter(csvfile, fieldnames=headers)
                            writer.writeheader()
                            writer.writerow({"id": id, "product_name": product_name, "purchase_date": purchase_date,
                                             "purchase_amount":amount, "purchase_price": purchase_price,
                                             "expiration_date":expiration_date, "cool_storage":cool_storage, "sold_date": sold_date,
                                             "sold_price": sold_price, "exit_status": exit_satus})
# subfile sales building
                    if os.path.isfile(sales_file):      # write rows
                        with open(sales_file, 'a', newline='') as csvfile:
                            headers = ["id","product_name", "purchase_date", "purchase_amount",
                                       "purchase_price", "sold_date", "sold_price", "exit_status"]
                            writer = csv.DictWriter(csvfile, fieldnames=headers)
                            if row["exit_status"] == "sold":        # only add a row to sales.csv if ID is sold
                                writer.writerow({"id": id, "product_name": product_name, "purchase_date": purchase_date, "purchase_amount": amount,
                                                 "purchase_price": purchase_price, "sold_date": sold_date,
                                                 "sold_price": sold_price, "exit_status": exit_satus})
                    else :                              # write headers
                        with open(sales_file, 'w', newline='') as csvfile:
                            headers = ["id","product_name", "purchase_date", "purchase_amount",
                                       "purchase_price", "sold_date", "sold_price", "exit_status"]
                            writer = csv.DictWriter(csvfile, fieldnames=headers)
                            writer.writeheader()
                            if row["exit_status"] == "sold":        # only add a row to sales.csv if ID is sold
                                writer.writerow({"id": id, "product_name": product_name, "purchase_date": purchase_date,"purchase_amount": amount,
                                             "purchase_price": purchase_price, "sold_date": sold_date,
                                             "sold_price": sold_price, "exit_status": exit_satus})
# subfile purchase building
                    if os.path.isfile(purchase_file):
                        with open(purchase_file, 'a', newline='') as csvfile:
                            headers = ("id", "product_name", "purchase_date", "purchase_amount", "purchase_price", "expiration_date",
                                       "cool_storage", "sold_date", "sold_price", "exit_status")
                            writer = csv.DictWriter(csvfile, fieldnames=headers)
                            writer.writerow({"id": id, "product_name": product_name, "purchase_date": purchase_date,
                                             "purchase_amount":amount, "purchase_price": purchase_price,
                                             "expiration_date":expiration_date, "cool_storage":cool_storage, "sold_date": sold_date,
                                             "sold_price": sold_price, "exit_status": exit_satus})
                    else:
                        with open(purchase_file, 'w', newline='') as csvfile:
                            headers = ("id", "product_name", "purchase_date", "purchase_amount", "purchase_price", "expiration_date",
                                       "cool_storage", "sold_date", "sold_price", "exit_status")
                            writer = csv.DictWriter(csvfile, fieldnames=headers)
                            writer.writeheader()
                            writer.writerow({"id": id, "product_name": product_name, "purchase_date": purchase_date,
                                             "purchase_amount":amount, "purchase_price": purchase_price,
                                             "expiration_date":expiration_date, "cool_storage":cool_storage,"sold_date": sold_date,
                                             "sold_price": sold_price, "exit_status": exit_satus})

# subfile expire building
                    if os.path.isfile(expire_file):
                        pass
                    else:
                        with open(expire_file, 'w', newline='') as csvfile:
                            headers = ("id", "product_name", "purchase_date", "purchase_price", "expiration_date", "exit_status")
                            writer = csv.DictWriter(csvfile, fieldnames=headers)
                            writer.writeheader()

# stock_start = StockStart()        # test line for module testing