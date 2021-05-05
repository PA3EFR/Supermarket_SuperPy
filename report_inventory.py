import os
import sys
import fileinput
import csv
import math
from os import system, name
from print_tabel import print_tabel

count = 0
sales_price = 0.0
purchase_price = 0.0
sold_counter = 0
expire_counter = 0
value_loss = 0.0
full_path = os.path.realpath(__file__)
file_directory = os.path.dirname(full_path)
directory_path = os.path.join(file_directory, "initial_files")
inventory_file = os.path.join(directory_path, "inventory.csv")
expire_file = os.path.join(directory_path, "expires_dates.csv")
purchase_file = os.path.join(directory_path, "purchase.csv")
sales_file = os.path.join(directory_path, "sales.csv")

with fileinput.input(files=inventory_file, inplace=False, mode='r') as file:
    reader =csv.DictReader(file)
    # print("\t,".join(reader.fieldnames))                # print back the headers
    for row in reader:
        purchase_price = purchase_price + float(row["purchase_price"])
        count+= 1                                      # row counter
        if row["sold_price"] != "0.0":
            if row["exit_status"] == "sold":
                sales_price = sales_price + float(row["sold_price"])
                sold_counter += 1
        if row["exit_status"] == "expired":
                expire_counter += 1
                value_loss += float(row["purchase_price"])

print_tabel(inventory_file)  # external routine
print("\n\n\tnumber of inventory items:",count)
print("\n\ttotal purchase costs:\t\t", round((purchase_price),2))
print(f"\ttotal of {sold_counter} sales:\t\t", round((sales_price), 2))
print("\tnumber of expired items today:\t", expire_counter)
print("\tvalueloss due to expired items:\t", value_loss)
print("\ttoday's profit on total stock:\t", (round((sales_price-purchase_price-value_loss),2)), "\n\n\n")
