import os
from shutil import copyfile
from os import path, makedirs
from csv import DictWriter
import shutil

""" 
Target of this routine is to create a directory folder 'initial_files'
to facilitate the stock-files in a later process.
"""

def create_directory(directory_name):                   
    # creates a directory with directory_name as input and directory as output
    full_path = os.path.realpath(__file__)
    file_directory = os.path.dirname(full_path)
    directory_path = os.path.join(file_directory, directory_name)

    if not os.path.isdir(directory_path):
        os.makedirs(directory_path)
        print(f"\n Created {directory_name} folder in {file_directory}")

    shutil.copy("stock.csv", directory_path)

    stock_file = os.path.join(directory_path, "stock.csv")

    if not os.path.isfile("inventory.csv"):
        inventory_file = os.path.join(directory_path, "inventory.csv")

    if not os.path.isfile("expires_dates.csv"):
        expire_file = os.path.join(directory_path, "expires_dates.csv")

    if not os.path.isfile("purchase.csv"):
        purchase_file = os.path.join(directory_path, "purchase.csv")

    if not os.path.isfile("sales.csv"):
        sales_file = os.path.join(directory_path, "sales.csv")

    return directory_path


# create_directory("supermarket_files")         # testline for debugging

