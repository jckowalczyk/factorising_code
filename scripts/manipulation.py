import pandas as pd

def access_country_code(dataframe):
   
    """Function to split combined code columns and remove uncessary columns"""
    
    dataframe = dataframe.copy()
    
    dataframe[["country_code", "parent_code"]] = (dataframe["country_and_parent_code"]
                                                .str.split("_", expand=True))
                                                
    return(dataframe)
    

def drop_cols(dataframe, drop_list): 

    for i in drop_list: 
        dataframe = dataframe.drop(labels = [i], 
                                   axis = 1)
        
        return dataframe


# Convert location_id to integer 

def to_integer(dataframe, variable, match_pat): 
        
        """function to convert a select variable to an integer, replacing any match patterns from the string"""
        
        dataframe = dataframe.copy()
        
        dataframe[variable] = dataframe[variable].astype(str) # cast variable to string first to manipulate
        
        dataframe[variable] = dataframe[variable].str.replace(match_pat, '').astype(int)
        
        return(dataframe)


# Left merge to join datasets together

def join_frames(left_dataframe, right_dataframe, left_column, right_column):
    """
    Function to join the required frames on specified columns, dropping
    unrecessary column
    """
    
    left_dataframe = left_dataframe.copy()
    right_dataframe = right_dataframe.copy()
    
    combined_frames = left_dataframe.merge(right=right_dataframe,
                                           how="left",
                                           left_on=left_column,
                                           right_on=right_column)
                                           
    combined_frames_reduced = combined_frames.drop(labels=[right_column], axis=1)
    
    return combined_frames_reduced