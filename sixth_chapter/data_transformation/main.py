import pandas as pd

tree_path = "./data_transformation"
df = pd.read_csv(f"{tree_path}/data.csv")
data_dict = {"people": df.to_dict()}
pd.DataFrame(data_dict).to_json(f"{tree_path}/data.json", orient="records")