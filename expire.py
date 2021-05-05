import os
import sys
import fileinput
import csv
import math
from datetime import date, timedelta, datetime



full_path = os.path.realpath(__file__)
file_directory = os.path.dirname(full_path)
directory_path = os.path.join(file_directory, "initial_files")
inventory_file = os.path.join(directory_path, "inventory.csv")
expire_file = os.path.join(directory_path, "expires_dates.csv")


def get_expiry_report_today(running_date, num_of_days):             # check current expire dates of inventory
    report = []
    number_of_days = num_of_days                                    # for today=0
    headers = ["id", "product_name", "purchase_amount", "expiration_date", "exit_status"]
    report.append(headers)
    os.remove(os.path.join(os.path.join(os.path.dirname(os.path.realpath(__file__)), "initial_files"), "expires_dates.csv"))

    with fileinput.input(files=inventory_file, inplace=True, mode='r') as file:     # update inventory.cvs
        reader = csv.DictReader(file)
        print(",".join(reader.fieldnames))  # print back the headers
        for row in reader:
            expire_date = row["expiration_date"]
            product_expire_date = date.fromisoformat(expire_date)
            exit_status = row["exit_status"]
            if exit_status != "expired" and exit_status != "sold":
                if running_date > product_expire_date:
                    row["exit_status"] = "expired"
                    print(",".join([row["id"], row["product_name"], row["purchase_date"], row["purchase_amount"],row["purchase_price"], row["expiration_date"],row["cool_storage"], row["sold_date"], row["sold_price"], row["exit_status"]]))
                    report.append([row["id"], row["product_name"], row["purchase_amount"], row["expiration_date"],"expired"])
                else:
                    print(",".join([row["id"], row["product_name"], row["purchase_date"], row["purchase_amount"],row["purchase_price"], row["expiration_date"],row["cool_storage"], row["sold_date"], row["sold_price"], row["exit_status"]]))
            else:
                print(",".join([row["id"], row["product_name"], row["purchase_date"], row["purchase_amount"],row["purchase_price"], row["expiration_date"],row["cool_storage"], row["sold_date"], row["sold_price"], row["exit_status"]]))

    file = open(expire_file, 'w+', newline="")     # update expires_dates.cvs
    with file:
        write = csv.writer(file)
        write.writerows(report)

    return report

# report = get_expiry_report_today("2021-04-11", 2)       # testline module

def get_expiry_report_simulated(sim_date, num_of_days):             # check expire dates of inventory
    if sim_date == "None":
        sim_date = str(date.today())
    report = []
    purchase_lost = 0.0
    os.remove(os.path.join(os.path.join(os.path.dirname(os.path.realpath(__file__)), "initial_files"), "expires_dates.csv"))
    sim_date = date.fromisoformat(str(sim_date))
    max_date = sim_date + timedelta(days=num_of_days)
    headers = ["id", "product_name", "purchase_amount", "purchase_price", "expiration_date", "exit_status"]
    report.append(headers)
    print(f"\n The simulated date for this run is {max_date}\n")
    with fileinput.input(files=inventory_file, inplace=False, mode='r') as file:     # read inventory.cvs
        reader = csv.DictReader(file)

        for row in reader:
            expire_date = row["expiration_date"]
            sold_date = row["sold_date"]
            exit_status = row["exit_status"]
            purchase_date = row["purchase_date"]
            product_purchase_date = date.fromisoformat(purchase_date)
            product_expire_date = date.fromisoformat(expire_date)
            if sold_date == "0":
                product_sold_date = date.fromisoformat("2999-01-01")
            else:
                product_sold_date = date.fromisoformat(sold_date)
            if product_sold_date <= max_date:
                print (f" product {row['id']} / {row['product_name']} has been \tsold \t\tbefore the simulation date")
            else:
                if product_purchase_date >= max_date:
                    print (f" product {row['id']} / {row['product_name']} has been purchased later than or on the simulation date")
                else:
                    if max_date > product_expire_date:
                        row["exit_status"] = "expired (simulated)"
                        report.append([row["id"], row["product_name"], row["purchase_amount"], row["purchase_price"], row["expiration_date"],row["exit_status"]])
                        expiration_date = row["expiration_date"]
                        purchase_lost += float(row["purchase_price"])
                        print(f" product {row['id']} / {row['product_name']} has been \texpired, \tgiven the simulation date")
                    else:
                        print(f" product {row['id']} / {row['product_name']} is still \t'fresh' \tgiven the "
                              f"simulation date \t(Exp_Date: {product_expire_date})")
    file = open(expire_file, 'w+', newline="")     # update expires_dates.cvs
    with file:
        write = csv.writer(file)
        write.writerows(report)
    from print_tabel import print_tabel
    print_tabel(expire_file)            # external routine
    print(f"\n Total value loss due to expiration for this simulation: {purchase_lost}")
    return report



