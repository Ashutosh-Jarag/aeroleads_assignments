#  Job Scraper

This project is a Python-based web scraper designed to automatically collect job postings from LinkedIn. It uses Selenium for web browser automation and BeautifulSoup for parsing HTML content.

## Features

- **Automated Job Search**: Searches for jobs based on a predefined list of roles.
- **Data Extraction**: Scrapes job titles and direct links to the job postings.
- **CSV Export**: Saves the collected data into a `job_results.csv` file for easy analysis.
- **Human-like Behavior**: Utilizes `fake-useragent` and random delays to mimic a real user and avoid detection.

## Prerequisites

- Python 3.8 or higher
- Google Chrome installed
- ChromeDriver compatible with your Chrome version

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/your-repo-name.git
cd aeroleads/job-scraper
```

### 2. Create a Virtual Environment

```bash
python -m venv myenv
source myenv/bin/activate  # On Windows, use `myenv\Scripts\activate`
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Customize Your Search (Optional)

You can edit the `ROLES` list in `job_scraper.py` to search for different job titles:

```python
ROLES = ["Software Engineer", "Product Manager"]
```

### 5. Run the Scraper

```bash
python job_scraper.py
```

The script will open a Chrome browser, perform the searches, and create a `job_results.csv` file with the findings.

## Project Structure

```
job-scraper/
├── job_scraper.py      # The main scraping script
├── requirements.txt    # Python dependencies
└── job_results.csv     # Output file with scraped job data
```
