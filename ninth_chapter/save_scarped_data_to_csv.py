from bs4 import BeautifulSoup
import pandas as pd

html = """
<ul>
    <li>Apple</li>
    <li>Banana</li>
    <li>Cherry</li>
</ul>
"""

soup = BeautifulSoup(html, "html.parser")
items = [li.get_text(strip=True) for li in soup.find_all("li")]

df = pd.DataFrame(items)

df.columns = ["Fruit"]
df.to_csv("./ninth_chapter/fruit.csv", index=None)