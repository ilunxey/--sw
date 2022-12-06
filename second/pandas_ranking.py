import pandas as pd
def ranking():
    df = pd.read_csv('record.csv')

    df.sort_values('TIME', inplace=True)
    df.reset_index(drop=True, inplace=True)
    return df


