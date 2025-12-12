from bs4 import BeautifulSoup
import requests

html_text = requests.get("https://realpython.github.io/fake-jobs/").text
soup = BeautifulSoup(html_text, "lxml")
jobs = soup.find_all("div", class_="column is-half")

for job in jobs:
    job_name = job.find("h2", class_="title is-5").text
    company_name = job.find("h3", class_="subtitle is-6 company").text
    location = job.find("p", class_="location").text.strip()
    publish_date = job.find("time").text
    print("=" * 50)
    print("Job Info: ")
    print(f"Job name: {job_name}")
    print(f"Company name: {company_name}")
    print(f"Job location: {location}")
    print(f"Publish date: {publish_date}")
