import csv
import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

# Configure
ROLES = ["Data Analyst", "Machine Learning Engineer"]   # roles to search
OUTPUT_FILE = "job_results.csv"

def make_driver():
    ua = UserAgent()
    options = Options()
    options.add_argument("--window-size=1200,900")
    options.add_argument(f"--user-agent={ua.random}")
    options.add_argument("--disable-blink-features=AutomationControlled")
    driver = webdriver.Chrome(options=options)
    return driver

def scrape_linkedin_jobs(role):
    driver = make_driver()
    print(f"🔍 Searching jobs for: {role}")
    search_url = f"https://www.linkedin.com/jobs/search/?keywords={role.replace(' ', '%20')}"
    driver.get(search_url)
    time.sleep(5)

    soup = BeautifulSoup(driver.page_source, "html.parser")
    job_cards = soup.select("a.base-card__full-link")
    jobs = []

    for i, job in enumerate(job_cards[:10]):
        link = job.get("href")
        title = job.text.strip()
        jobs.append({
            "id": f"{role[:3].upper()}_{i+1}",
            "job_name": title,
            "hr_name": "",
            "hr_email": "",
            "company_email": "",
            "link": link
        })

    driver.quit()
    print(f"✅ Found {len(jobs)} jobs for {role}")
    return jobs

def save_to_csv(jobs):
    keys = ["id", "job_name", "hr_name", "hr_email", "company_email", "link"]
    with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        writer.writerows(jobs)
    print(f"💾 Saved {len(jobs)} jobs to {OUTPUT_FILE}")

def main():
    all_jobs = []
    for role in ROLES:
        role_jobs = scrape_linkedin_jobs(role)
        all_jobs.extend(role_jobs)
        time.sleep(random.randint(3, 6))
    save_to_csv(all_jobs)

if __name__ == "__main__":
    main()
