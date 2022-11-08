import pandas as pd 
from pandas_profiling import ProfileReport

df=pd.read_csv(r'C:\Users\delhi\OneDrive\Desktop\DS project\7. Udemy Courses.csv')
print(df)

profile=ProfileReport(df)
profile.to_file(output_file="udemy.html")