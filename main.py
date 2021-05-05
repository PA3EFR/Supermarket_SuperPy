# Do not change these lines.
__winc_id__ = 'a2bc36ea784242e4989deb157d527ba0'
__human_name__ = 'superpy'
"""
See the user guide for the set-up of the main.py functionalities
"""
from os import system, name
import os.path
from os import path

directory_exists = path.exists('initial_files')  # check if this is first time run by dir_existance checking
if directory_exists:
    print(" The initial start-up of the Super Market Py has been executed.")
else:
    import init
""""
Action requests through argparse. 
"""
import argparse
from sell2 import sell2
from datetime import date
from expire import get_expiry_report_simulated

def main(command_line=None):
    # function to obtain the users command for further execution
    parser = argparse.ArgumentParser('Supermarket SuperPy')
    subparsers = parser.add_subparsers(dest='command')

    report = subparsers.add_parser('report', help='report stock inventory')

    purchase = subparsers.add_parser('purchase', help='start process of purchasing item')

    sell = subparsers.add_parser('sell', help='information on sold items')
    sell.add_argument('-id', '--id', help='identification number of sold item', required=True)
    sell.add_argument('-soldprice', '--soldprice', help='price for sold item', required=True)
    sell.add_argument('-solddate', '--solddate', help='date of sold item. Default = today', required=False)

    expire = subparsers.add_parser('expire', help='simulate expire dates and periods')
    expire.add_argument('-simdate', '--simdate', help='start date of simulation. Default = today', required=False)
    expire.add_argument('-numdays', '--numdays', help='number of simulated days', required=True)

    args = parser.parse_args(command_line)

    if args.command == "report":
        import report_inventory

    elif args.command == "purchase":
        import purchase_input

    elif args.command == "sell":
        id = str(args.id)
        sold_price = str(args.soldprice)
        sold_date = str(args.solddate)
        sell2(id, sold_date, sold_price)

    elif args.command == "expire":
        sim_date = str(args.simdate)
        num_of_days = int(args.numdays)
        get_expiry_report_simulated(sim_date, num_of_days)

    else:
        print ("\n Your input is required, based on information from the HELP file.\n"
               " Further optional commands are report, purchase, sell or expire."
               "\n\n Type 'python main.py -h' for additional information.\n")

if __name__ == '__main__':
    main()
