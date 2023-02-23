
import os
import pandas as pd





def to_datetime(df, col):
    
    '''this function takes in a dataframe, changes the 'date' col
    to datetime and then sets it as the index, [then creates day and month
    columns, along with total 'sale_amount' col,] and returns the 
    modified dataframe
    '''
    
    # change 'date' to datetime format
    df[col] = pd.to_datetime(df[col])
    
    
    # dropping and renaming
    df = df.drop(columns = ['deleted_at', 'slack', 'created_at', 'updated_at'])
    df = df.rename(columns = {'path' : 'url_path'})
    
    return df


