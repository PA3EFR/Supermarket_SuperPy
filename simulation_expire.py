import argparse
from expire import get_expiry_report_simulated, get_expiry_report_today
from datetime import date, timedelta, datetime
""""
This module takes the number of days for comparison to the expiration date
of products in de inventory database.
Numbers can be negative if simulated to the past.
"""
ap = argparse.ArgumentParser()
ap.add_argument("-num", required=False, help="Number of calendar days for the simulation (days in the past: negative value). Default: 0 (zero).")
ap.add_argument("-date", required=False, help="Date if simulation start_date is NOT today (input yyyy-mm-dd). Default: today.")
args = vars(ap.parse_args()) # change commandline arguments in dictionary 'args'. Key: argument name, value: content

if args["num"] == None:
    num_of_days = 0
else:
    num_of_days = int(args["num"])
    
if args["date"] == None:
    sim_date = date.today()
else:
    sim_date = date.fromisoformat(args["date"])

print (f"\n This simulation may run with arguments for a different start_date and/or number of days.")
get_expiry_report_simulated(sim_date, num_of_days )
print (f"\n This simulation may run with arguments for a different start_date and/or number of days.")
