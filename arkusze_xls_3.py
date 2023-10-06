import pandas as pd
import numpy as np
import openpyxl

techno = ['Spark', 'Pandas', 'Python', 'PHP']
fee = [25000, 20000, 15000, 18000]
duration = ['50 Days','35 Days',np.nan,'30 Days','30 Days']
columns = ['Courses', 'Fee', 'Duration','Discont']
discount = [2000,1000,3000,1000,800,500]

df = pd.DataFrame(
    list(zip(techno, fee,duration,discount)), # utnie dane które są większe
    columns=columns
)

print(df)
#   Courses    Fee Duration  Discont
# 0   Spark  25000  50 Days     2000
# 1  Pandas  20000  35 Days     1000
# 2  Python  15000      NaN     3000
# 3     PHP  18000  30 Days     1000


df.to_excel('Courses.xlsx')
df.to_excel('Courses.xls', engine='openpyxl')



