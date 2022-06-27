import re
import requests
from bs4 import BeautifulSoup

def get_last_page(URL):
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, "html.parser")
    job_lists = soup.find_all("div", {"class": "fs-unmask"})
    job_lists_num = int(len(job_lists))
    total_text = soup.find("div", {"id":"searchCountPages"}).string.strip()
    total_num = int(re.sub(r'[^0-9]', '', total_text[2:]))
    if total_num%job_lists_num == 0:
        return int(total_num/job_lists_num)
    else:
        return int(total_num/job_lists_num) + 1

def extract_job(html):
    title = html.find("h2",{"class": "jobTitle"}).find("span", attrs={"title":True}).string
    #new job인 경우에는 jobTitle-newJob이라는 class가 있음
    company = html.find("span", {"class": "companyName"})
    if company:
      company_anchor = company.find("a")
      if company_anchor is not None:
        company = str(company_anchor.string)
      else:
        company = str(company.string)
      company = company.strip()
    else:
      company = None
    location = html.find("div",{"class": "companyLocation"}).string
    job_id = html.find("a", {"class": "jcs-JobTitle"})["data-jk"]
    return {
      'title': title,
      'company': company,
      'location': location,
      "link": f"https://www.indeed.com/채용보기?jk={job_id}"
      #"link": f"https://www.indeed.com/viewjob?jk={job_id}" 영문 페이지
    }
    
def extract_jobs(last_page, URL):
    jobs = []
    for page in range(last_page):
        result = requests.get(f"{URL}{page*10}")
        soup = BeautifulSoup(result.text, "html.parser")
        results = soup.find_all("div", {"class": "fs-unmask"})
        for result in results:
            job = extract_job(result)
            jobs.append(job)
    return jobs

def get_indeed_jobs(word):
  url = f"https://kr.indeed.com/jobs?q={word}&start="
  last_page = get_last_page(url)
  jobs = extract_jobs(last_page, url)
  return jobs