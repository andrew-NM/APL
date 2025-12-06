import pandas as pd

data = [
    ["Andrew", "20", 100],
    ["Mohamed", "19", 90],
    ["John", "18", 50]
]

columns = ["Name", "Age", "Score"]

df = pd.DataFrame(data, columns=columns)

print(df[df["Score"] > 80])