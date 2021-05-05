""""
This is the very first routine to be executed for importing the inventory data from
stock.csv. This is our starting point.
"""
from os import system, name
import os
from stockstart import StockStart
from expire import get_expiry_report_today
from datetime import date, datetime


_ = system('cls')                                           # clear screen
stock_start = StockStart()
running_date = date.today()
todays_expire = get_expiry_report_today(running_date, 0)    # external routine
full_path = os.path.realpath(__file__)
file_directory = os.path.dirname(full_path)
directory_path = os.path.join(file_directory, "initial_files")
inventory_file = os.path.join(directory_path, "inventory.csv")
expire_file = os.path.join(directory_path, "expires_dates.csv")
import report_inventory
