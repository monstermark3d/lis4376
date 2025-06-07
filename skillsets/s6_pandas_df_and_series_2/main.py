#!/usr/bin/env python3
#
# skillset 6 Pandas DataFrames and Series Data Structures by Mark Trombly
#
"""module docstring goes here"""
import functions as f

def main():
    """program entry"""
    f.get_requirements()
    titanic_df = f.get_data()
    f.and_operator(titanic_df)
    converted_all, converted_non_num, converted_num = f.convert_data(titanic_df)
    f.or_operator(converted_num)
    f.not_operator(titanic_df)


if __name__ == "__main__":
    main()