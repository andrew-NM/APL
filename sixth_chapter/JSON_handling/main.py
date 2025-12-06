import pandas as pd

data = {
    "course": "python",
    "duration": "3 months",
    "students": ["Ali", "Sara"]
}

df = pd.DataFrame(data)
df.to_json("./JSON_handling/course.json")
print(pd.read_json('./JSON_handling/course.json'))