import pandas as pd
import numpy as np
def ranking(di):
    if di == 'easy':
        df = pd.read_csv('record_easy.csv')
    elif di == 'normal':
        df = pd.read_csv('record_normal.csv')
    else:
        df = pd.read_csv('record_normal.csv')

    df.sort_values('TIME', inplace=True)
    df.reset_index(drop=True, inplace=True)
    return df