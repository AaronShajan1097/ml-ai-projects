from selenium import webdriver
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
import os
import time

# Load environment variables
load_dotenv()
EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")

# Set up Selenium
driver = webdriver.Chrome()
driver.get("https://www.linkedin.com/login")
time.sleep(2)

# Log in
driver.find_element(By.ID, "username").send_keys(EMAIL)
driver.find_element(By.ID, "password").send_keys(PASSWORD)
driver.find_element(By.XPATH, '//*[@type="submit"]').click()
time.sleep(5)

# Go to Jobs
driver.get("https://www.linkedin.com/jobs/")
time.sleep(3)

# Search for Python Developer jobs
search_job = driver.find_element(By.XPATH, '//*[@aria-label="Search by title, skill, or company"]')
search_job.send_keys("Python Developer")

search_location = driver.find_element(By.XPATH, '//*[@aria-label="City, state, or zip code"]')
search_location.clear()
search_location.send_keys("United States")
search_location.send_keys(u'\ue007')
time.sleep(5)

# Apply Easy Apply filter
try:
    easy_apply_button = driver.find_element(By.XPATH, '//button[contains(@aria-label, "Easy Apply filter.")]')
    easy_apply_button.click()
    time.sleep(3)
except:
    print("Easy Apply filter not found.")

# Loop through job listings and apply
job_listings = driver.find_elements(By.CSS_SELECTOR, ".job-card-container--clickable")
print(f"Found {len(job_listings)} job listings.")

for job in job_listings:
    job.click()
    time.sleep(3)

    try:
        easy_apply = driver.find_element(By.CSS_SELECTOR, ".jobs-apply-button--top-card button")
        easy_apply.click()
        time.sleep(3)

        submit_button = driver.find_element(By.CSS_SELECTOR, "footer button[aria-label='Submit application']")
        submit_button.click()
        print("Applied successfully!")

        time.sleep(3)
        close_button = driver.find_element(By.CSS_SELECTOR, "button[aria-label='Dismiss']")
        close_button.click()

    except:
        print("No Easy Apply button, skipped.")
        continue

time.sleep(5)
driver.quit()