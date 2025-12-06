from bs4 import BeautifulSoup

html = """<table>
    <tr><th>Name</th><th>Age</th></tr>
    <tr><td>Alice</td><td>25</td></tr>
    <tr><td>Bob</td><td>30</td></tr>
</table>
"""

soup = BeautifulSoup(html, "html.parser")

rows = []
for tr in soup.find_all("tr"):
    cells = [cell.get_text(strip=True) for cell in tr.find_all(["th", "td"])]
    rows.append(cells)

for row in rows:
    print(row)