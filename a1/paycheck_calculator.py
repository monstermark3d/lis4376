#!/usr/bin/env python3

# Note: shebang line only needed in executable files (e.g.,main.py, *not* functions.py)

""" Module doctring example: One-line summary: All multi-lined docstrings have the following parts:

1. One-line summary line
2. Blank line after summary
3. Docstring description, if needed
Resources:
https://realpython.com/documenting-python-code/#docstrings-background
https://www.programiz.com/python-programming/docstrings
"""

print("Pay Check Calculator\n"
    + "Program calculates net pay based upon hours worked, hourly rate and taxes paid.")

print("\nProgram Requirements:\n"
    + "Developer: Mark Trombly\n"
    + "1. Must use float data type for user input.\n"
    + "2. Must round calculations to two decimal places.\n"
    + "3. Must format currency with dollar sign, and two decimal places.")

# Federal income tax rates/brackets: https://www.irs.gov/filing/federal-income-tax-rates-and-brackets
# federal and FICA taxes (Florida - NO state income tax!)
# https://smartasset.com/taxes/florida-paycheck-calculator

# IPO:
# input:
print("\nUser Input:")
hours = float(input("Hours Worked: "))
hourly_rate = float(input("Hourly Rate: $"))
tax_rate = float(input("Tax Rate (percent): "))

# process:
gross_pay = hours * hourly_rate
tax_amount = gross_pay * (tax_rate / 100)
net_pay = gross_pay - tax_amount

# output:
# display results
# Formatting:
# NEW!: https://realpython.com/python-f-strings/
# https://docs.python.org/3/library/string.html#format-specification-min-language
# https://docs.python.org/3/library/string.html#formatexamples
# https://mkaz.blog/code/python-string-format-cookbook/
# Old style: https://docs.python.org/3/library/stdtypes.html#string-formatting
print("\nProgram Output:")
print("Gross Pay:\t", "${0:,.2f}".format(gross_pay))
print("Tax Rate:\t", "{0:.2%}".format(tax_rate/100))
print("Tax Amount:\t", "${0:,.2f}".format(tax_amount))
print("Net Pay:\t", "${0:,.2f}".format(net_pay))