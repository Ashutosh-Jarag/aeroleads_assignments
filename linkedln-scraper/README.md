# 🕵️‍♂️ LinkedIn Profile Scraper

This project is a sophisticated web scraper for gathering public information from LinkedIn profiles. It uses Selenium and `webdriver-manager` to automate browser actions and includes several techniques to avoid detection.

**Note**: The directory is named `linkedln-scraper`, which is a common typo.

## ✨ Features

-   **Automated Login**: Securely logs into LinkedIn using credentials from environment variables.
-   **Profile Scraping**: Extracts key information such as name, headline, location, about section, and current company.
-   **Anti-Detection**: Employs a pool of user-agents, random delays, and other advanced techniques to minimize the risk of being blocked.
-   **CSV Export**: Saves all scraped data into a `linkedin_profiles.csv` file.

## 🛠️ Prerequisites

-   Python 3.8+
-   Google Chrome
-   A LinkedIn account

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/your-repo-name.git
cd aeroleads/linkedln-scraper
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

### 4. Set Up Environment Variables

Create a `.env` file in the `linkedln-scraper` directory and add your LinkedIn credentials:

```env
LINKEDIN_EMAIL="your_linkedin_email@example.com"
LINKEDIN_PASSWORD="your_linkedin_password"
```

### 5. Prepare the Profile List

Edit the `profiles.txt` file to include the LinkedIn profile URLs you want to scrape, one URL per line.

### 6. Run the Scraper

```bash
python scraper.py
```

The script will log in to LinkedIn, visit each profile, scrape the data, and save it to `linkedin_profiles.csv`.

## 📄 Project Structure

```
linkedln-scraper/
├── scraper.py            # The main scraping script
├── requirements.txt      # Python dependencies
├── profiles.txt          # List of LinkedIn profile URLs to scrape
├── linkedin_profiles.csv # Output file with scraped data
└── .env                  # Environment variables (create this file)
```
