"""function library for pandas DataFrames/Series"""
#
# skillset 6 Pandas DataFrames and Series Data Structures by Mark Trombly
#
import pandas as pd

def get_requirements():
    """function prints program requirements"""
    # print Docstring here:
    # print(get_requiremnets.__doc__)

    print("\nPandas DataFrames and Series Data Structures")
    print("\nProgram Requirements:\n"
          "Developer: Mark Trombly\n"
          + "1. Work with pandas DataFrames and Series data structures, for tabular data handling.\n"
          + "2. DataFrame: Two-dimensional labeled data structure (i.e., rows/cols).\n"
          + "3. DataFrame: Series collection. Each column is Series sharing same index.\n"
          + "4. Use multiple conditions: not, and, or.\n"
          + "5. Logical operators, numeric comparisons, counting/comparing NaN/non-NaN values.\n"
          + "\nNote: not, and, or statements require truth-values.\n"
          + "Pandas requires \"bitwise\" (overloaded operators): not(~), and (&), or (|).")
    
def get_data():
    """function to get and display data"""
    print("\nPrint pandas version:")
    print(pd.__version__)

    # read data into DataFrame
    df = pd.read_csv('titanic.csv', encoding='utf-8')
    
    print("\nDisplay data:")
    print(df)

    print("\nDisplay type:")
    print(type(df)) # DataFrame type

    print("\nTotal number of passengers: ",end="")
    print(len(df))

    return df

def convert_data(my_titanic_df):
    """
    Finds non-numeric elements in Pandas Series.
    pars: Pandas Series
    Returns: Pandas Series containing non-numeric elements.
    """

    # check or missing values using Pandas isnull() and isna() functions
    # pd.to_numeric(ser,es, errors='coerce'):
    # Tries to convert each element of series input to numeric value
    # errors='coerce' replaces elements that can't be converted to number with NaN (Not a Number)

    titanic_series = my_titanic_df['age']
    numeric_and_non_numeric_data = pd.to_numeric(titanic_series, errors='coerce')
    nun_numeric_data = titanic_series[numeric_and_non_numeric_data.isna()]
    numeric_data = titanic_series[~numeric_and_non_numeric_data.isna()]

    return numeric_and_non_numeric_data, numeric_and_non_numeric_data, numeric_data

def and_operator(my_titanic_df):
    """function to evaluate bitwise AND operator"""
    total_non_survivors = (my_titanic_df['survived'] == 'no').sum()
    print("\nTotal number perished: ", end="")
    print(total_non_survivors)

    print("\nTotal males perished: ", end="")
    male_non_survivors = ((my_titanic_df['gender'] == 'male') & (my_titanic_df['survived'] == 'no')).sum()
    print(male_non_survivors)

    print("\nPercentage of males who died from total perished: ", end="")
    num_deceased_males_to_total_deceased = male_non_survivors/total_non_survivors
    print(f"{num_deceased_males_to_total_deceased:.2%}")

def or_operator(my_titanic_series):
    """function to evaluate bitwise OR operator"""
    # use negation and isnull() function to remove missing values to evaluate numeric data
    titanic_series = pd.Series(my_titanic_series, name='age')

    # convert Series to DataFrame
    my_titanic_df = titanic_series.to_frame()

    # check data/type
    # print(my_df)
    # print(type(my_df))

    old_young_passengers = my_titanic_df[(my_titanic_df['age'] > 70) | (my_titanic_df['age'] < 5)]

    print("\nTotal number of passengers older than 70 OR younger than 5: ", end="")
    print(len(old_young_passengers))

def not_operator(my_titanic_df):
    """function to evaluate bitwise NOT operator"""

    unique_countries = my_titanic_df['country'].drop_duplicates()

    print("\nTotal number of unique home countries: ", end="")
    print(len(unique_countries))

    # check type 
    # print(type(unique_countries))

    titanic_series = pd.Series(unique_countries, name='country')

    # convert series to DataFrame
    countries_df = titanic_series.to_frame()

    # excluded home countries
    excluded_countries = ['England', 'France']

    # filter DataFame using NOT with isin() function
    non_excluded_countries = countries_df[~countries_df['country'].isin(excluded_countries)]

    # verify nonexcluded counties
    # print(non_excluded_countries)

    print("\nTotal number of unique home countries, not including England or France: ", end="")
    print(len(non_excluded_countries))