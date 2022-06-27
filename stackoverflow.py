import requests
from bs4 import BeautifulSoup

def get_last_page(keyword):
    url = f"https://stackoverflow.com/jobs/companies?tl={keyword}"
    result = requests.get(url)
    soup = BeautifulSoup(result.text, "html.parser")
    pagination = soup.find("div", {"class": "s-pagination"}).find_all("a")[-2].find("span").string
    return int(pagination)
    
def extract_jobs(last_page):
    companys = []
    for i in range(last_page):
        url = f"https://stackoverflow.com/jobs/companies?tl=linux&pg={i+1}"
        result = requests.get(url)
        soup = BeautifulSoup(result.text, "html.parser")
        company_lists = soup.find("div", {"class": "company-list"}).find_all("div", {"class": "-company"})
        for company_list in company_lists:
            try:
                location_and_title = company_list.find_all("div", {"class": "flex--item fc-black-500 fs-body1"})
                title = location_and_title[1].get_text().strip()
                location = location_and_title[0].get_text().strip()
                company = company_list.find("a", {"class": "s-link"}).string.strip()
                link = company_list.find("a", {"class": "s-link"})["href"]
                companys.append({
                    'title': title,
                    'location': location,
                    'company': company,
                    'link': f"https://stackoverflow.com{link}"
                })
            except (AttributeError, TypeError):
                pass
    return companys

def get_stackoverflow_companys(word):
  last_page = get_last_page(word)
  so_companys = extract_jobs(last_page)
  return so_companys