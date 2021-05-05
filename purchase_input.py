import os
import sys
import fileinput
import csv
from unique_id import unique_id
from print_tabel import print_tabel


full_path = os.path.realpath(__file__)
file_directory = os.path.dirname(full_path)
directory_path = os.path.join(file_directory, "initial_files")
inventory_file = os.path.join(directory_path, "inventory.csv")
expire_file = os.path.join(directory_path, "expires_dates.csv")
purchase_file = os.path.join(directory_path, "purchase.csv")

def purchase_input():
    flag = "n"
    while flag != "y":
        product_name = input("Product_name: (text) ")
        flag = input(f"Is the product_name '{product_name}' correct (y/n/q):")
        if flag == "q":
            return
    print (f"The product_name is now accepted as {product_name}.\n--------")

    flag = "n"
    while flag != "y":
        purchase_date = str(input("Purchase_date: (yyyy-mm-dd) "))
        flag = input(f"Is the purchase_date '{purchase_date}' correct (y/n/q):")
        if flag == "q":
            return
    print (f"The purchase_date is now accepted as {purchase_date}.\n--------")

    flag = "n"
    while flag != "y":
        purchase_amount = str(input("Product_amount: (number) "))
        flag = input(f"Is the product_amount '{purchase_amount}' correct (y/n/q):")
        if flag == "q":
            return
    print (f"The product_name is now accepted as {purchase_amount}.\n--------")

    flag = "n"
    while flag != "y":
        purchase_price = str(input("Total Purchase_price: (number) "))
        flag = input(f"Is the purchase_price '{purchase_price}' correct (y/n/q):")
        if flag == "q":
            return
    print (f"The purchase_price is now accepted as {purchase_price}.\n--------")

    flag = "n"
    while flag != "y":
        expiration_date = input("Expiration_date: (yyyy-mm-dd) ")
        flag = input(f"Is the expiration_date '{expiration_date}' correct (y/n/q):")
        if flag == "q":
            return
    print (f"The expiration_date is now accepted as {expiration_date}.\n--------")

    flag = "n"
    while flag != "y":
        cool_storage = input("Cool_storage: (y/n) ")
        flag = input(f"Is the cool_storage '{cool_storage}' correct (y/n/q):")
        if flag == "q":
            return
    print (f"The cool_storage is now accepted as {cool_storage}.\n--------")
    id = str(unique_id(purchase_amount, expiration_date, purchase_date))
    sold_date = "0"
    sold_price = "0.0"
    exit_status = "n"
    full_input_purchase = (id, product_name,purchase_date,purchase_amount,
                           purchase_price,expiration_date,cool_storage,
                           sold_date,sold_price,exit_status)
    return full_input_purchase

print("The purchase of a product includes many information fields. Your input per field is required.\n")
routine = input("Would you like the full input routine (if not a standard line is added) (y/n): ")
if routine == "y":
    purchase = purchase_input()
else:
    purchase = ("246810", 'schaap', '2021-04-15', '12.0', '150.0', '2021-07-25', 'n', '0', '0.0', 'n')            # default input line

headers = ("id","product_name","purchase_date","purchase_amount","purchase_price",
           "expiration_date","cool_storage","sold_date","sold_price","exit_status")
""""
Afer the required input of the puchase, three files need to be updated:
    the inventory_file with all the headers
    the puchase_file with all the headers
    the expires_dates_file with only a subset of headers.
"""
with fileinput.input(files=purchase_file, inplace=True, mode='r') as file:
    reader= csv.DictReader(file)
    print(",".join(reader.fieldnames))  # print back the headers
    print(",".join(purchase))
    for row in reader:
        print(",".join([row["id"], row["product_name"],row["purchase_date"], row["purchase_amount"],
                    row["purchase_price"], row["expiration_date"], row["cool_storage"],
                    row["sold_date"],row["sold_price"],row["exit_status"]]))

with fileinput.input(files=inventory_file, inplace=True, mode='r') as file:
    reader= csv.DictReader(file)
    print(",".join(reader.fieldnames))  # print back the headers
    print(",".join(purchase))
    for row in reader:
        print(",".join([row["id"], row["product_name"],row["purchase_date"], row["purchase_amount"],
                    row["purchase_price"], row["expiration_date"], row["cool_storage"],
                    row["sold_date"],row["sold_price"],row["exit_status"]]))

# substraction of purchase data, required for expires_dates.csv
purchase_expire_data = list(purchase)
purchase_expire_data.remove(purchase_expire_data[8])    # remove sold_price
purchase_expire_data.remove(purchase_expire_data[7])    # remove sold_date
purchase_expire_data.remove(purchase_expire_data[6])    # remove cool_storage
purchase_expire_data.remove(purchase_expire_data[4])    # remove purchase_amount
purchase_expire_data = tuple(purchase_expire_data)

with fileinput.input(files=expire_file, inplace=True, mode='r') as file:
    reader= csv.DictReader(file)
    print(",".join(reader.fieldnames))  # print back the headers
    print(",".join(purchase_expire_data))
    for row in reader:
        print(",".join([row["id"], row["product_name"],row["purchase_amount"],row["expiration_date"],row["exit_status"]]))

print(f"the following files have been updated with the purchase information:\n\n"
      f"{purchase_file}\n"
      f"{inventory_file}\n"
      f"{expire_file}\n\n"
      f"Purchase completed")

print_tabel(purchase_file)  # external routine
