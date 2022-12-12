import pandas as pd

df = pd.read_excel('게임퀴즈.xlsx')

print(df.loc[0, '문제'])