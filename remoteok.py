import requests
from bs4 import BeautifulSoup


def get_remoteok_jobs(keyword):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.105 Safari/537.36'
        }
    remoteok_jobs = []
    url = f"https://remoteok.com/remote-dev+{keyword}-jobs"
    result = requests.get(url, headers=headers)
    soup = BeautifulSoup(result.text, "html.parser")
    if soup.find("table") is None:
        pass
    else:
        jobs = soup.find("table", {"id": "jobsboard"}).find_all("tr", {"class": "job"})
        for job in jobs:
            try:
                remoteok_job = extract_job(job)
                remoteok_jobs.append(remoteok_job)
            except (AttributeError, TypeError):
                pass
    return remoteok_jobs
            

def extract_job(html):
    title = html.find("h2", {"itemprop": "title"}).get_text().strip()
    company = html["data-company"]
    location = html.find("div", attrs={"title":True}).get_text().strip()
    link = "https://remoteok.com/l/" + html["data-id"]
    return {
        'title': title,
        'company': company,
        'location': location,
        'link': link
    }