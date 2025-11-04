# scraper.py
import os
import time
import csv
import random
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException, TimeoutException, WebDriverException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Load environment variables
load_dotenv()
EMAIL = os.getenv("LINKEDIN_EMAIL")
PASSWORD = os.getenv("LINKEDIN_PASSWORD")
CHROME_DRIVER_PATH = os.getenv("CHROMEDRIVER_PATH", "chromedriver")  # change if needed

# Random user-agent pool
user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Safari/605.1.15",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1",
]

def make_driver(proxy: str=None, headless: bool=False):
    options = Options()
    if headless:
        options.add_argument("--headless=new")
        options.add_argument("--disable-gpu")

    user_agent = random.choice(user_agents)
    options.add_argument(f"--user-agent={user_agent}")
    options.add_argument("--window-size=1200,900")
    options.add_argument("--disable-blink-features=AutomationControlled")

    if proxy:
        options.add_argument(f'--proxy-server={proxy}')

    # Avoid Selenium detection flags
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)

    # ✅ WebDriverManager automatically handles ChromeDriver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
        "source": """
            Object.defineProperty(navigator, 'webdriver', {get: () => undefined})
        """
    })
    return driver

def linkedin_login(driver):
    driver.get("https://www.linkedin.com/login")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "username")))
    driver.find_element(By.ID, "username").send_keys(EMAIL)
    driver.find_element(By.ID, "password").send_keys(PASSWORD)
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    # Wait for homepage
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "global-nav-search")))

def safe_get_text(driver, by, selector):
    try:
        return driver.find_element(by, selector).text.strip()
    except NoSuchElementException:
        return ""

def scrape_profile(driver, url):
    result = {"url": url, "name": "", "headline": "", "location": "", "about": "", "current_company": ""}
    try:
        driver.get(url)
        WebDriverWait(driver, 8).until(EC.presence_of_element_located((By.TAG_NAME, "h1")))
        time.sleep(1.0)  # short wait
        result["name"] = safe_get_text(driver, By.TAG_NAME, "h1")

        try:
            result["headline"] = driver.find_element(By.CSS_SELECTOR, ".text-body-medium.break-words").text
        except NoSuchElementException:
            result["headline"] = safe_get_text(driver, By.CSS_SELECTOR, ".pv-top-card--list li")

        result["location"] = safe_get_text(driver, By.CSS_SELECTOR, ".pv-top-card--list-bullet")

        try:
            about_el = driver.find_element(By.CSS_SELECTOR, "section.pv-about-section .pv-about__summary-text")
            result["about"] = about_el.text
        except NoSuchElementException:
            result["about"] = ""

        try:
            exp = driver.find_element(By.CSS_SELECTOR, "#experience-section li")
            result["current_company"] = exp.text.split("\n")[0]
        except NoSuchElementException:
            result["current_company"] = ""

    except (TimeoutException, WebDriverException) as e:
        print(f"Failed to load {url}: {e}")
    return result

def main():
    # Read URLs
    with open("profiles.txt", "r") as f:
        profiles = [line.strip() for line in f if line.strip()]

    driver = make_driver(headless=False)
    try:
        linkedin_login(driver)
        results = []
        for i, url in enumerate(profiles, start=1):
            print(f"[{i}/{len(profiles)}] Scraping {url}")
            item = scrape_profile(driver, url)
            results.append(item)
            time.sleep(3 + (i % 3))  # delay between requests
    finally:
        driver.quit()

    # Save to CSV
    keys = ["url", "name", "headline", "location", "about", "current_company"]
    with open("linkedin_profiles.csv", "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=keys)
        writer.writeheader()
        for r in results:
            writer.writerow(r)
    print("✅ Done! Output saved to linkedin_profiles.csv")

if __name__ == "__main__":
    main()
