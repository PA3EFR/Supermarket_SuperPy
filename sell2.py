import os
from os import system
import sys
import fileinput
import csv
import argparse
from datetime import date
from print_tabel import print_tabel

full_path = os.path.realpath(__file__)
file_directory = os.path.dirname(full_path)
directory_path = os.path.join(file_directory, "initial_files")
# print(directory_path)
inventory_file = os.path.join(directory_path, "inventory.csv")
# print(inventory_file)
expire_file = os.path.join(directory_path, "expires_dates.csv")
purchase_file = os.path.join(directory_path, "purchase.csv")
sales_file = os.path.join(directory_path, "sales.csv")

ap = argparse.ArgumentParser()
# id = "246810"                                      # testline
# sold_date = "2021-04-03"                                          # testline
# sold_price = str(23.23)                                           # testline

def sell2(id, sold_date, sold_price):
    # process to embed sold item information into the inventory and associated files
    if sold_date == "None":
        sold_date = str(date.today())
    print("\n Action: sell item\n")
    print(f" The indicated item-ID: \t{id}")
    print(f" The indicated sold date: \t{sold_date}")
    print(f" The total selling price: \t{sold_price}")
    sold_flag = ""
    total_sales = 0.0

    with fileinput.input(files=inventory_file, inplace=True, mode='r') as file:
        reader =csv.DictReader(file)
        print(",".join(reader.fieldnames))  # print back the headers
        for row in reader:
            if row["id"] == id and row["exit_status"] == "n":
                row["sold_date"] = sold_date
                row["sold_price"]= sold_price
                row["exit_status"] = "sold"
                sold_flag = "and sold action completed"
                product_name = row["product_name"]
                purchase_date = row["purchase_date"]
                purchase_amount = row["purchase_amount"]
                purchase_price = row["purchase_price"]
                # for the sales.csv additional row
                id2 = id
                sold_date2 = sold_date
                sold_price2 = sold_price
                exit_status2 = "sold"
                product_name2 = product_name
                purchase_date2 = purchase_date
                purchase_amount2 = purchase_amount
                purchase_price2 = purchase_price
                exit_status = "sold"
            else:
                pass
            print(",".join([row["id"], row["product_name"],row["purchase_date"], row["purchase_amount"],
                                row["purchase_price"],row["expiration_date"],row["cool_storage"],
                                row["sold_date"],row["sold_price"],row["exit_status"]]))

    if sold_flag == "and sold action completed":
        with fileinput.input(files=sales_file, inplace=True, mode='r') as file:
            reader = csv.DictReader(file)
            print(",".join(reader.fieldnames))  # print back the headers
            print(",".join([id2, product_name2, purchase_date2, purchase_amount2, purchase_price2, sold_date2, sold_price2,
                            exit_status2]))  # Add sold item to overview BEFORE the rest is shown
            total_sales += float(sold_price2)
            for row in reader:
                print(",".join([row["id"], row["product_name"], row["purchase_date"], row["purchase_amount"],
                                row["purchase_price"],
                                row["sold_date"], row["sold_price"], row["exit_status"]]))
                total_sales += float(row["sold_price"])
    else:
        pass

    if sold_flag == "and sold action completed":
        print(f"\nTransaction completed; item {id} {sold_flag}", file=sys.stdout)
        total_sales = round(total_sales, 2)
        print(f"\nTotal sales: \t\t\t{total_sales}", file=sys.stdout)
        print("\n Sales overview:")
        print_tabel(sales_file)
    else:
        print(f"\nTransaction aborted, because item-ID {id} was already sold/expired/non-existing (see inventory report).", file=sys.stdout)
    return

