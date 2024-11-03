from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

try:
    # Step 1: Open Instagram and log in
    driver.get("https://www.instagram.com/accounts/login/")
    sleep(3)  # Wait for the page to load

    # Enter username and password (replace with your actual credentials)
    username = driver.find_element(By.XPATH, "//input[@name='username']")
    username.send_keys("your_username")
    password = driver.find_element(By.XPATH, "//input[@name='password']")
    password.send_keys("your_password")

    # Click the login button
    login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    login_button.click()
    sleep(5)  # Wait for login to complete

    # Step 2: Navigate to the target profile page
    driver.get("https://www.instagram.com/guviofficial/")
    sleep(3)  # Wait for the profile page to load

    # Step 3: Handle potential pop-ups
    try:
        not_now_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Not Now')]"))
        )
        not_now_button.click()
    except Exception as e:
        print("No 'Not Now' button found, continuing...")

    # Optional: Capture a screenshot to help troubleshoot if necessary
    driver.save_screenshot("instagram_profile_debug.png")

    # Step 4: Extract followers and following counts using explicit wait
    followers = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//a[contains(@href,'followers')]/span"))
    ).get_attribute("title")
    following = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//a[contains(@href,'following')]/span"))
    ).text

    print("Followers:", followers)
    print("Following:", following)

finally:
    # Close the browser
    driver.quit()
