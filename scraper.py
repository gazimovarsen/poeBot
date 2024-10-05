from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager

# Load cookies from JSON file
import json

reliable_name = "Boidocafe"

print(reliable_name)

with open('cookies.json', 'r') as f:
    cookies = json.load(f)

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run in headless mode (no GUI)
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Start a Selenium WebDriver session
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# Open the initial page to set up the session
driver.get("https://www.pathofexile.com")
print(1)
# Add the cookies to the session
for name, value in cookies.items():
    driver.add_cookie({
        'name': name,
        'value': value,
        'domain': '.pathofexile.com',  # Set the domain to the website you are targeting
        'path': '/',
    })

# Navigate to the target page after adding cookies
print(1)
driver.get("https://www.pathofexile.com/trade/search/Settlers/2JbnzG0Ik")
print(2)

# Wait until the 'resultset' div is present
try:
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.LINK_TEXT, reliable_name))
    )

    # Get the page source after the element has been confirmed loaded
    html = driver.page_source

    # Parse the HTML with BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

    # Find the div with class 'resultset'
    resultset = soup.find('div', class_='resultset')

    if resultset:
        rows = resultset.find_all('div', class_='row')

        for row in rows:
            stack_size = row.find('span', class_='stackSize').text.strip() if row.find('span', class_='stackSize') else 'N/A'

            exact_price = row.find('span', class_='s sorted sorted-asc').find_all('span')[1].text.strip() if row.find('span', class_='s sorted sorted-asc') else 'N/A'

            account_name = row.find('span', class_='profile-link').find('a').text.strip() if row.find('span', class_='profile-link') else 'N/A'

            # Print the extracted information
            print(f"@{account_name} Hello, I want to buy your {stack_size}x Harvest Scarab of Doubling for {int(stack_size) * int(exact_price)} Chaos Orbs")
            print(f"Stack Size: {stack_size}")
            print(f"Exact Price: {exact_price}")
            print(f"Account Name: {account_name}")
            print('-' * 30)

    else:
        print("Resultset div not found.")

except Exception as e:
    print("An error occurred:", e)

finally:
    driver.quit()
