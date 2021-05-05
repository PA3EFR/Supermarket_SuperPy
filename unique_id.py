""""
This function creates an item_id, based on four components of the item:
    1. the date of the change to the stock database (basically today)
    2. the amount of the item
    3. the expiration date of the item.
    4. the purchase date
This 'glued together' through a randomizer forms a unique item_id.
"""

from datetime import date

def unique_id(amount_round, expiration_date, purchase_date):
    import random
    today = str(date.today())
    today_replace = today.replace("-", "")
    amount = str(amount_round)
    expiration_date = expiration_date
    exipration_replace = expiration_date.replace("-", "")
    purchase_date = purchase_date
    purchase_replace = purchase_date.replace("-", "")
    change_id = int(today_replace+amount+exipration_replace+purchase_replace)
    random = random.random()
    change_id = int((change_id * random)/(1e+19))
    return change_id

# print(unique_id(12, "2022-12-31", "2021-04-02"))          # testline
