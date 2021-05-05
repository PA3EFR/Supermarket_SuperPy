SuperPy - a supermarket stock management tool

In this report three technical elements of my assignment are highlighted. I present the issue, and my way of finding the solution. In all three elements the third rule of Zen in Python applied: "Simple is better then complex".

1. Unique numbers for the same product name

The initial stock items might have similar, if not exact, same prodcut name, expiration dates and other item attributes. However, the items have a requirement to be unique in the identification. It is for that reason that a unique_id.py has been written, using a complex code to generate a unique number to identical products. 

2. Initial stock

My assumption was that the super market for this assignment already existed and had already a filled stock.csv file that had to be imported and serve as basis for my programm. The stock.csv file is copied to the initial_files directory, from where all other program modules deduct their required information.

3. Shifted start date for expiration check

It has been a challenge to not only find expiration dates from stock items, but also to shift the start date for that check, together with a calculatable period of time from that shifted start date. The finalized expire.py module holds two functions: one for the initial health check of the imported stock-file (point 2), the second function for processing expiration information based on a shifted start date of the process.