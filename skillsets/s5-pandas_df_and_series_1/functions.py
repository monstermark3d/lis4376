"""function library for pandas DataFrames/Series"""
#
# skillset 5 Pandas DataFrames and Series Data Structures by Mark Trombly
#
import pandas as pd
# read data into pandas "global" DataFrame (for access in functions below)
df = pd.read_csv('us_data.csv')

"""
State Capitals: https://www.britannica.com/topic/list-of-state-capitals-in-the-United-States-2119210
State Sizes (sq mi): https://www.britannica.com/topic/largest-U-S-state-by-area
https://note.nkmk.me/en/python-pandas-count-condition/
"""

def get_requirements():
    """function prints program requirements"""
    # print Docstring here:
    # print(get_requirements.__doc__)

    print("\nPandas DataFrames and Series Data Structures")
    print("\nProgram Requirements:\n"
          "Developer: Mark Trombly\n"
          + "1. Working with pandas DataFrames and Series data structures, for tabular data handling.\n"
          + "2. DataFrame: Two-dimensional labeled data structure (i.e., rows/cols).\n"
          + "3. DataFrame: Series collection. Each column is Series sharing same index.\n"
          + "4. Isolating rows and columns.\n"
          + "5. Series: One-dimensional labeled array.\n"
          + "6. Working with Boolean data.\n")
    
def get_data():
    """function to get and display data"""
    print("Print pandas version:")
    print(pd.__version__)

    print("\nDisplay data:")
    print(df)
    print("\nDisplay type:")
    print(type(df)) #DataFrame

def get_bool_data():
    """function to get Boolean data"""
    print("\nPrint Boolean data:\n"
          + "Note: Comparison operator returns Boolean value, parentheses () optional.")
    df_bool = (df == 'DE')
    print(df_bool)

    print("\nDisplay type:")
    print(type(df_bool))    # DataFrame
    return df_bool

def count_bool_cols(your_bool):
    """function to count Boolean columns"""
    # Note: True = 1; False = 0
    bool_sum_cols = your_bool.sum()
    print("\nPrint Boolean cols:\n"
          + "Note: Using sum() method on DataFrame returns Series.")
    print(bool_sum_cols)

    print("\nDisplay type:")
    print(type(bool_sum_cols))

def count_bool_rows(your_bool):
    """function to count Boolean rows"""
    bool_sum_rows = your_bool.sum(axis=1)
    print("\nPrint Boolean rows:\n"
          + "Note: Using sum() method on DataFrame retuns Series.")
    print(bool_sum_rows)

    print("\nDisplay type:")
    print(type(bool_sum_rows))

def count_bool_total(your_bool):
    """function to count Boolean rows"""
    bool_sum_total = your_bool.sum().sum()
    print("\nPrint Boolean total:\n"
          + "Note: Calling sum() on Series returns total count (also, implicitly converts to numpy.int64).")
    print(bool_sum_total)

    print("\nDisplay type:")
    print(type(bool_sum_total))

def get_series_data():
    """function to get Series data"""
    print("\nPrint Square Miles as Series:\n"
          + "Note: Calling one column in DataFrame returns Series object.)")
    my_series = df['total square miles']
    print(my_series)

    print("\nDisplay type:")
    print(type(my_series))
    return my_series

def evaluate_series_data(s_data):
    """function to evaluate Series data"""
    num_states = (s_data >= 100000).sum()
    print("\nPrint number of states with 100,000 or more square miles:")
    print(num_states)

    print("\nDisplay type:")
    print(type(num_states))
    print("Note: sum() used on series objec implicitly converts to numpy.int64_(i.e., scalar value/single number)")

def convert_dataframe_to_numpy_array(your_bool):
    """function to convert DataFrame to NumPy array"""
    print("\nDataFrame converted to NumPy array (ndarray) using \"values\" attribute:")

    print("\nDisplay your_bool type:")
    print(type(your_bool))

    print("\nDisplay your_bool type using \"values\" attribute:")
    print(your_bool.values)

    print("\nDisplay NumPy array using '|values\" attribute:")
    print(your_bool.values)

    print("\nPrint total number of states with two-letter abbreviation == to \"DE\":\n"
          + "Note: Calling sum() method of ndarray calculates sum across entire array.")
    print(your_bool.values.sum())