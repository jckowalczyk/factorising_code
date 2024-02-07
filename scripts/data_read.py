import pandas as pd 

# Read in data and clean col names

def read_cleaned_data(filepath): 
    
    """reads in a dataframe from a specified filepath, and formats colname to lowercase, replace space with _"""
    
    dataframe = pd.read_csv(filepath)

    dataframe.columns = dataframe.columns.str.lower()
    dataframe.columns = dataframe.columns.str.replace(" ", "_")

    return(dataframe)