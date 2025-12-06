import pandas as pd
import openpyxl

data = [
    [1, "Andrew Naeem", 1000000000],
    [2, "Sayed Mohamed", 3000],
    [3, "Mohamed Sayed", 2000],
]

columns = ["ID", "Name", "Salary"]
path = "./Excel_handling/employees.xlsx"
df = pd.DataFrame(data, columns=columns)
df.to_excel(path, engine="openpyxl")
print(pd.read_excel(path))