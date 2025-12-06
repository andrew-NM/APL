import pandas as pd

df = pd.read_csv("./CSV_handling/students.csv")
result = df[df['Grade'] > 80]
print("Students who scored above 80: ")
print(result)