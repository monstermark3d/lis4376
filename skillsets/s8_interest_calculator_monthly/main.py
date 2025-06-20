1#!/usr/bin/env python3
import functions as f


def main():
    """Program entry. Calling environment to user-defined functions"""
    # initialize variable(s)
    principal = 0.0
    rate = 0.0
    years = 0

    # function calls
    f.get_requirements()
    principal = f.get_principal()
    rate = f.get_rate()
    years = f.get_years()

    f.calculate_interest(principal, rate, years)

if __name__ == "__main__":
    main()