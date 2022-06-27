import requests
from bs4 import BeautifulSoup

def get_wwr_jobs(word):
    url = f"https://weworkremotely.com/remote-jobs/search?term={word}"
    result = requests.get(url)
    soup = BeautifulSoup(result.text, "html.parser")
    jobs = soup.find("div", {"class": "jobs-container"}).find_all("li")
    wwr_jobs = []
    for job in jobs:
        try:
            title = job.find("span", {"class": "title"}).get_text().strip()
            company = job.find("span", {"class": "company"}).get_text().strip()
            location = job.find("span", {"class": "region company"}).get_text().strip()
            link = job.find("a", recursive=False)["href"]
            wwr_jobs.append({
                'titlt': title,
                'company': company,
                'location': location,
                'link': link
            })
        except (AttributeError, TypeError):
            pass
    return wwr_jobs
