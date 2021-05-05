import csv
import os
from os import system, name

full_path = os.path.realpath(__file__)
file_directory = os.path.dirname(full_path)
directory_path = os.path.join(file_directory, "initial_files")
inventory_file = os.path.join(directory_path, "inventory.csv")
expire_file = os.path.join(directory_path, "expires_dates.csv")

def pad_col(col, max_width):
    # determine the maximum column width
    return col.ljust(max_width)

def print_tabel(print_file):
    # display the offered print_file in a table format
    print()
    with open(print_file) as csvfile:
        reader = csv.reader(csvfile)
        all_rows = []
        for row in reader:
            all_rows.append(row)

    max_col_width = [0] * len(all_rows[0])
    for row in all_rows:
        for idx, col in enumerate(row):
            max_col_width[idx] = max(len(col), max_col_width[idx])
    row_count=0
    empty_line = 0
    # _ = system('cls')                                       # clear screen
    # print(f"\n{print_file}\n")                               # file-path and file-name
    for row in all_rows:
        if row_count <= 1:                                  # print header in table form
            to_print = " "
            for idx, col in enumerate(row):
                to_print += pad_col(col, max_col_width[idx]) + " | "
            print("-"*(len(to_print)-1))
            print(to_print)
        else:
            if empty_line == 2:
                print()
                empty_line = 0
            else:
                empty_line += 1
            to_print = " "                                  # print data in table form
            for idx, col in enumerate(row):
                to_print += pad_col(col, max_col_width[idx]) + " | "
            # print("-"*(len(to_print)-1))
            print(to_print)
        row_count+= 1
    print("-"*(len(to_print)-1))

